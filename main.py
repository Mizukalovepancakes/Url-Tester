#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys
import re
import urllib2
regex = r"^(http(s?))://(www\.)?([a-z]){2,}(\.)([a-zA-Z]){2,}"
if(len(sys.argv) != 2):
	print('Insert a url')
	sys.exit(1)
url = sys.argv[1].lower()
if(re.match(regex, url)):
	print('Format correct')
else:
	print('Format incorrect')
	sys.exit(1)
try:
	co = urllib2.build_opener()
	co.addheaders = [('User-Agent', 'Mozilla/5.0')]
	co.open(url)
	print('Website correct/on')
except:
	print('Website off/incorrect')
	sys.exit(1)

