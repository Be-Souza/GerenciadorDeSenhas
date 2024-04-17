import sqlite3

conn = sqlite3.connect('PassMngr.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS SENHAS_SITES (
    id INTEGER PRIMARY KEY,
    site TEXT NOT NULL,
    usuario TEXT NOT NULL,
    senha TEXT NOT NULL
)
''')

conn.commit()

conn.close()
