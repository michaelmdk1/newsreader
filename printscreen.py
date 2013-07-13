# -*- coding: utf-8 -*-

import sqlite3
import time


def ausgabeEinItem(text):
    for char in text:
        print(char, end='',flush=True)
        time.sleep(0.001)


def main():
    conn = sqlite3.connect('news.db')
    c = conn.cursor()

    c.execute('''SELECT title FROM fefe ORDER BY date DESC''')

    liste = c.fetchall()

    for row in liste:
        #print((row[0]))
        ausgabeEinItem(row[0])
        print('\n', flush=True)
        time.sleep(5)

if __name__ == '__main__':
    main()


