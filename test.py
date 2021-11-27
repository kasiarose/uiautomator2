import uiautomator2 as u2
from xlrd_test import get_execl_data

# 匹配题库，寻找并输出答案
def match_answer(question_type, question, i, single_array,  multiple_array, judge_array):
    if question_type == "1":
        # 循环遍历匹配单选题题库
        for j in range(len(single_array)):
            if single_array[j][0] == question:
                # 输出匹配到的题目 和 答案
                print(f'{single_array[j][0]}')
                print(f'答案：{single_array[j][1]}')
                break
    elif question_type == "2":
        # 循环遍历匹配多选题题库
        for j in range(len(multiple_array)):
            if multiple_array[j][0] == question:
                # 输出匹配到的题目 和 答案
                print(f'{multiple_array[j][0]}')
                print(f'答案：{multiple_array[j][1]}')
                break
    elif question_type == "3":
        # 循环遍历匹配多选题题库
        for j in range(len(judge_array)):
            if judge_array[j][0] == question:
                # 输出匹配到的题目 和 答案
                print(f'{judge_array[j][0]}')
                print(f'答案：{judge_array[j][1]}')
                break
# 连接手机
device = u2.connect("f1986ad8")


# 获取单选题数组
single_array = get_execl_data("D:/Test/single.xls")
# 获取多选题数组
multiple_array = get_execl_data("D:/Test/multiple.xls")
# 获取判断题数组
judge_array = get_execl_data("D:/Test/judge.xls")
# 获取文本

# 判断题
# device.xpath('//*[@text="subpackages/ying-school-exam/pages/ExamDetail/ExamDetail[9]"]/android.view.View[1]').get_text()
# device.xpath('//*[@resource-id="_root"]/android.view.View[1]/android.view.View[1]').get_text()
# device.xpath('//*[@text="subpackages/ying-school-exam/pages/ExamDetail/ExamDetail[9]"]/android.view.View[14]/android.view.View[2]/android.view.View[1]').click()

for i in range(30):

    # 获取题目类型
    # question_type = device.xpath('//*[@text="subpackages/ying-school-exam/pages/ExamDetail/ExamDetail[9]"]/android.view.View[1]').get_text()
    # question_type = device.xpath('//*[@text="subpackages/ying-school-exam/pages/ExamDetail/ExamDetail[27]"]//android.view.View[1]').get_text()
    # 获取题目
    question_type = input(f"第{i + 1}题类型：")
    question = device.xpath('//*[@resource-id="_root"]/android.view.View[1]/android.view.View[1]').get_text()
    # 输出爬取到的题目类型和题目
    # print(f'{i+1}.({question_type})')
    # 输出题目
    print(f'{question}')

    # 判断题目类型
    if question_type == "1":
        match_answer(question_type, question, i, single_array,  multiple_array, judge_array)
        # 单选下一题
        # device.xpath('//*[@text="subpackages/ying-school-exam/pages/ExamDetail/ExamDetail[21]"]/android.view.View[17]/android.view.View[2]').click()
    if question_type == "2":
        match_answer(question_type, question, i, single_array,  multiple_array, judge_array)
        # 多选，下一题
        # device.xpath('//*[@text="subpackages/ying-school-exam/pages/ExamDetail/ExamDetail[21]"]/android.view.View[18]/android.view.View[2]').click()
    if question_type == "3":
        match_answer(question_type, question, i,single_array,  multiple_array, judge_array)
        # 判断，点击下一题
        # device.xpath('//*[@text="subpackages/ying-school-exam/pages/ExamDetail/ExamDetail[21]"]/android.view.View[14]/android.view.View[2]').click()


