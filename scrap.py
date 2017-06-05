# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 10:35:59 2017

@author: Alabhya
"""
from bs4 import BeautifulSoup
import urllib2 
def scrappy(link,class_name):
	url = urllib2.urlopen(link)
	content = url.read()
	soup = BeautifulSoup(content).find('div',class_=class_name).get_text()
	print soup

scrappy("https://www.edujinn.com/teacher-search?category_id=3&batch_city=2",'listview')