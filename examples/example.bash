#!/bin/bash

# Run from the main directory:
#
# cd mermaider
# ./example/example.bash

solc example/Example.sol --combined-json ast >/tmp/artifacts.json
python main.py /tmp/artifacts.json
