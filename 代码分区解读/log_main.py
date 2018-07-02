import logging
#from log.globle import *
from log.excel import *
from log.search import *
from xlutils.copy import copy
import os.path

def LogAnalysis():
    nowt = time.strftime("%Y%m%d", time.localtime())
    delete_file_folder(outputpath + nowt)
    print(outputpath + nowt + '中上次测试数据已删除')
    logfile, outputfile, logname, flag = getFileName(filePath)
    print(filePath + '文件夹中包含的log文件有%d个：' % flag)
    print(logname)

    for i in range(0, flag):
        name = str(logname[i])
        print('*****开始处理第%d个log：' % (i + 1) + name + '*****')
        try:
            out(keywordfile, name, nowt)
        except Exception as e:
            print(e)
            logging.exception(e)
            print('分析' + name + '失败')
        delete_file(outxlstemp)
        print(name + '处理完成')
        print('')

#  --- jsonkeyword搜索结果输入表格---
def out(keywordfile, logname, nowt):
    data = open_excel(keywordfile)
    datacopy = copy(data)
    tableout = datacopy.get_sheet(0)

    for i in range(1, rownum-1):
        search_keyword(logname, CASE.item[i], CASE.keyword1[i], CASE.keyword2[i])
    print('---keyword1、2搜索已完成---')
    for j in range(1, rownum-1):
        CASE.jsonout1[j] = jsonkeyword_out(logname, CASE.keyword1[j], CASE.jsonkey[j], CASE.keyword2[j])
        tableout.write(j, CASE_jsonout1, CASE.jsonout1[j])
    print('---json keyword搜索已完成---')
    compareout()
    for m in range(1, rownum-1):
        if CASE.compresult[m] == 'F' :
            tableout.write(m, CASE_compresult, CASE.compresult[m], style_red())
        else :
            tableout.write(m, CASE_compresult, CASE.compresult[m])
    print('---json数据对比已完成---')

    datacopy.save(outputpath + nowt + '/' + pkgname + '.xls')


if __name__ == "__main__":
    # 获取测试的apk包名
    pkgname = getPKGName(filePath)

    for num in range(0, 100):
        # 从手机中获取指定应用的log
        print('----从' + phonepath + pkgname + '/files/' + pkgname + '.log ' + '获取log' + '----')
        os.system('adb pull ' + phonepath + pkgname + '/files/' + pkgname + '.log ' + filePath)
        # 按规则分析log
        LogAnalysis()
        print('第%d轮处理完成' % num)
        print('----------------------------------------------------------------')
        input('按回车键再次从手机获取log')

    input('log刷新次数已达到最大，按回车键退出脚本')