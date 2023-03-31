from collections import abc
from pprint import pformat


def gentypes(sources):
    '''
    Usage:

    $ solc /home/a/b/Something.sol                             \
           @openzeppelin=/home/a/b/node_modules/\@openzeppelin \
           >/tmp/artifacts.json

    import json
    from mermaider.utils import gentypes
    with open('/tmp/artifacts.json', 'r', encoding='utf-8') as f:
        artifacts = json.load(f)
    gentypes(artifacts['sources'])

    ## Then write the output to mermaider/types.py.
    '''
    top = {}
    def f(d):
        if not isinstance(d, abc.Mapping):
            return
        if node_type := d.get('nodeType'):
            top.setdefault(node_type, set())
            top[node_type].update(d.keys())
        for k, v in d.items():
            if isinstance(v, list):
                [f(x) for x in v]
            else:
                f(v)
    for x in sources.values():
        f(x['AST'])
    for k in sorted(top):
        params = pformat(
            sorted(top[k]),
            indent=5,
            width=75,
        ).replace('[    ', '[')
        print(f'{k} = namedtuple(')
        print(f"    '{k}',")
        print('    ', end='')
        print(params, end=',\n')
        print(')\n')
