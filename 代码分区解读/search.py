import codecs
import time
from log.globle import *
import xlwt

rownum = readExcel(keywordfile).getRows
colnum = readExcel(keywordfile).getCol

#  --- 通过keyword1，keyword2搜索log，输出结果到文本 参数：item：测试项目名---
def search_keyword(logname, item, keyword1, keyword2=''):
    logfile = filePath + logname
    #cpoylogfile = outputpath + logname
    nowt = time.strftime("%Y%m%d", time.localtime())
    outputfile = filePath + 'out/' + nowt + '/' + 'filter_' + logname
    with codecs.open(logfile, 'r', 'utf8') as f_in, codecs.open(outputfile, 'a', 'utf8') as f_out:
        f_out.write('\n' + item + '\n')
        list = []
        for line in f_in:
            line = line.strip()
            if (keyword1 in line) and (keyword2 in line):
                f_out.write(line + '\n')
                list.append(line)
    return list

#  --- jsonkeyword搜索结果---
def jsonkeyword_out(logname, keyword1, jsonkey, keyword2=''):
    # outputfile=filePath+'out/'+filename
    outputfile = filePath + logname
    getWord = ''
    #getWord1 = ''
    # 开始标识
    startSign = '"' + jsonkey + '":'
    # 结束标识
    endSign1 = ','
    endSign2 = '}'
    endSign3 = ']'
    with codecs.open(outputfile, 'r', 'utf8') as file02:
        list = []
        for line in file02.readlines():
            # line = line.encode("utf8")
            line = line.strip()
            if (keyword1 in line) and (keyword2 in line):
                #  --- 判断开始标识是否存在于当前行中 ---
                if startSign in line:
                    #  --- 进行字符串的切割 ---
                    startIndex = line.index(startSign)
                    if startIndex >= 0:
                        startIndex += len(startSign)
                    getWord1 = line[startIndex:].strip()
                    if getWord1[0] == '[':
                        endIndex = getWord1.find(endSign3)
                    elif endSign1 in getWord1:
                        endIndex = getWord1.find(endSign1)
                    elif endSign2 in getWord1:
                        endIndex = getWord1.find(endSign2)
                    else:
                        endIndex = 0
                    getWord = getWord1[0:endIndex]
                    # 去掉空格,'',[,等符号
                    getWord = getWord.strip()
                    getWord = getWord.strip('[')
                    getWord = getWord.strip('"')
    return getWord

#  --- 设置单元格字体颜色---
def style_red():
    font0 = xlwt.Font()
    font0.colour_index = 2

    style0 = xlwt.XFStyle()
    style0.font = font0

    return style0

#  --- jsonout compare结果---
def compareout():
    for i in range(1, rownum-1):
        if CASE.compkey[i] :
            if CASE.compkey[i] == CASE.keywordout[i] :
                CASE.compresult[i] = 'T'
            else :
                CASE.compresult[i] = 'F'
    return CASE.compresult
