# -*- coding: UTF-8 -*-
import urllib2

#代理服务器
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : '127.0.0.1:1080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)