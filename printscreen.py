# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('news.db')
c = conn.cursor()

c.execute('''SELECT title FROM fefe ORDER BY date DESC''')

liste = c.fetchall()
for row in liste:
    print(row[0])
    print()