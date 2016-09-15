#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Hugo
#   E-mail  :   nsirone@outlook.com
#   Date    :   16/09/15 22:37:58


import os
import urllib2

url = 'http://www.baidu.com'
request = urllib2.Request(url)
response = urllib2.urlopen(request)

print response.read()
