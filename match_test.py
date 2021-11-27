
# 匹配题库，寻找并输出答案
def match_answer(question_type, question, i, single_array,  multiple_array, judge_array):

    if question_type == "1":
        # 循环遍历匹配单选题题库
        # print("单选题")
        for j in range(len(single_array)):
            # print(single_array[j])
            if single_array[j][0] == question:

                # 输出匹配到的题目 和 答案
                print(f'{i+1}.{single_array[j][0]}')
                print(f'答案：{single_array[j][1]}\n')
                break
    elif question_type == "2":
        # print("多选题")
        # 循环遍历匹配多选题题库
        for j in range(len(multiple_array)):
            if multiple_array[j][0] == question:
                # 输出匹配到的题目 和 答案
                print(f'{i+1}.{multiple_array[j][0]}')
                print(f'答案：{multiple_array[j][1]}\n')
                break
    elif question_type == "3":
        # print("判断题")
        # 循环遍历匹配多选题题库
        for j in range(len(judge_array)):
            if judge_array[j][0] == question:
                # 输出匹配到的题目 和 答案
                print(f'{i+1}.{judge_array[j][0]}')
                print(f'答案：{judge_array[j][1]}\n')
                break


