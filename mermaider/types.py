from collections import namedtuple
from os import name


ArrayTypeName = namedtuple(
    'ArrayTypeName',
    ['baseType', 'id', 'length', 'nodeType', 'src', 'typeDescriptions'],
)

Assignment = namedtuple(
    'Assignment',
    ['id',
     'isConstant',
     'isLValue',
     'isPure',
     'lValueRequested',
     'leftHandSide',
     'nodeType',
     'operator',
     'rightHandSide',
     'src',
     'typeDescriptions'],
)

BinaryOperation = namedtuple(
    'BinaryOperation',
    ['commonType',
     'id',
     'isConstant',
     'isLValue',
     'isPure',
     'lValueRequested',
     'leftExpression',
     'nodeType',
     'operator',
     'rightExpression',
     'src',
     'typeDescriptions'],
)

Block = namedtuple(
    'Block',
    ['id', 'nodeType', 'src', 'statements'],
)

Break = namedtuple(
    'Break',
    ['id', 'nodeType', 'src'],
)

Conditional = namedtuple(
    'Conditional',
    ['condition',
     'falseExpression',
     'id',
     'isConstant',
     'isLValue',
     'isPure',
     'lValueRequested',
     'nodeType',
     'src',
     'trueExpression',
     'typeDescriptions'],
)

Continue = namedtuple(
    'Continue',
    ['id', 'nodeType', 'src']
)

ContractDefinition = namedtuple(
    'ContractDefinition',
    ['abstract',
     'baseContracts',
     'canonicalName',
     'contractDependencies',
     'contractKind',
     'documentation',
     'fullyImplemented',
     'id',
     'internalFunctionIDs',
     'linearizedBaseContracts',
     'name',
     'nameLocation',
     'nodeType',
     'nodes',
     'scope',
     'src',
     'usedErrors',
     'usedEvents'],
)

ElementaryTypeName = namedtuple(
    'ElementaryTypeName',
    ['id', 'name', 'nodeType', 'src', 'stateMutability', 'typeDescriptions'],
)

ElementaryTypeNameExpression = namedtuple(
    'ElementaryTypeNameExpression',
    ['argumentTypes',
     'id',
     'isConstant',
     'isLValue',
     'isPure',
     'lValueRequested',
     'nodeType',
     'src',
     'typeDescriptions',
     'typeName'],
)

EmitStatement = namedtuple(
    'EmitStatement',
    ['eventCall', 'id', 'nodeType', 'src'],
)

EnumDefinition = namedtuple(
    'EnumDefinition',
    ['canonicalName',
     'documentation',
     'id',
     'members',
     'name',
     'nameLocation',
     'nodeType',
     'src'],
)

EnumValue = namedtuple(
    'EnumValue',
    ['id', 'name', 'nameLocation', 'nodeType', 'src'],
)

ErrorDefinition = namedtuple(
    'ErrorDefinition',
    ['id', 'name', 'nameLocation', 'nodeType', 'parameters', 'src'],
)

EventDefinition = namedtuple(
    'EventDefinition',
    ['anonymous',
     'documentation',
     'eventSelector',
     'id',
     'name',
     'nameLocation',
     'nodeType',
     'parameters',
     'src'],
)

ExpressionStatement = namedtuple(
    'ExpressionStatement',
    ['expression', 'id', 'nodeType', 'src'],
)

ForStatement = namedtuple(
    'ForStatement',
    ['body',
     'condition',
     'id',
     'initializationExpression',
     'isSimpleCounterLoop',
     'loopExpression',
     'nodeType',
     'src'],
)

FunctionCall = namedtuple(
    'FunctionCall',
    ['argumentTypes',
     'arguments',
     'expression',
     'id',
     'isConstant',
     'isLValue',
     'isPure',
     'kind',
     'lValueRequested',
     'nameLocations',
     'names',
     'nodeType',
     'src',
     'tryCall',
     'typeDescriptions'],
)

FunctionCallOptions = namedtuple(
    'FunctionCallOptions',
    ['argumentTypes',
     'expression',
     'id',
     'isConstant',
     'isLValue',
     'isPure',
     'lValueRequested',
     'names',
     'nodeType',
     'options',
     'src',
     'typeDescriptions'],
)

FunctionDefinition = namedtuple(
    'FunctionDefinition',
    ['baseFunctions',
     'body',
     'documentation',
     'functionSelector',
     'id',
     'implemented',
     'kind',
     'modifiers',
     'name',
     'nameLocation',
     'nodeType',
     'overrides',
     'parameters',
     'returnParameters',
     'scope',
     'src',
     'stateMutability',
     'virtual',
     'visibility'],
)

FunctionTypeName = namedtuple(
    'FunctionTypeName',
    ['id',
     'nodeType',
     'parameterTypes',
     'returnParameterTypes',
     'src',
     'stateMutability',
     'typeDescriptions',
     'visibility'],
)

Identifier = namedtuple(
    'Identifier',
    ['argumentTypes',
     'id',
     'name',
     'nodeType',
     'overloadedDeclarations',
     'referencedDeclaration',
     'src',
     'typeDescriptions'],
)

IdentifierPath = namedtuple(
    'IdentifierPath',
    ['id', 'name', 'nameLocations', 'nodeType', 'referencedDeclaration', 'src'],
)

IfStatement = namedtuple(
    'IfStatement',
    ['condition', 'falseBody', 'id', 'nodeType', 'src', 'trueBody'],
)

ImportDirective = namedtuple(
    'ImportDirective',
    ['absolutePath',
     'file',
     'id',
     'nameLocation',
     'nodeType',
     'scope',
     'sourceUnit',
     'src',
     'symbolAliases',
     'unitAlias'],
)

IndexAccess = namedtuple(
    'IndexAccess',
    ['baseExpression',
     'id',
     'indexExpression',
     'isConstant',
     'isLValue',
     'isPure',
     'lValueRequested',
     'nodeType',
     'src',
     'typeDescriptions'],
)

InheritanceSpecifier = namedtuple(
    'InheritanceSpecifier',
    ['baseName', 'id', 'nodeType', 'src'],
)

InlineAssembly = namedtuple(
    'InlineAssembly',
    ['AST',
     'documentation',
     'evmVersion',
     'externalReferences',
     'id',
     'nodeType',
     'src'],
)

Literal = namedtuple(
    'Literal',
    ['hexValue',
     'id',
     'isConstant',
     'isLValue',
     'isPure',
     'kind',
     'lValueRequested',
     'nodeType',
     'src',
     'subdenomination',
     'typeDescriptions',
     'value'],
)

Mapping = namedtuple(
    'Mapping',
    ['id',
     'keyName',
     'keyNameLocation',
     'keyType',
     'nodeType',
     'src',
     'typeDescriptions',
     'valueName',
     'valueNameLocation',
     'valueType'],
)

MemberAccess = namedtuple(
    'MemberAccess',
    ['argumentTypes',
     'expression',
     'id',
     'isConstant',
     'isLValue',
     'isPure',
     'lValueRequested',
     'memberLocation',
     'memberName',
     'nodeType',
     'referencedDeclaration',
     'src',
     'typeDescriptions'],
)

ModifierDefinition = namedtuple(
    'ModifierDefinition',
    ['body',
     'documentation',
     'id',
     'name',
     'nameLocation',
     'nodeType',
     'parameters',
     'src',
     'virtual',
     'visibility'],
)

ModifierInvocation = namedtuple(
    'ModifierInvocation',
    ['arguments', 'id', 'kind', 'modifierName', 'nodeType', 'src'],
)

NewExpression = namedtuple(
    'NewExpression',
    ['argumentTypes',
     'id',
     'isConstant',
     'isLValue',
     'isPure',
     'lValueRequested',
     'nodeType',
     'src',
     'typeDescriptions',
     'typeName'],
)

OverrideSpecifier = namedtuple(
    'OverrideSpecifier',
    ['id', 'nodeType', 'overrides', 'src'],
)

ParameterList = namedtuple(
    'ParameterList',
    ['id', 'nodeType', 'parameters', 'src'],
)

PlaceholderStatement = namedtuple(
    'PlaceholderStatement',
    ['id', 'nodeType', 'src'],
)

PragmaDirective = namedtuple(
    'PragmaDirective',
    ['id', 'literals', 'nodeType', 'src'],
)

Return = namedtuple(
    'Return',
    ['expression', 'functionReturnParameters', 'id', 'nodeType', 'src'],
)

RevertStatement = namedtuple(
    'RevertStatement',
    ['errorCall', 'id', 'nodeType', 'src'],
)

SourceUnit = namedtuple(
    'SourceUnit',
    ['absolutePath',
     'exportedSymbols',
     'id',
     'license',
     'nodeType',
     'nodes',
     'src'],
)

StructDefinition = namedtuple(
    'StructDefinition',
    ['canonicalName',
     'documentation',
     'id',
     'members',
     'name',
     'nameLocation',
     'nodeType',
     'scope',
     'src',
     'visibility'],
)

StructuredDocumentation = namedtuple(
    'StructuredDocumentation',
    ['id', 'nodeType', 'src', 'text'],
)

TryCatchClause = namedtuple(
    'TryCatchClause',
    ['block',
     'errorName',
     'id',
     'nodeType',
     'parameters',
     'src'],
)

TryStatement = namedtuple(
    'TryStatement',
    ['clauses', 'externalCall', 'id', 'nodeType', 'src'],
)

TupleExpression = namedtuple(
    'TupleExpression',
    ['components',
     'id',
     'isConstant',
     'isInlineArray',
     'isLValue',
     'isPure',
     'lValueRequested',
     'nodeType',
     'src',
     'typeDescriptions'],
)

UnaryOperation = namedtuple(
    'UnaryOperation',
    ['id',
     'isConstant',
     'isLValue',
     'isPure',
     'lValueRequested',
     'nodeType',
     'operator',
     'prefix',
     'src',
     'subExpression',
     'typeDescriptions'],
)

UncheckedBlock = namedtuple(
    'UncheckedBlock',
    ['id', 'nodeType', 'src', 'statements'],
)

UserDefinedTypeName = namedtuple(
    'UserDefinedTypeName',
    ['id',
     'nodeType',
     'pathNode',
     'referencedDeclaration',
     'src',
     'typeDescriptions'],
)

UsingForDirective = namedtuple(
    'UsingForDirective',
    ['global_', 'id', 'libraryName', 'nodeType', 'src', 'typeName'],
)

VariableDeclaration = namedtuple(
    'VariableDeclaration',
    ['baseFunctions',
     'constant',
     'documentation',
     'functionSelector',
     'id',
     'indexed',
     'mutability',
     'name',
     'nameLocation',
     'nodeType',
     'overrides',
     'scope',
     'src',
     'stateVariable',
     'storageLocation',
     'typeDescriptions',
     'typeName',
     'value',
     'visibility'],
)

VariableDeclarationStatement = namedtuple(
    'VariableDeclarationStatement',
    ['assignments', 'declarations', 'id', 'initialValue', 'nodeType', 'src'],
)

WhileStatement = namedtuple(
    'WhileStatement',
    ['body', 'condition', 'id', 'nodeType', 'src'],
)

YulAssignment = namedtuple(
    'YulAssignment',
    ['nativeSrc', 'nodeType', 'src', 'value', 'variableNames'],
)

YulBlock = namedtuple(
    'YulBlock',
    ['nativeSrc', 'nodeType', 'src', 'statements'],
)

YulBreak = namedtuple(
    'YulBreak',
    ['nativeSrc', 'nodeType', 'src'],
)

YulExpressionStatement = namedtuple(
    'YulExpressionStatement',
    ['expression', 'nativeSrc', 'nodeType', 'src'],
)

YulForLoop = namedtuple(
    'YulForLoop',
    ['body', 'condition', 'nativeSrc', 'nodeType', 'post', 'pre', 'src'],
)

YulFunctionCall = namedtuple(
    'YulFunctionCall',
    ['arguments', 'functionName', 'nativeSrc', 'nodeType', 'src'],
)

YulFunctionDefinition = namedtuple(
    'YulFunctionDefinition',
    ['body', 'name', 'nativeSrc', 'nodeType', 'parameters', 'src'],
)

YulIdentifier = namedtuple(
    'YulIdentifier',
    ['name', 'nativeSrc', 'nodeType', 'src'],
)

YulIf = namedtuple(
    'YulIf',
    ['body', 'condition', 'nativeSrc', 'nodeType', 'src'],
)

YulLiteral = namedtuple(
    'YulLiteral',
    ['kind', 'nativeSrc', 'nodeType', 'src', 'type', 'value'],
)

YulTypedName = namedtuple(
    'YulTypedName',
    ['name', 'nativeSrc', 'nodeType', 'src', 'type'],
)

YulVariableDeclaration = namedtuple(
    'YulVariableDeclaration',
    ['nativeSrc', 'nodeType', 'src', 'value', 'variables'],
)
