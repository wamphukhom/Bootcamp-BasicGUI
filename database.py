import sqlite3

conn = sqlite3.connect('product_database.sqlite3')
c = conn.cursor()

#Create Table
c.execute("""CREATE TABLE IF NOT EXISTS INV (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                tid TEXT,
                stamp TEXT,
                product TEXT,
                price REAL,
                quan REAL,
                total REAL)""")

print('success')

def insert_INV(data):
    # data= {'tid':'123445', 'stamp':'2021-12-12 10:20:59'...}
    ID = None
    tid = data['tid']
    stamp = data['stamp']
    product = data['product']
    price = data['price']
    quan = data['quan']
    total = data['total']

    with conn:
        command = 'INSERT INTO INV VALUES (?,?,?,?,?,?,?)'
        c.execute(command,(ID,tid,stamp,product,price,quan,total))
        conn.commit()
    print('inserted!')

def view_INV():
    with conn:
        c.execute("SELECT * FROM INV")
        data = c.fetchall()
        print(data)

INV = {'tid':'213123',
        'stamp':'2020-12-12 11:11:11',
        'product':'ทุเรียน',
        'price':100,
        'quan':20,
        'total':5000}

insert_INV(INV)