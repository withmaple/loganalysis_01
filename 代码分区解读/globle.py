from log.excel import readExcel
import os.path

#  --- 测试路径 ---
phonepath = 'sdcard/Android/data/'
# phonepath = 'storage/emulated/0/Android/data/'
# apk及log路径
filePath = 'C:/Users/mobif/Desktop/phoneLogAnalysis/'
# 预置资源路径
#keywordfile = 'C:/Users/mobif/Desktop/phoneLogAnalysis/profile/keywordexcel/GMPKeywords.xls'
#sfgpath = 'C:/Users/mobif/Desktop/phoneLogAnalysis/profile/sfg'
keywordfile = filePath + 'profile/keywordexcel/GMPKeywords.xls'
sfgpath = filePath + 'profile/sfg'
# 输出路径
#outputpath = 'C:/Users/mobif/Desktop/phoneLogAnalysis/out/'
outputpath = filePath + 'out/'
# 临时文件路径
#pkgnamepath = 'C:/Users/mobif/Desktop/phoneLogAnalysis/temp/pkgname.txt'
#outxlstemp = 'C:/Users/mobif/Desktop/phoneLogAnalysis/temp/outtemp.xls'
pkgnamepath = filePath + 'temp/pkgname.txt'
outxlstemp = filePath + 'temp/outtemp.xls'


CASE_NUMBER = 0 # 用例编号
CASE_ITEM = 1   # 用例名称
CASE_keyword1 = 2  # 关键词1
CASE_keyword2 = 3    # 关键词2
CASE_jsonkey = 4   # json关键词
CASE_compkey = 5 # 比较关键词
CASE_compresult = 6    # 比较结果
CASE_keywordout = 7 # 关键词搜索结果
CASE_jsonout1 = 8    # json搜索结果

row_num = readExcel(keywordfile).getRows
col_num = readExcel(keywordfile).getCol

class CASE:
    number = readExcel(keywordfile).getName(CASE_NUMBER)
    item = readExcel(keywordfile).getName(CASE_ITEM)
    keyword1 = readExcel(keywordfile).getName(CASE_keyword1)
    keyword2 = readExcel(keywordfile).getName(CASE_keyword2)
    jsonkey = readExcel(keywordfile).getName(CASE_jsonkey)
    compkey = readExcel(keywordfile).getName(CASE_compkey)
    compresult = readExcel(keywordfile).getName(CASE_compresult)
    keywordout = readExcel(keywordfile).getName(CASE_keywordout)
    jsonout1 = readExcel(keywordfile).getName(CASE_jsonout1)

#print(CASE.keyword1)

#  --- 获取指定目录下的所有指定后缀的文件名---
def getFileName(filePath):
    f_list = os.listdir(filePath)
    logname = []
    logfile = []
    outputfile = []
    flag = 0
    for i in f_list:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] == '.log':
            logfile.append(filePath + i)
            outputfile.append(filePath + 'out/' + i)
            # logname.append(os.path.splitext(i)[0])
            logname.append(i)
            flag = flag + 1
    return logfile, outputfile, logname, flag

#  --- 获取apk包名 ---
def getPKGName(filePath):
    f_list = os.listdir(filePath)
    pkgname = ''
    for i in f_list:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] == '.apk':
            pkgname = os.path.splitext(i)[0]
            print('当前处理的包名为：' + pkgname)
            break
    with open(pkgnamepath, 'w') as f_pkg:
        f_pkg.write(pkgname)
    return pkgname

