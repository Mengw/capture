# -*- coding: UTF-8 -*-
import urllib2
import cookielib
import time
import json
import datetime
import codecs
import types
import sys

#微小宝的公众号地址，我发现他的page页面都是可以点击的，所以用程序把模拟这些点击 全部数据目前先存入到csv的文件中
# 第一次只写了最简单的
reload(sys)
sys.setdefaultencoding('UTF-8')




url = "http://data.wxb.com/rank"
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
headers ={"User-Agent": user_agent, 'Referer':'http://data.wxb.com','Connection': 'keep-alive'}
request = urllib2.Request(url,None,headers)
# response = urllib2.urlopen(request)
# print response.read()

# 这个访问查不到数据，显示 访问受限,联系管理员;刷新页面重试;错误码:5，感觉是因为cook的原因
# url = "http://data.wxb.com/rank/day/2017-07-11/-1?sort=index_scores+desc&page=1&page_size=20"
# request1 = urllib2.Request(url,None,headers)
# response = urllib2.urlopen(request1)
# print response.read()

# #声明一个Cookie对象实例保存cookie
# cookie = cookielib.CookieJar()
# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler=urllib2.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener = urllib2.build_opener(handler)
# #此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open(request)
# for item in cookie:
#     print 'Name = '+item.name
#     print 'Value = '+item.value

# #设置保存cookie的文件，同级目录下的cookie.txt
# filename = 'cookie.txt'
# #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = cookielib.MozillaCookieJar(filename)
# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib2.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener = urllib2.build_opener(handler)
# #创建一个请求，原理同urllib2的urlopen
# response = opener.open(request)
# #保存cookie到文件
# cookie.save(ignore_discard=True, ignore_expires=True)



filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)



result = opener.open(request)
#保存cookie到cookie.txt中

cookie.save(ignore_discard=True, ignore_expires=True)
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value
urldataPre = "http://data.wxb.com/rank/day/2017-07-11/-1?sort=index_scores+desc&page="
pageNum =1
pageSize =20
headers1 ={"User-Agent": user_agent, 'Referer':'http://data.wxb.com/rank','Connection': 'keep-alive','X-Requested-With': 'XMLHttpRequest'}

# 日期
now = datetime.datetime.now()
nowStr = now.strftime('%Y-%m-%d-%H-%M-%S')
csvFileName = nowStr+'_data.cvs'
csvFile = open(csvFileName, 'w')
csvHeadStr ="push_total,"+'stat_time,'+'index_scores,'+'wx_alias,'+'name,'+'read_num_max,'+'cate_rank'+'top_read_num_avg,'\
+'wx_origin_id,'+'rank,'+'fans_num_estimate,'+'cate_id,'+'avatar,'+'avg_read_num,'+'qrcode,'+'articles_total,'\
+'avg_like_num,'+'top_like_num_avg,'+'desc,'+'\n'
csvFile.write(csvHeadStr)
# 网站有50页
for pageNum in range(1,3):
    urldataAll = urldataPre+str(pageNum)+'&page_size='+str(pageSize)
    print urldataAll
    requestData = urllib2.Request(urldataAll, headers=headers1)
    result = opener.open(requestData)
    jsonResult = result.read()
    print jsonResult
    dictData = json.loads(jsonResult)
    for key, value in dictData.items():
             print key, '对应的值', value
    wxArray = dictData['data']
    for i in range(len(wxArray)):
        print  "第",i,"个",wxArray[i]
        print  type(wxArray[i])
        for key,value in wxArray[i].items():
            keyUff8 = key.encode('utf-8')
            print '转义后的key', keyUff8
            print '当前的值', wxArray[i][keyUff8],type(wxArray[i][keyUff8])
            # 字符串需要转义
            if type(wxArray[i][keyUff8]) is types.UnicodeType:
                csvFile.write(wxArray[i][keyUff8].encode("utf-8"))
            else:
                csvFile.write(str(wxArray[i][keyUff8]))
            csvFile.write(',')
        csvFile.write('\n')
    #停止三秒钟
    time.sleep(3)


