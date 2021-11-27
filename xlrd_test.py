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


'''
# 获取单选题数组
single_array = get_execl_data("D:/Test/single.xls")
# 获取多选题数组
multiple_array = get_execl_data("D:/Test/multiple.xls")
# 获取判断题数组
judge_array = get_execl_data("D:/Test/judge.xls")

text0 = ["生产安全预警系统的任何一个环节如果失去了（），预警就失去了意义。",
         "根据《生产安全事故应急预案管理办法》，某城市轨道交通运营企业，应当在应急案公布之日起（）日内，按照分级属地原则，向县级以上人民政府应急管理部门和其他负有安全生产监督管理职责的部门进行备案。",
         "依据《突发事件应对法》的规定，下列关于突发事件的应急处置与救援的说法，正确的是（）。",
         "某气瓶充装单位擅自转移被执法机关查封的气瓶，情节严重，其充装许可证于2018年6月30日被依法吊销。根据《特种设备安全法》，特种设备安全监督管理部门不予受理该单位新的许可申请的截止时间为（）。",
         "甲公司是一家五星级酒店，为解决蒸汽不足的问题，从乙公司购进一台蒸发量为4t/h的燃气锅炉。依据《特种设备安全监察条例》，下列关于该锅炉安全管理要求的说法中，正确的是（）。"
         ]
text1 = ["《安全生产法》规定，负有安全生产监督管理部门和其他负有安全生产监督管理的部门依法对生产经营单位的安全生产情况进行监督检查时，可以行职权有（）。",
         "依据《安全生产法》，安全生产监督管理部门和其他负有安全生产监督管理职责的部门可以对违法（）危险物品的作业场所予以查封，并依法作出处理决定。",
         "加强安全生产立法，制定《安全生产法》的必要性，主要体现在（）。",
         "依据《安全生产法》，两个以上生产经营单位在同一作业区域内进行可能危及对方安全生产的生产经营活动，未签订安全生产管理协议，以下处罚恰当的是（）。",
         "应急预案编制完成后,生产经营单位应按法律法规有关规定组织评审或论证,参加应急预案评审的人员可包括有关安全生产及应急管理方面的、有现场处置经验的专家。下列属于应急预案评审内容的是（）。"]
# text3 = "《安全生产法》规定，负有安全生产监督管理部门和其他负有安全生产监督管理的部门依法对生产经营单位的安全生产情况进行监督检查时，可以行职权有（）。"
text2 =["应急救援过程中，应急救援人员应在事故地区的主要交通要道、路口设安全检查站，控制抢险救援的车辆通行。",
        "可以预警的自然灾害，事故灾难和公共卫生事故预警级别，分为一级、二级、三级、四级，四级为最高级别",
        "工业园区、开发区等产业聚集区域内的生产经营单位，可以联合建立应急救援队伍。",
        "制定《安全生产法》最重要的目的是制裁各种安全生产违法犯罪行为。",
        "为安全生产提供技术、管理服务的中介机构必须是依法组建成立的，具备国家规定的资质总件。对其出具的安全评价、认证、检测、检验结果的准确性、公正性负法律责任。"
        ]


for i in range(5):
    match_answer("单选题", text0[i], i+1, single_array,  multiple_array, judge_array)
for i in range(5):
    match_answer("多选题", text1[i], i+1, single_array,  multiple_array, judge_array)
for i in range(5):
    match_answer("判断题", text2[i], i+1, single_array,  multiple_array, judge_array)
    
'''
'''
rows = len(array)

text = "在生产过程中，人们经常利用安全监控系统监测与安全有关的状态参数，发现故障、异常，及时采取措施控制，使这些参数不达到危险水平，消除故障、异常，以防止事故发生，然而安全监控系统本身也可能发生故障从而变得不可靠。安全监控系统可能发生两种类型的故障，即漏报和误报，下列说法属于漏报的是（ ）。"
for i in range(rows):
    if array[i][0] == text:
        print(f'{text} 的答案是： \n{array[i][1]}')

'''