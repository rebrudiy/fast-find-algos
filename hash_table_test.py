from parsetolist import databases
from hash_table_imple import HashTable
import random
import timeit

table = 0
keyer = 0

def find():
    table.search(keyer)


hash_table = []
lengths = []
for i in databases:
    lengths.append(len(i))
    head = HashTable(1000000)
    for j in range(len(i)):
        head.insert(i[j].name, i[j])
    hash_table.append(head)

hash_table_search_time = []

for i in hash_table:
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
    hash_table_search_time.append(_sum)

coll_count = []
for i in hash_table:
    coll_count.append(i.collisioncount)