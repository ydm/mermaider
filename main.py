#!/usr/bin/env python3

import json
from mermaider.visitor import to_mermaid


def main():
    artifacts = json.loads(input())
    to_mermaid(artifacts)


if __name__ == '__main__':
    main()
