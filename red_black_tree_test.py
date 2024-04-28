from parsetolist import databases
from red_black_tree_imple import RBTree

rbtrees = []

for i in databases:
    head = RBTree()
    for j in i:
        head.insert(j)
    rbtrees.append(head)
