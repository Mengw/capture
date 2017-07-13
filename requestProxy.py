# -*- coding: UTF-8 -*-
import requests
import datetime
import time
import json
import types
import codecs
import sys ,io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

url = "http://data.wxb.com/rank"
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
myHeaders ={"User-Agent": user_agent, 'Referer':'http://data.wxb.com','Connection': 'keep-alive'}
proxies = { "http": "http://dev-proxy.oa.com:8080"}

s = requests.session()

response  = s.get(url, headers = myHeaders, proxies = proxies)
print(response.cookies)
print(response.content)

# 日期
now = datetime.datetime.now()
nowStr = now.strftime('%Y-%m-%d-%H-%M-%S')
csvFileName = nowStr + '_data.csv'
csvFile = open(csvFileName, 'w',encoding='utf-8')
csvFile.write(codecs.BOM_UTF8.decode("utf-8"))
# csvHeadStr = "push_total," + 'stat_time,' + 'index_scores,' + 'wx_alias,' + 'name,' + 'read_num_max,' + 'cate_rank' + 'top_read_num_avg,' \
#              + 'wx_origin_id,' + 'rank,' + 'fans_num_estimate,' + 'cate_id,' + 'avatar,' + 'avg_read_num,' + 'qrcode,' + 'articles_total,' \
#              + 'avg_like_num,' + 'top_like_num_avg,' + 'desc,' + '\n'
# csvHeadStr = 'avatar,'+'stat_time,'+'fans_num_estimate,'+'articles_total,'+'rank,'\
#     'top_read_num_avg,'+'top_like_num_avg,'+'avg_read_num,'+'qrcode,'+'index_scores,'+'wx_alias,'\
#     'push_total,'+'desc,'+'wx_origin_id,'+'cate_rank,'+'name,'+'avg_like_num,'+'read_num_max,'+'cate_id,\n'
# csvFile.write(csvHeadStr)
#7-11
# "http://data.wxb.com/rank/day/2017-07-12/-1?sort=index_scores+desc&page="
#7-12
#urldataPre = "http://data.wxb.com/rank/day/2017-07-12/-1?sort=index_scores+desc&page="
#6月榜单
urldataPre = "http://data.wxb.com/rank/month/2017-06/-1?sort=index_scores+desc&page="

pageNum =1
pageSize =20
headers1 ={"User-Agent": user_agent, 'Referer':'http://data.wxb.com/rank','Connection': 'keep-alive','X-Requested-With': 'XMLHttpRequest'}
count = 51
for pageNum in range(1,count):
    urldataAll = urldataPre+str(pageNum)+'&page_size='+str(pageSize)
    print (urldataAll)
    responseData = s.get(urldataAll, headers=headers1,proxies = proxies)
    dictDataByte = responseData.content
    print ('内容：%s, \n 类型：%s' % (responseData.content, type(dictDataByte)))
    dictData = json.loads(dictDataByte.decode('utf-8'))
    for key, value in dictData.items():
        print
        key, '对应的值', value
    wxArray = dictData['data']
    if pageNum == 1:
        csvHeadstrDict = wxArray[0]
        strTemp = ''
        for key, value in wxArray[0].items():
            strTemp += key
            strTemp += ','
        strTemp += '\n'
        csvFile.write(strTemp)
    for i in range(len(wxArray)):
        print ("第", i, "个", wxArray[i])
        print (type(wxArray[i]))
        for key, value in wxArray[i].items():
            print(wxArray[i][key])
            if isinstance(wxArray[i][key], int):
                csvFile.write(str(wxArray[i][key]))
            elif isinstance(wxArray[i][key], float):
                csvFile.write(str(wxArray[i][key]))
            else:
                print(type(wxArray[i][key]))
                csvFile.write(wxArray[i][key])
            csvFile.write(',')
        csvFile.write('\n')
    # 停止三秒钟
    time.sleep(3)







