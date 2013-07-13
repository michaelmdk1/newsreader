# -*- coding: utf-8 -*-
import urllib.request
import xml.etree.ElementTree as ET
import sqlite3
import time

def main():
    req = urllib.request.urlopen('http://www.faz.net/rss/aktuell/')
    #print(req.read().decode('utf-8'))
    tree = ET.parse(req)
    root = tree.getroot()
    conn = sqlite3.connect('news.db')
    c = conn.cursor()

    vorher = c.execute('''SELECT count(uid) FROM faz''').fetchone()[0]

    for child in root[0].findall('item'):
        #print(child[0].text, child[1].text)
        parse = child[1].text
        parselist = parse.split("<p>")
        parselist = parselist[1].split("</p>")
        #print(parselist[0])
        if not c.execute("select uid from faz where uid=:id",
             {"id": child[4].text}).fetchone():
            c.execute('insert into faz values (?,?,?,?,?)', (child[4].text,
             child[0].text, parselist[0], child[3].text, int(time.time())))
    conn.commit()

    nachher = c.execute('''SELECT count(uid) FROM faz''').fetchone()[0]

    print(('Anzahl neuer Elemente: ' + str(nachher - vorher)))

    c.close()

if __name__ == '__main__':
    main()