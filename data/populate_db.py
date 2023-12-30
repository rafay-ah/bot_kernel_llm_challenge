import sqlite3
from faker import Faker

conn = sqlite3.connect('agent_db.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE trades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symbol TEXT,
        quantity INTEGER,
        price REAL,
        trade_date TEXT,
        trader_name TEXT,
        trade_type TEXT
    )
''')


fake = Faker()
for _ in range(30):
    cursor.execute('''
        INSERT INTO trades (symbol, quantity, price, trade_date, trader_name, trade_type)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        fake.word(),
        fake.random_int(min=1, max=100),
        fake.random_int(min=1, max=1000),
        fake.date_this_decade(),
        fake.name(),
        fake.word()
    ))

conn.commit()
conn.close()
