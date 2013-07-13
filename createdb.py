# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('news.db')
c = conn.cursor()

c.execute('''DROP TABLE fefe''')
c.execute('''DROP TABLE faz''')

c.execute('''CREATE TABLE fefe (uid text, title text, date int)''')
c.execute('''CREATE TABLE faz (uid text, title text, description text,''' +
'''pubDate text, date int)''')

conn.commit()
c.close()