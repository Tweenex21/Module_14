import sqlite3

connection = sqlite3.connect("not_telegram.db")

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance TEXT NOT NULL
)
''')


users_data = [
    ("User1", "example@gmail.com", 10, 1000),
    ("User2", "example@gmail.com", 20, 1000),
    ("User3", "example@gmail.com", 30, 1000),
    ("User4", "example@gmail.com", 40, 1000),
    ("User5", "example@gmail.com", 50, 1000),
    ("User6", "example@gmail.com", 60, 1000),
    ("User7", "example@gmail.com", 70, 1000),
    ("User8", "example@gmail.com", 80, 1000),
    ("User9", "example@gmail.com", 90, 1000),
    ("User10", "example@gmail.com", 100, 1000)
]

cursor.executemany("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", users_data)

cursor.execute("UPDATE Users SET balance = balance -500 WHERE id % 2 = 1")

cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
results = cursor.fetchall()
for username, email, age, balance in results:
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

connection.commit()
connection.close()