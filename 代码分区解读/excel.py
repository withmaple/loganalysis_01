import xlrd
import os.path

#  --- 删除文件---
def delete_file(path='C:/Users/mobif/Desktop/LogAnalysis/out/out.xls'):
    if os.path.exists(path):
        os.remove(path)

#  --- 删除上一次测试数据---
def delete_file_folder(src):
    if os.path.exists(src):
        if os.path.isfile(src):
            try:
                os.remove(src)
            except:
                pass
        elif os.path.isdir(src):
            for item in os.listdir(src):
                itemsrc = os.path.join(src, item)
                delete_file_folder(itemsrc)
    else:
        os.makedirs(src)

#  --- 获取keywordfile数据 ---
def open_excel(keywordfile):
    try:
        data = xlrd.open_workbook(keywordfile, formatting_info=True)
        return data
    except Exception as e:
        print(e)

#  --- 根据索引获取Excel表格中的数据   参数:keywordfile：Excel文件路径    rownameindex：表头行名所在行的索引  ，by_index：表的索引 ---
def excel_table_byindex(keywordfile, rownameindex=0, by_index=0):
    data = open_excel(keywordfile)
    table = data.sheets()[by_index]
    rows = table.nrows  # 获取行数
    list = []
    for rownum in range(0, rows):
        row = table.row_values(rownum)
        list.append(row)
    return list

class readExcel(object):
    def __init__(self, path):
        self.path = path

    @property
    def getSheet(self):
        # 获取索引
        xl = xlrd.open_workbook(self.path)
        sheet = xl.sheet_by_index(0)
        return sheet

    @property
    def getRows(self):
        # 获取行数
        rows = self.getSheet.nrows
        return rows

    @property
    def getCol(self):
        # 获取列数
        col = self.getSheet.ncols
        return col

    # 以下是分别获取每一列的数值
    def getName(self, column_index):
        if column_index <= self.getCol:
            ColumnName = []
            for i in range(1, self.getRows):
                ColumnName.append(self.getSheet.cell_value(i, column_index))
            return ColumnName
        else:
            print("输入的column不合法！")
