#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:05:12 2019

@author: nephilim
"""

import requests
import lxml
import time
import hashlib
import datetime

NowDate=datetime.datetime.now()
NowDateString=NowDate.strftime('%Y-%m-%d')
m = hashlib.md5()
m.update(NowDateString.encode("utf8"))
passcode=m.hexdigest()

serial_number=input('请输入激活码：\n')
# if serial_number==passcode:
if True:
    print('成功！')
    session=requests.Session()
    # username=input('请输入学号：\n')
    # password=input('请输入门户密码：\n')
    username='195001029'
    password='dante2016'
    headers={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Cache-Control':'no-cache',
            'Connection':'keep-alive',
            'Content-Length':'48',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'ca.its.csu.edu.cn',
            'Pragma':'no-cache',
            'Referer':'http://ca.its.csu.edu.cn/Home/Login/23',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'	
            }
    login_url='http://ca.its.csu.edu.cn/Home/Login/23'
    data={
         'userName':username,
         'passWord':password,
         'enter':'true'
         }
    req=session.post(url=login_url,headers=headers,data=data)
    html=lxml.etree.HTML(req.text)

    contents=html.xpath('//input/@value')
    tokenId=contents[0]
    account=contents[1]
    Thirdsys=contents[2]
    url='http://202.197.71.93/exam_login_tyrz.php'
    headers['Content-Length']='80'
    headers['Host']='202.197.71.93'
    headers['Referer']='http://ca.its.csu.edu.cn/SysInfo/SsoService/23'
    data={
         'tokenId':tokenId,
         'account':account,
         'Thirdsys':Thirdsys
         }
    req=session.post(url=url,headers=headers,data=data)

    url='http://202.197.71.93/index.php'
    del headers['Content-Length']
    del headers['Content-Type']
    headers['Host']='202.197.71.93'
    headers['Referer']='http://202.197.71.93/exam_login_tyrz.php'
    req=session.get(url=url,headers=headers)
    
    url='http://202.197.71.93/redir.php?catalog_id=121'
    headers['Host']='202.197.71.93'
    del headers['Referer']
    
    req=session.get(url=url,headers=headers)

    url='http://202.197.71.93/exam_xuexi_online.php'
    headers['Accept']='*/*'
    headers['Connection']='47'
    headers['Content-Type']='application/x-www-form-urlencoded; charset=UTF-8'
    headers['Host']='202.197.71.93'
    headers['Referer']='http://202.197.71.93/redir.php?catalog_id=121&object_id=2737'
    del headers['Upgrade-Insecure-Requests']
    headers['X-Requested-With']='XMLHttpRequest'
    data={
         'cmd':'xuexi_online'
         }
    while True:
        req=session.post(url=url,headers=headers,data=data)
        req.encoding = 'utf-8'
        print(req.json())
        time.sleep(1)
    # req=session.post(url=url,headers=headers,data=data)
    # req.encoding = 'utf-8'
    # print(req.json())
# NowDate=datetime.datetime.now()
# NowDateString=NowDate.strftime('%Y-%m-%d')
# delta = datetime.timedelta(days=1)
# NextDate=NowDate+delta
# NextDateString=NextDate.strftime('%Y-%m-%d')