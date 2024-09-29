import sqlite3

def initiate_db():
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
        )
    ''')
    cursor.execute('DELETE FROM Products')
    connection.commit()
    cursor.execute('DELETE FROM SQLITE_SEQUENCE WHERE NAME="Products"')
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                       (f'Витамины №{i}', f'Описание витаминов №{i}', i * 150))
    connection.commit()
    connection.close()



def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    connection.close()
    return products

