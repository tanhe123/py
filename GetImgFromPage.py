# -*- coding: utf-8 -*-

import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    print "打开网页成功...."
    html = page.read()
    print "读取网页成功...."
    return html

def getImg(url):
    html = getHtml(url);
    reg = r'src="(http://.{0,300}?(?:\.jpg|\.gif|\.jpeg|\.png))"'
    imgre = re.compile(reg)
    print "正则表达式编译成功..."
    imglist = imgre.findall(html)
    print "正在查找网页中的图片..."
    x = 0
    for imgurl in imglist:
        print '正在下载',imgurl
        if imgurl[-2] == 'p':
            urllib.urlretrieve(imgurl, '%s.jpg' % x)
        elif imgurl[-2] == 'i':
            urllib.urlretrieve(imgurl, '%s.gif' % x)
        elif imgurl[-2] == 'e':
            urllib.urlretrieve(imgurl, '%s.jpeg' % x)
        elif imgurl[-2] == 'n':
            urllib.urlretrieve(imgurl, '%s.png' % x)
        x += 1
        
html = raw_input("请输入想要下载的网址:\n")

if html.find("http:") == -1:
    html = "http://" + html



print '准备获取'+html+'中的图片'

getImg(html)
