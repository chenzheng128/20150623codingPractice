#!//anaconda/bin/python
# -*- coding: utf-8 -*-

#REF: Python 2.7 Web Scraping 101 with Python03 Mar 2013
#REF: Easy and Practical Web scraping in Python http://arunrocks.com/easy-practical-web-scraping-in-python/
#
"""
Python2 Documentation: https://docs.python.org/2/
xpath: http://www.w3school.com.cn/xpath/xpath_syntax.asp
"""

#import urllib.request
import urllib
#from beautifulsoup4 import BeautifulSoup
#from bs4 import BeautifulSoup
#REF: http://www.crummy.com/software/BeautifulSoup/bs4/doc/
from lxml import etree
#http://lxml.de/tutorial.html#the-elementtree-class

import os
import os.path

req='http://rss.cnn.com/services/podcasting/studentnews/rss.xml'

f = urllib.urlopen(req)
e = etree.XML(f.read())
remotefile= e.xpath("//guid")[0].text
filename=remotefile.split("/")[-1]
localpath=u"/Users/chen/百度云同步盘/ESLyun/"
localfile=localpath + filename
print localfile

if os.path.isfile(localfile):
	print "File %s already downloaded.." % localfile
else:
	mycmd= "wget -P " + localpath.encode("utf-8") + " " + remotefile
	print mycmd
	os.system(mycmd)


