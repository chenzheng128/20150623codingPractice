

#REF: Python 2.7 Web Scraping 101 with Python03 Mar 2013
#REF: Easy and Practical Web scraping in Python http://arunrocks.com/easy-practical-web-scraping-in-python/
#

import urllib.request
from bs4 import BeautifulSoup
#REF: http://www.crummy.com/software/BeautifulSoup/bs4/doc/

url='http://jw.cuc.edu.cn/home'
cssstr=".center_article_list a"

#url='http://news.cuc.edu.cn'
#cssstr="a"

req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html_doc = response.read()

#http://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors
soup = BeautifulSoup(html_doc)
for elem in soup.select(cssstr):
    print(elem.get_text(strip=True))
    #print(elem)
    #if elem.has_attr("href"):
    #print ("DEBUG:", elem.get("href"), "\n")


print ("\nINFO: elem functions")
print ("DEBUG:", type(elem))
print ("DEBUG:",dir(elem))
print ("DEBUG:",elem.prettify())
"""
<class 'bs4.element.Tag'>
['HTML_FORMATTERS', 'XML_FORMATTERS', '__bool__', '__call__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__unicode__', '__weakref__', '_all_strings', '_attr_value_as_string', '_attribute_checker', '_find_all', '_find_one', '_formatter_for_name', '_is_xml', '_lastRecursiveChild', '_last_descendant', '_select_debug', '_selector_combinators', '_should_pretty_print', '_tag_name_matches_and', 'append', 'attribselect_re', 'attrs', 'can_be_empty_element', 'childGenerator', 'children', 'clear', 'contents', 'decode', 'decode_contents', 'decompose', 'descendants', 'encode', 'encode_contents', 'extract', 'fetchNextSiblings', 'fetchParents', 'fetchPrevious', 'fetchPreviousSiblings', 'find', 'findAll', 'findAllNext', 'findAllPrevious', 'findChild', 'findChildren', 'findNext', 'findNextSibling', 'findNextSiblings', 'findParent', 'findParents', 'findPrevious', 'findPreviousSibling', 'findPreviousSiblings', 'find_all', 'find_all_next', 'find_all_previous', 'find_next', 'find_next_sibling', 'find_next_siblings', 'find_parent', 'find_parents', 'find_previous', 'find_previous_sibling', 'find_previous_siblings', 'format_string', 'get', 'getText', 'get_text', 'has_attr', 'has_key', 'hidden', 'index', 'insert', 'insert_after', 'insert_before', 'isSelfClosing', 'is_empty_element', 'name', 'namespace', 'next', 'nextGenerator', 'nextSibling', 'nextSiblingGenerator', 'next_element', 'next_elements', 'next_sibling', 'next_siblings', 'parent', 'parentGenerator', 'parents', 'parserClass', 'parser_class', 'prefix', 'prettify', 'previous', 'previousGenerator', 'previousSibling', 'previousSiblingGenerator', 'previous_element', 'previous_elements', 'previous_sibling', 'previous_siblings', 'recursiveChildGenerator', 'renderContents', 'replaceWith', 'replaceWithChildren', 'replace_with', 'replace_with_children', 'select', 'setup', 'string', 'strings', 'stripped_strings', 'tag_name_re', 'text', 'unwrap', 'wrap']
"""


#Signature: find_all(name, attrs, recursive, text, limit, **kwargs)
#print(soup.find_all("a"))

#Searching by CSS class
#print(soup.find_all("a", class_="center_article_list"))
#http://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class



