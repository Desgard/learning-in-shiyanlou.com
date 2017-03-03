#!/usr/bin/env python
# encoding: utf-8

import urllib, urllib2, random
from time import localtime, strftime, time

#返回uri参数字典
def gen_uri_param():
    curID = '183859'
    submittype = '1'
    t = str(int(time()*1000))
    starttime = strftime("%Y/%m/%d %H:%M:%S", localtime())
    rn = '3065862882'
    return locals()

#返回submitdata字符串
#([(1,2),(2,4),(3,1)]) => '1$2}2$4}3$1'
def gen_post_string(answer):
    def concat_pair(pair):
        return '$'.join([str(pair[0]), str(pair[1])])
    
    tmp_list = []
    for x in answer:
        tmp_list.append(concat_pair(x))
    return '}'.join(tmp_list)


jq_base = "http://www.sojump.com/jq/{}.aspx"
uri_base = "http://www.sojump.com/handler/processjq.ashx?{}"

#answer是这种形式[(1,2),(2,1),(3,5)……]的答案列表，这里答案我是随机生成的。
answer = zip(range(1,11),[random.randint(1,4) for x in range(11)])

post_data = urllib.urlencode({'submitdata':gen_post_string(answer)})
get_data = urllib.urlencode(gen_uri_param())

request_url = uri_base.format(get_data)
request = urllib2.Request(request_url, post_data)
result = urllib2.urlopen(request)
print result.read()
