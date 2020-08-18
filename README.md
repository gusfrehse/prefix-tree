# prefix-tree
Implementation of a prefix tree in python 3
# Usage
`main.py <inputFile> <options>`

Where `<inputFile>` is a file containing the intial nodes, one each line, with the frequency and the name of the node.
Example of input file:
```
0.5 a
0.25 b
0.125 c
0.125 d
```
The sum of the probabilities should be `1.0`, although the application itself won't check for it.
The `<options>` are:
```
--pretty
--code
--verbose
```
When `--pretty` is used `--code` should not be used. `--pretty` makes the output more readable, in the format of nested statements. Each statement contains the corresponding Huffman Coding, name and frequency.

`--code` makes the output be the Huffman coding and the name.

`--verbose` can be used with both `--code` and `--pretty`. It makes the script print most steps made to the tree.
