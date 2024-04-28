from parsetolist import databases
from red_black_tree_imple import RBTree
import random
import timeit

table = 0
keyer = 0


def find():
    table.exists(keyer)


rbtrees = []

for i in databases:
    head = RBTree()
    for j in i:
        head.insert(j)
    rbtrees.append(head)

rb_tree_time = []

for i in rbtrees:
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
    rb_tree_time.append(_sum)
print(rb_tree_time)


