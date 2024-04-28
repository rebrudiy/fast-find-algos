from parsetolist import databases
from hash_table_imple import HashTable

hash_table = []

for i in databases:
    head = HashTable(len(i))
    for j in range(len(i)):
        if j == 0:
            head.insert(i[j].name, i[j])
    hash_table.append(head)


