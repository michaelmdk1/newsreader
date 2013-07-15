# -*- coding: utf-8 -*-

import sqlite3
import time


def printSlowly(text):
    for char in text:
        print(char, end='',flush=True)
        time.sleep(0.03)


def ausgabeItem(text, text2=False):
    printSlowly(text)
    if text2:
        print()
        printSlowly(text2)


def main():
    conn = sqlite3.connect('news.db')
    c = conn.cursor()

    c.execute('''SELECT title FROM fefe ORDER BY date DESC''')

    liste = c.fetchall()

    for row in liste:
        #print((row[0]))
        ausgabeItem(row[0])
        print('\n', flush=True)
        time.sleep(10)

    c.execute('''SELECT title, description FROM faz ORDER BY date DESC''')
    liste = c.fetchall()

    for row in liste:
        #print((row[0]))
        ausgabeItem(row[0], row[1])
        print('\n', flush=True)
        time.sleep(10)


if __name__ == '__main__':
    main()