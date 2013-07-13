# -*- coding: utf-8 -*-
import urllib.request
import xml.etree.ElementTree as ET
import sqlite3
import datetime

req = urllib.request.urlopen('http://blog.fefe.de/rss.xml')
#print(req.read().decode('utf-8'))
tree = ET.parse(req)
root = tree.getroot()
conn = sqlite3.connect('news.db')
c = conn.cursor()

vorher = c.execute('''SELECT count(uid) FROM fefe''').fetchone()[0]

for child in root[0].findall('item'):
    #print(child[0].text, child[1].text)

    if not c.execute("select uid from fefe where uid=:id",
         {"id": child[1].text}).fetchone():
        c.execute('insert into fefe values (?,?,?)', (child[1].text,
         child[0].text, datetime.datetime.today()))
conn.commit()

nachher = c.execute('''SELECT count(uid) FROM fefe''').fetchone()[0]

print('Anzahl neuer Elemente: ' + str(nachher - vorher))

c.close()

