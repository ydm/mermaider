# Mermaider

Generates [Mermaid](https://mermaid.js.org]) 
[class diagrams](https://mermaid.js.org/syntax/classDiagram.html)
for smart contracts written in [Solidity](https://soliditylang.org/).

### Example

```mermaid
classDiagram
class `Hello` {
    +uint256 world
    +Mermaider()
```

### Usage

```
solc                                                                 \
  /home/someone/path/to/my/Contract.sol                              \
  @openzeppelin=/home/someone/path/to/my/node_modules/\@openzeppelin \
  --combined-json ast >/tmp/artifacts.json

git clone git@github.com:ydm/mermaider.git
cd mermaider
python main.py </tmp/artifacts.json
```

### Install optional dependencies

If `eth-hash` is installed, function signatures (as displayed in the
diagram) will be additionally hashed and checked against the compiled
function selectors.

```
python -m venv env
source env/bin/activate
python -m pip install --upgrade pip
python -m pip install eth-hash[pycryptodome]
python main.py
```
