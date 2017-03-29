# -*- coding: utf-8 -*-
import stat
import urllib2
import os
import re
def loadurl(url):
    try:
        conn = urllib2.urlopen(url,timeout=5)
        html = conn.read()
        return html
    except urllib2.URLError:
        return ''
    except Exception:
        print("unkown exception in conn.read()")
        return ''

def download(url,filename):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }
        req = urllib2.Request(url=url, headers=headers)
        conn = urllib2.urlopen(requ,timeout=5)
        f = open(filename,'wb')
        f.write(conn.read())
        f.close()
        return True
    except urllib2.URLError:
        print 'load',url,'error'
        return False
    except Exception:
        print("unkown exception in conn.read()")
        return ''

def save_pic(url,path):
    searchname = '.*/(.*?.jpg)'
    name = re.findall(searchname,url)
    filename = path +'/'+ name[0]

    print filename + ':start'

    tryTimes = 3

    while tryTimes != 0:
        tryTimes -= 1
        if os.path.exists(filename):
            print filename,' exists, skip'
            return True

        if download(url,filename):
            break

    if tryTimes != 0:
        print(filename + ": over")
    else:
        print(url + " ：Failed to download")

def pic_list(picList,path):
    picurl = ''
    for picurl in picList:
        save_pic(picurl,path)

def picurl(url,path):
    if os.path.exists(path):
        print path, 'exist'
    else:
        os.makedirs(path)
    html = ''
    while True:
        html = loadurl(url)
        if html == '':
            print 'load', url,'error'
            continue
        else:
            break
    rePicContent1 = '<div.*?id="picture.*?>.*?<p>(.*?)</p>'
    rePicContent2 = '<div.*?class="postContent.*?>.*?<p>(.*?)</p>'
    rePicList = '<img.*?src="(.*?)".*?>'
    picContent = re.findall(rePicContent1, html,re.S)
    if len(picContent) <=0:
        picContent = re.findall(rePicContent2, html,re.S)
    if len(picContent) <=0:
        print 'load false, over download this page and return'
        return False
    else:
        picList = re.findall(rePicList,picContent[0],re.S)
        pic_list(picList,path)

url = 'http://www.meizitu.com/a/454.html'
picurl(url,'/Users/Desgard_Duan/Desktop/')
