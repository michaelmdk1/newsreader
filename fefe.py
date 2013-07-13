# -*- coding: utf-8 -*-
import urllib.request
import xml.etree.ElementTree as ET

req = urllib.request.urlopen('http://blog.fefe.de/rss.xml')
#print(req.read().decode('utf-8'))
tree = ET.parse(req.read().decode('utf-8'))
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)