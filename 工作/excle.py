#/usr/bin/python
#coding=utf-8

import xlwt
workbook=xlwt.Workbook(encoding='utf-8')
worksheet=workbook.add_sheet('My Worksheet')
worksheet.write(1,1,label='this is test')
workbook.save('test.xls')