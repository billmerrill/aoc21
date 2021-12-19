'''

to add
X + Y = [X,Y]


to reduce take the first action

1. if 1 or more pairs are depth 4, Explode left most pair
2. if any regular number is >= 10, Split left most regular num

To explode a pair:
    if reg num to left exists, add pair[0] 
    if reg num to righ exists, add pair[1] 
    pair is replaced with 0

[[[[[9,8],1],2],3],4]
    [[[[0,9],2],3],4 ]


to split a number X
X -> [floor(X/2), ceil(X/2)],

'''
import ast
from math import floor, ceil
from binarytree import Node

class ParentNode(Node):
    def __init__(self, *args, parent=None, **kwargs):
        super().__init__(*args, **kwargs)       # Initialize the super class
        self.parent = parent

def load(input, node):
    if isinstance(input, list):
        node.left = load(input[0], ParentNode(-1, parent=node))
        node.right = load(input[1], ParentNode(-1, parent=node))
    else:
        node.value  = input
    return node

def explode(tree):
    explode_root = tree.levels[5][0].parent
    cur = explode_root

    left_target = None
    cur = cur.parent
    while cur:
        if (cur.left and 
            explode_root not in cur.left.postorder and
            len(cur.left.leaves)> 0):
            # left_target = cur.left.leaves[0]
            left_target = cur.left.inorder[-1]
            break
        cur = cur.parent

    if left_target:
        left_target.value += explode_root.left.value

    cur = explode_root
    right_target = None
    cur = cur.parent
    while cur:
        if (cur.right and 
            explode_root not in cur.right.postorder and
            len(cur.right.leaves)> 0):
            # right_target = cur.right.leaves[0]
            right_target = cur.right.inorder[0]
            break
        cur = cur.parent

    if right_target:
        right_target.value += explode_root.right.value

    explode_root.value = 0
    explode_root.left = None
    explode_root.right = None

def split(tree):
    target = None
    for node in tree.inorder:
        if node.value > 9:
            target = node
            break
    if target:
        target.left = ParentNode(floor(target.value / 2), parent=target)
        target.right = ParentNode(ceil(target.value / 2), parent=target)
        target.value = -1
    else:
        print('whoops')
    


def reduce(tree, verbose=False):
    reduce_again = True
    if verbose:
        tree.pprint()
    while reduce_again:
        reduce_again = False
        if tree.max_leaf_depth >= 5:
            if verbose:
                print('explode')
            explode(tree)
            reduce_again = True
        elif len([x.value for x in tree.leaves if x.value > 9]):
            if verbose:
                print('split')
            split(tree)
            reduce_again = True
        if verbose:
            tree.pprint()
    

def add(tree_a, tree_b):
    sum = ParentNode(-1)
    sum.left = tree_a
    tree_a.parent = sum
    sum.right = tree_b
    tree_b.parent = sum
    return sum

def sum_file(fname):
    lines = []
    with open(fname, 'r') as fh:
        lines = fh.readlines()

    sum = ParentNode(-1)
    load(ast.literal_eval(lines.pop(0).strip()), sum)
    while(lines):
        righthand = ParentNode(-1)
        load(ast.literal_eval(lines.pop(0).strip()), righthand)
        sum = add(sum, righthand)
        print(sum.inorder)
        reduce(sum, verbose=True)
        print('finished reduce vvvv')
        sum.pprint()
        print('finished reduce ^^^^^')

    # sum.pprint()

sum_file('/Users/bill/fun/aoc21/18/ex.txt')
# sum_file('/Users/bill/fun/aoc21/18/exa.txt')
# sum_file('/Users/bill/fun/aoc21/18/exb.txt')
# sum_file('/Users/bill/fun/aoc21/18/exc.txt')
# sum_file('/Users/bill/fun/aoc21/18/exd.txt')

def main():
    input = [[[[0,9],2],3],4]
    root = ParentNode(-1)   
    load(input, root)
    
def test():
    # input = [[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]    
    input = [[[[[13, 3], 4], 4], [7, [[8, 4], 19]]], [1, 1]]    
    root = ParentNode(-1)   
    load(input, root)
    root.pprint()
    reduce(root, verbose=True)
    # explode(root)
    # split(root)
    # root.pprint()
    # explode(root)
    # split(root)
    # root.pprint()

def ex1():
    ina = [[[[4,3],4],4],[7,[[8,4],9]]]
    inb = [1,1]
    tree_a = ParentNode(-1)
    load(ina, tree_a)
    tree_b = ParentNode(-1)
    load(inb, tree_b)
    sum = add(tree_a, tree_b)
    reduce(sum, verbose=True)
    sum.pprint()

