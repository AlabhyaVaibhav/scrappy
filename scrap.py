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

url = "YOUR_URL_HERE"
soup = BeautifulSoup(urlopen(url))
print(soup.get_text())

'''Another code type'''
from	urllib.request	import	urlopen 
from	urllib.error	import	HTTPError 
from	bs4	import	BeautifulSoup	
def	getTitle(url):
	try:
		html	=	urlopen(url)
	except	HTTPError	as	e:
		return	None
	try:
		bsObj	=	BeautifulSoup(html.read())
		title	=	bsObj.body.h1
	except	AttributeError	as	e:
		return	None
	return	title
title	=	getTitle("http://www.pythonscraping.com/exercises/exercise1.html") 
if	title	==	None:
	print("Title	could	not	be	found")
else:
	print(title)