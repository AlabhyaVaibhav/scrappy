# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 10:35:59 2017

@author: Alabhya
"""
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen # py3k
import re
from bs4 import BeautifulSoup # $ pip install beautifulsoup4
STORE_LIST = []
html = urlopen("YOUR_URL_HERE")
bsObj =	BeautifulSoup(html)
YOUR_LIST_OF_OBJECTS = bsObj.findAll("HTML_TAG",{"class":"CLASS_NAME"}) 
for object in YOUR_LIST_OF_OBJECTS:
	STORE_LIST.append(re.sub('\s+','',name.get_text()))
print(STORE_LIST)
