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
extractedBNList = []
extractedPNList = []
html = urlopen("https://www.sulekha.com/school-tuitions/kolkata")
bsObj =	BeautifulSoup(html)
phoneList = bsObj.findAll("span",{"class":"icon-phone"}) 
nameList = bsObj.findAll("div",{"class":"busi-name"})
for	name in	nameList:
	extractedBNList.append(re.sub('\s+','',name.get_text()))
for	name in	phoneList:
	extractedPNList.append(re.sub('\s+','',name.get_text()))
print(extractedBNList + extractedPNList)
