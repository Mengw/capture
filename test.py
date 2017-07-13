# -*- coding: UTF-8 -*-

print('请点击下方➕关注，每个夜晚伴你夜听！')

u=u'unicode编码文字'
g=u.encode('gbk') #转换为gbk格式
print (g) #此时为乱码，因为当前环境为utf-8,gbk编码文字为乱码
str=g.decode('gbk').encode('utf-8')   #以gbk编码格式读取g（因为他就是gbk编码的）并转换为utf-8格式输出
print (str) #正常显示中文