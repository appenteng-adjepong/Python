import sqlite3

conn = sqlite3.connect("longlist.db")

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS books(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT NOT NULL,
               author TEXT NOT NULL,
               award TEXT NOT NULL,
               year INTEGER NOT NULL,
               longlisted BOOLEAN NOT NULL DEFAULT 1,
               shortlisted BOOLEAN DEFAULT 0,
               won BOOLEAN DEFAULT 0)
               """)

sample_books = [
    ("The Bee Sting", "Paul Murray", "Booker Price", 2023, 1, 1, 0),
    ("Western Lane", "Chetna Maroo", "Booker Prize", 2023, 1, 1, 0),
    ("Prophet Song", "Paul Lynch", "Booker Prize", 2023, 1, 1, 1),
    ("The Heaven & Earth Grocery Store", "James McBride", "National Book Award", 2023, 1, 1, 1),
    ("Chain-Gang All-Stars", "Nana Kwame Adjei-Brenyah", "National Book Award", 2023, 1, 1, 0),
]


cursor.executemany("""
INSERT INTO books (title, author, award, year, longlisted, shortlisted, won)
VALUES (?, ?, ?, ?, ?, ?, ?)""", sample_books)

conn.commit()
conn.close()

print("Database created and sample data inserted")