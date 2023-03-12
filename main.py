#!/usr/bin/env python3

import json
import sys
from mermaider.visitor import to_mermaid


def main():
    if len(sys.argv) >= 2:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            artifacts = json.load(f)
    else:
        artifacts = json.loads(input())
    to_mermaid(artifacts)


if __name__ == '__main__':
    main()
