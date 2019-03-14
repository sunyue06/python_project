import xlwt
import xlrd
import datetime

def local_net():
    file_name=input('请输入文件名:')
    workbook=xlrd.open_workbook('C:/Users/yue.sun/Desktop/自己/py/工作/%s'%file_name,'r')#打开excel表格
    sheet_name = workbook.sheet_names()[0]  # sheet名字
    sheet = workbook.sheet_by_name(sheet_name)
    #sheet=workbook.sheet_by_index(0)#sheet索引从0开始
    sheet=workbook.sheet_by_name(sheet_name)
    print(sheet.name,sheet.nrows,sheet.ncols)
    cols_provice=sheet.col_values(2)
    cols_city=sheet.col_values(3)
    cols_pro=sheet.col_values(4)
    aim_cols_provice=sheet.col_values(10)
    aim_cols_city=sheet.col_values(11)
    aim_cols_pro=sheet.col_values(12)
    num=0
    local=xlwt.Workbook(encoding='utf-8')
    worksheet1=local.add_sheet('非本省本网')
    try:
        for     provice,city,pro,aim_provice,aim_city,aim_pro in zip(cols_provice,cols_city,cols_pro,aim_cols_provice,aim_cols_city,aim_cols_pro):
            if provice==aim_provice and city==aim_city and pro==aim_pro:
                continue
            else:
                #print(provice,city,pro,aim_provice,aim_city,aim_pro)
                worksheet1.write(num, 0, label=pro)
                worksheet1.write(num, 1, label=provice)
                worksheet1.write(num, 2, label=city)
                worksheet1.write(num, 3, label=aim_pro)
                worksheet1.write(num, 4, label=aim_provice)
                worksheet1.write(num, 5, label=aim_city)
                num+=1
                local.save('非本省本网%s.xls'%datetime.datetime.now().strftime('%Y-%m-%d'))
        print('表格已导出，请前往脚本执行路径下查看')
    except Exception as reult:
        print('导出失败,异常为%s'%reult)

if __name__=='__main__':
    local_net()






