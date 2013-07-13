# -*- coding: utf-8 -*-
import urllib.request
req = urllib.request.urlopen('http://blog.fefe.de/rss.xml')
print(req.read().decode('utf-8'))
