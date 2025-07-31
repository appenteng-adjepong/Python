import sqlite3
import os


db_path = "longlist.db"
if os.path.exists(db_path):
    print(f"Database found: {db_path}")

    # connect and fetch records
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='books'")
    if cursor.fetchone():
        print("'books' table found. Fetching data...\n")

        cursor.execute("SELECT title, author, award, year, longlisted, shortlisted, won FROM books")
        rows = cursor.fetchall()
        for row in rows:
            title, author, award, year, longlisted, shortlisted, won = row
            print(f"{title} by {author} ({year}) | {award}")
            print(f" Longlisted: {bool(longlisted)}, Shortlisted: {bool(shortlisted)}, Won: {bool(won)}\n")
    else:
        print("'books' table does not exist in the database.")

    conn.close()

else:
    print(f"Database not found: {db_path}")