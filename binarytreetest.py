from parsetolist import databases
from binarytreeimple import BSTNode
from products import Product
import random
import timeit

table = 0
keyer = 0


def find():
    table.exists(keyer)


binarytrees = []
for i in databases:
    head = BSTNode(Product("does not exist", "neverland", -1, -1))
    for j in range(len(i)):
        if j == 0:
            head.insert(i[j])
    binarytrees.append(head)

binary_search_tree_time = []

for i in binarytrees:
    count = 1000
    _sum = 0.0
    for j in range(count):
        table_column = random.randint(0, 6)
        table_row = random.randint(table_column, len(databases[table_column]) - 1)
        _key = databases[table_column][table_row].name
        table = i
        keyer = _key
        execution_time = timeit.timeit(find, number=1)
        _sum += execution_time
    binary_search_tree_time.append(_sum)

