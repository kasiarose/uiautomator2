import xlrd
from match_test import match_answer

# 导入execl表格题库

def get_execl_data(execl_path):
    # 打开execl表格
    book = xlrd.open_workbook(execl_path)
    table_1 = book.sheet_by_index(0)  # 获取第一张表

    # 获取表的总行数
    rows = table_1.nrows
    # 定义存储execl的数组
    execl_array = [[0 for i in range(2)] for i in range(rows)]

    # print(f'行数：{rows}')
    # print(f'列数：{table_1.ncols}')
    # 获取所有行数据
    for rx in range(table_1.nrows):
        # 列
        for cy in range(2):
            # 获取execl的数据
            execl_array[rx][cy] = table_1.cell_value(rowx=rx, colx=cy)
    return execl_array
