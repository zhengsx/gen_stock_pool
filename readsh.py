import json
import urllib.request
import requests
import csv
import xml.dom.minidom
import sys
import time
from subprocess import call

def sayit():
    ## var hq_str_s_sh000001="上证指数,3094.668,-128.073,-3.97,436653,5458126";
    link_sina_shanghai = '''http://hq.sinajs.cn/list=s_sh000001'''

    wp = urllib.request.urlopen(link_sina_shanghai)
    data = wp.read().decode("gbk")

    start_pos = data.index('=')
    end_pos = data.index(';')
    j_data = data[start_pos + 1:end_pos - 1]
    ##remove "
    xx = j_data.strip('"')
    print(xx)

    yy=xx.split(",",6)
    ##上证指数,3033.9251,12.1739,0.40,1161979,11325518
    str1 = "\"" +yy[0]+str(round(float(yy[1]),0)) +"涨幅" + str(round(float(yy[3]),2)) +"成交额" + str(round(int(yy[5])/10000,0)) + "亿" + "\""
    call(['say-it',str1])
    ##for x in yy:
     ##   call(['say', x])

while True:
    sayit()
    time.sleep(12)
