from parsetolist import databases
from binarytreeimple import BSTNode
from products import Product

binarytrees = []
for i in databases:
    head = BSTNode(Product("does not exist", "neverland", -1, -1))
    for j in range(len(i)):
        if j == 0:
            head.insert(i[j])
    binarytrees.append(head)
