import sqlite3
from products import Product

def parseDBtoList(databasename):
    connection = sqlite3.connect(databasename)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    unfinished_data = cursor.fetchall()
    data = []
    for i in unfinished_data:
        name = i[0]
        country = i[1]
        volume = i[2]
        price = i[3]
        pr = Product(name, country, volume, price)
        data.append(pr)
    return data


databases = []

for i in range(1, 8):
    DBname = 'databases/products'
    DBname += str(i) + '.db'
    databases.append(parseDBtoList(DBname))


