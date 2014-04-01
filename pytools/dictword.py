#!/usr/bin/python
#coding:utf-8
#author:zsc347
#create on:2013-8-28

import urllib2
import re
import sys

def get_url(word):
	prefix="http://www.iciba.com/"
	return prefix+word

def get_content(url):
	return urllib2.urlopen(url).read()

def get_css_class(css_class,content):
	#patt=r"<.*\s+class=\"%s\"[^>]*>([^<]*)</[^>]*>" % css_class
	#patt=r"<.*\s+class=\"%s\"[^>]*>" % css_class
	print patt
	return re.search(patt,content).group()

def get_meaning(content):
	patt=r"<div class=\"group_pos\">(.*?)</div>"
	meaning=re.search(patt,content,re.S).group(1)
	meaning=re.sub('\s','',meaning)
	meaning=re.sub('</p>','\n',meaning)
	meaning=re.sub('</strong>','\t',meaning)
	meaning=re.sub('<[^>]*>','',meaning)
	return '\n'+ meaning


if __name__=="__main__":
	def main():
		if len(sys.argv) <2:
			print "input error!"
			return -1
		word=sys.argv[1]
		url=get_url(word)
		content=get_content(url)
		need=get_meaning(content)
		print need
	main()
