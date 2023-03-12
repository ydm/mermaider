from collections import abc
from mermaider import types


def type_string(root):
    return root.typeName.typeDescriptions['typeString']


def _instantiate(root):
    if node_type := root.get('nodeType'):
        cls = getattr(types, node_type)
        arg = {f: None for f in cls._fields}
        arg.update(root)
        if 'global' in arg:
            arg['global_'] = arg.pop('global')
        return cls(**arg)
    return root


def wrap(root):
    if isinstance(root, abc.Mapping):
        return _instantiate({k: wrap(v) for k, v in root.items()})
    elif isinstance(root, abc.MutableSequence):
        return [wrap(x) for x in root]
    else:
        return root
