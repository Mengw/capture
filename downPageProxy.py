# -*- coding: UTF-8 -*-
# 此代码在2.7.10试用
import urllib2
import cookielib
import time
import json
import datetime
import codecs
import types
import sys


reload(sys)
sys.setdefaultencoding('UTF-8')

url = "http://data.wxb.com/rank"
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
headers ={"User-Agent": user_agent, 'Referer':'http://data.wxb.com','Connection': 'keep-alive'}
request = urllib2.Request(url,None,headers)


filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)


proxy_handler = urllib2.ProxyHandler({'http': 'dev-proxy.oa.com:8080'})
opener = urllib2.build_opener(proxy_handler)

result = opener.open(request)
print result.read()
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)



for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value
urldataPre = "http://data.wxb.com/rank/day/2017-07-11/-1?sort=index_scores+desc&page="
pageNum =1
pageSize =20
headers1 ={"User-Agent": user_agent, 'Referer':'http://data.wxb.com/rank','Connection': 'keep-alive','X-Requested-With': 'XMLHttpRequest'}
for pageNum in range(1,3):
    urldataAll = urldataPre+str(pageNum)+'&page_size='+str(pageSize)
    print urldataAll
    requestData = urllib2.Request(urldataAll, headers=headers1)
    result = opener.open(requestData)
    print result.read()