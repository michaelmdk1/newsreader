# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('news.db')
c = conn.cursor()

c.execute('''CREATE TABLE fefe (uid text, title text, date text)''')

conn.commit()
c.close()