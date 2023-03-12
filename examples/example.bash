#!/bin/bash

# Run from the main directory:
#
# cd mermaider
# ./examples/example.bash

solc816 examples/Example.sol --combined-json ast >/tmp/artifacts.json
python main.py /tmp/artifacts.json
