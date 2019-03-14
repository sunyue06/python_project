#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding=gbk

import os,json,xlwt
#key="'Authorization: CC95AC02F3D28EA2B848258BE87F88F8'"
#date="'Date:2018-12-07 10:20:00'"
#lei= "'Content-Type:json'"
#url= "'http://openapi.exclouds.com/contentService/QueryCacheIp?domain=www.csair.com&detail=Y'"
#url_api=str(os.system(input('请输入:')))
#print(type(url_api))
a=input('请输入字符串:')
jd=json.loads(a)
for i in jd:

    ziyuan=print('%s\t%s\t%s'%(i['ip'],i['isp'],i['pro']))

    #workbook = xlwt.Workbook(encoding='ascii')
    #sheet = workbook.add_sheet('逸云资源')
    #sheet.write(ziyuan)
    #workbook.save('逸云资源.xls')
#
