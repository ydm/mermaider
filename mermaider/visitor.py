import enum
from mermaider.ast import type_string, wrap
from mermaider import types


SKIPPED = (
    types.ImportDirective,
    types.ModifierDefinition,
    types.PragmaDirective,
)


class Kind(enum.Enum):
    STRUCT = enum.auto()
    CONTRACT = enum.auto()
    INTERFACE = enum.auto()
    LIBRARY = enum.auto()


class Class:
    def __init__(self, kind):
        '''
        https://mermaid.js.org/syntax/classDiagram.html#defining-relationship

        Inheritance: Derived --|> Base
        Composition: *--
        Aggreagation: Aggregator --o Aggregated
        Association: -->
        Link (Solid): --
        Dependency: A ..> Dependency
        Realization: Derived ..|> Interface
        Link (Dashed): ..
        '''
        self.kind = kind
        self.annotation = ''
        self.members = []
        #
        self.aggregates = []
        self.bases = []
        self.dependencies = []
        self.links = []

    def add_aggregate(self, agg):
        if agg not in self.aggregates:
            self.aggregates.append(agg)


def list_names(nodes):
    allowed = ('EnumValue', 'VariableDeclaration')
    def f(param):
        assert param.nodeType in allowed, param.nodeType
        return param.name
    return ', '.join(map(f, nodes))


def list_types(nodes):
    def f(node):
        assert node.nodeType == 'VariableDeclaration', node.nodeType
        ts = type_string(node)
        return {
            'uint': 'uint256',
            'int': 'int256',
        }.get(ts, ts)
    return ','.join(map(f, nodes))


class Visitor:
    def __init__(self):
        self.classes = {}

    def _add_class(self, root, desc):
        assert root.nodeType in ('ContractDefinition', 'StructDefinition')
        error = f'{root.canonicalName} conflicts with another declaration'
        self.classes[root.canonicalName] = desc

    def visit_ContractDefinition(self, root):
        # Determine kind.
        kind = getattr(Kind, root.contractKind.upper())
        # Instantiate and add to class registry.
        desc = Class(kind)
        self._add_class(root, desc)
        # Write base classes.
        desc.bases.extend(x.baseName.name for x in root.baseContracts)
        # Write annotation.
        if root.abstract:
            assert desc.kind == Kind.CONTRACT, f'have={desc.kind} want=CONTRACT'
            desc.annotation = 'abstract'
        elif desc.kind != Kind.CONTRACT:
            desc.annotation = desc.kind.name.lower()
        # Write members: variables, functions, etc.
        def f(node):
            if isinstance(node, types.ModifierDefinition):
                return
            if isinstance(node, types.StructDefinition):
                desc.dependencies.append(node.canonicalName)
            elif isinstance(node, types.UsingForDirective):
                desc.links.append(node.libraryName.name)
            elif (isinstance(node, types.VariableDeclaration) and
                  type_string(node).startswith('contract ')):
                desc.add_aggregate(type_string(node)[9:])
            # Keep traversing.  If the result is a string, (and that's
            # a bit hacky), it's included in the members list.
            res = self.visit(node)
            if isinstance(res, str):
                desc.members.append(res)
            elif not isinstance(node, types.StructDefinition):
                raise ValueError(node)
        for node in root.nodes:
            f(node)

    def visit_EnumDefinition(self, root):
        params = list_names(root.members)
        return f'event {root.name}({params})'

    def visit_ErrorDefinition(self, root):
        params = list_names(root.parameters.parameters)
        return f'error {root.name}({params})'

    def visit_EventDefinition(self, root):
        params = list_names(root.parameters.parameters)
        return f'event {root.name}({params})'

    def visit_FunctionDefinition(self, root):
        if root.kind == 'receive':
            signature = 'receive()'
        else:
            params = list_types(root.parameters.parameters)
            signature = f'{root.name}({params})'
        # Check the hash selector just to make sure the sig is right.
        if want := root.functionSelector:
            try:
                from eth_hash.auto import keccak
            except ImportError:
                pass
            else:
                have = keccak(signature.encode('ascii')).hex()[:8]
                error = (f'name={root.name} '
                         f'signature={signature} '
                         f'have={have} '
                         f'want={want}')
                assert have == want, error
        vis = ('+' if root.visibility in ('external', 'public') else
               '-' if root.visibility == 'private' else
               '#' if root.visibility == 'internal' else
               '??')
        abstract = '' if root.implemented else '*'
        return f'{vis}{signature}{abstract}'

    def visit_StructDefinition(self, root):
        desc = Class(Kind.STRUCT)
        self._add_class(root, desc)
        desc.members.append('<<struct>>')
        for member in root.members:
            desc.members.append(self.visit(member))

    def visit_UsingForDirective(self, root):
        name = root.libraryName.name
        return f'using {name} for {type_string(root)}'

    def visit_VariableDeclaration(self, root):
        vi = '+' if root.visibility in ('external', 'public') else '-'
        ts = type_string(root)
        # The mapping is problematic, so let's tint it a bit.
        if ts.startswith('mapping'):
            ts = (ts
                  .replace('(', '[')
                  .replace(')', ']')
                  .replace('=>', ','))
        return f'{vi}{ts} {root.name}'

    def visit(self, root):
        '''
        visit() is tricky:
        (0) It skips all nodes listed in `SKIPPED`.
        (1) It updates `self.classes` if the visited node one of:
          - ContractDefinition
          - StructDefinition
        (2) Returns a `members` string for all other nodes.
        '''
        if isinstance(root, SKIPPED):
            pass
        elif isinstance(root, types.ContractDefinition):
            self.visit_ContractDefinition(root)
        elif isinstance(root, types.EnumDefinition):
            return self.visit_EnumDefinition(root)
        elif isinstance(root, types.ErrorDefinition):
            return self.visit_ErrorDefinition(root)
        elif isinstance(root, types.EventDefinition):
            return self.visit_EventDefinition(root)
        elif isinstance(root, types.FunctionDefinition):
            return self.visit_FunctionDefinition(root)
        elif isinstance(root, types.SourceUnit):
            [self.visit(node) for node in root.nodes]
        elif isinstance(root, types.StructDefinition):
            self.visit_StructDefinition(root)
        elif isinstance(root, types.UsingForDirective):
            return self.visit_UsingForDirective(root)
        elif isinstance(root, types.VariableDeclaration):
            return self.visit_VariableDeclaration(root)
        else:
            raise ValueError(type(root))


def to_mermaid(artifacts):
    visitor = Visitor()
    for filename, ast in artifacts['sources'].items():
        unit = wrap(ast['AST'])
        visitor.visit(unit)

    print('---')
    print('title: github.com/ydm/mermaider')
    print('---')
    print('classDiagram')
    for name, desc in visitor.classes.items():
        # Class definition.
        lines = [f'class `{name}` {{']
        if desc.annotation:
            lines.append(f'    <<{desc.annotation}>>')
        lines.extend([f'    {prop}' for prop in desc.members])
        lines.append('}')
        print('\n'.join(lines))
        # Relations.
        for aggregate in desc.aggregates:
            print(f'`{name}` --o `{aggregate}`')
        for base in desc.bases:
            if visitor.classes[base].kind == Kind.CONTRACT:
                print(f'`{name}` --|> `{base}`')
            elif visitor.classes[base].kind == Kind.INTERFACE:
                print(f'`{name}` ..|> `{base}`')
        for dep in desc.dependencies:
            print(f'`{name}` ..> `{dep}`')
        for library in desc.links:
            print(f'`{name}` .. `{library}`')
