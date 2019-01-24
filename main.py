#!/usr/bin/env python3
"""
This is a prefix tree (https://en.wikipedia.org/wiki/Trie), I think. I was 
planning on doing a Huffman tree, but then realized that this is a prefix tree.
I don't know if the terminology is correct, and I am pretty sure that there
are bugs (that I am yet to discover, so if you find one contact me).
I want to make an implemantation of the Huffman coding, so I can compress 
some files. Gus Frehse 10/12/2018
"""

class Node:
    dependencies = []
    frequency = 0
    name = "unnamed"
    totalDepen = 0

    def __init__(self, depen, frequ, nam, totalDepe):
        self.frequency = frequ
        self.dependencies = depen
        self.totalDepen = totalDepe
        self.name = nam

    def printTreeFormat(self, tabs, binaryCode):
    # Print in a fancy tree format
        print("    " * tabs + binaryCode +  " " + self.name + " " + str(self.frequency))
        for i in range(len(self.dependencies)):
            self.dependencies[i].printTreeFormat(tabs + 1, binaryCode + str(i))

def getNodeFrequency(node):
    # Method so I can sort based on the frequency
    return node.frequency

def concatenateNodes(nodesList, nodes):
    print("concatenating {} ({}) and {} ({})".format(nodes[0].name, nodes[0].frequency, nodes[1].name, nodes[0].frequency))
    # Create a node that is the combinations of those with least frequency
    n = Node(nodes, nodes[0].frequency + nodes[1].frequency, nodes[0].name + nodes[1].name, nodes[0].totalDepen + nodes[0].totalDepen)
    # Remove the nodes that were concatenated
    for node in nodes:
        nodesList.remove(node)
    # Add the new node to the list
    nodesList.append(n)

def printNodeNames(nodeList):
    # Just an easier way to print the names instead of some cryptic thing
    print("[", end="")
    for node in nodeList:
        print(node.name, end=" ")
    print("]")

#### Data

import sys
if len(sys.argv) != 2:
    print("USAGE: main.py <file>")
    sys.exit(1)

nodes = []
# File input
with open(sys.argv[1], "r") as f:
    for line in f:
        (frequency, name) = line.split()
        nodes.append(Node([], float(frequency), name, 0))

while len(nodes) > 1:
    # Print
    printNodeNames(nodes)

    # Sort, so I can get the two smallest frequencies
    nodes.sort(key=getNodeFrequency)
    # Concatenate the two least frequent
    concatenateNodes(nodes, [nodes[0],nodes[1]])

for i in range(len(nodes)):
    nodes[i].printTreeFormat(0, "")

