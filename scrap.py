# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 10:35:59 2017

@author: Alabhya
"""
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen # py3k

from bs4 import BeautifulSoup # $ pip install beautifulsoup4
html = 	urlopen("https://www.sulekha.com/school-tuitions/kolkata")
bsObj	=	BeautifulSoup(html)
nameList	=	bsObj.findAll("li",{"class":"list-item"}) 
for	name in	nameList:
	print(name.get_text())
