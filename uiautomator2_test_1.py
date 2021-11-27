import uiautomator2 as u2
from xlrd_test import get_execl_data

# 匹配题库，寻找并输出答案
def match_answer(question_type, question, i, single_array,  multiple_array, judge_array):
    if question_type == "单选题":
        # 循环遍历匹配单选题题库
        for j in range(len(single_array)):
            if single_array[j][0] == question:
                # 输出匹配到的题目 和 答案
                print(f'{i}.{single_array[j][0]}')
                print(f'答案：{single_array[j][1]}')
                break
            else:
                print(f'{i}.没有答案')

    elif question_type == "多选题":
        # 循环遍历匹配多选题题库
        for j in range(len(multiple_array)):
            if multiple_array[j][0] == question:
                # 输出匹配到的题目 和 答案
                print(f'{i}.{multiple_array[j][0]}')
                print(f'答案：{multiple_array[j][1]}')
                break
            else:
                print(f'{i}.没有答案')

    elif question_type == "判断题":
        # 循环遍历匹配多选题题库
        for j in range(len(judge_array)):
            if judge_array[j][0] == question:
                # 输出匹配到的题目 和 答案
                print(f'{i}.{judge_array[j][0]}')
                print(f'答案：{judge_array[j][1]}')
                break
            else:
                print(f'{i}.没有答案')

# 连接手机
device = u2.connect("f1986ad8")

# device = u2.connect_wifi("172.0.0.1:7912")
# print(device.device_info)

# 获取正在运行的APP包名
# print(device.current_app())

# 启动APP
# device.app_start("com.aky.yal")
# 打开应用
# device(text="QQ").click()

# device.xpath('//*[@content-desc="应安联"]/android.widget.ImageView[1]').click()
# device(resourceId="function1").click()
# device(text="“应安联杯”新安法知识竞赛-全员参与赛").click()

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

for i in range(20):

    # 获取题目类型
    question_type = device.xpath('//*[@text="subpackages/ying-school-exam/pages/ExamDetail/ExamDetail[9]"]/android.view.View[1]').get_text()
    # 获取题目
    question = device.xpath('//*[@text="subpackages/ying-school-exam/pages/ExamDetail/ExamDetail[21]"]/android.view.View[11]/android.view.View[1]/android.view.View').get_text()

    # 输出爬取到的题目类型和题目
    print(f'{i}.({question_type})')
    # 输出题目
    print(f'{i}.{question}')

    # 判断题目类型
    if question_type == "单选题":
        match_answer(question_type, question, i, single_array,  multiple_array, judge_array)
        # 单选下一题
        device.xpath('//*[@text="subpackages/ying-school-exam/pages/ExamDetail/ExamDetail[21]"]/android.view.View[17]/android.view.View[2]').click()
    if question_type == "多选题":
        match_answer(question_type, question, i, single_array,  multiple_array, judge_array)
        # 多选，下一题
        device.xpath('//*[@text="subpackages/ying-school-exam/pages/ExamDetail/ExamDetail[21]"]/android.view.View[18]/android.view.View[2]').click()
    if question_type == "判断题":
        match_answer(question_type, question, i,single_array,  multiple_array, judge_array)
        # 判断，点击下一题
        device.xpath('//*[@text="subpackages/ying-school-exam/pages/ExamDetail/ExamDetail[21]"]/android.view.View[14]/android.view.View[2]').click()





'''
2
危害和整改难度较大，应当全部或者局部停产停业，并经过一定时间整改治理方能排除的隐患是（）。


3
依据《安全生产法》的规定，当企业发生生产安全事故时，企业有关人员的正确做法应该是（）。


4
《安全生产法》对企业的主要负责人和安全生产管理人员的职责进行了进一步的明确，以下属于企业主要负责人职责的是（）。


5
根据《安全生产法》的规定，国有企业的主要负责人未按有关规定保证安全生产所需的资金投入，导致发生生产安全事故尚不够刑事处罚的对企业主要负责人应当给予（）的处分。


6
根据《企业安全生产费用提取和使用管理办法》，安全生产费用提取以上年度实际营业收入为计提依据，采取超额累退方式按照以下标准平均逐月提取：


7
规范生产安全事故应急预案管理工作，是提高预案质量、科学开展应急救援工作的重要举措。根据《生产安全事故应急预案管理办法》，关于企业应急预案论证或评审的说法，正确的是（）。


8
根据《生产安全事故应急预案管理办法》，以下不属于应急预案评审时应注重的要素是（）。


9
根据《生产安全事故应急预案管理办法》，以下不属于应急预案评审时应注重的要素是（）。


10
承包商管理是企业安全生产管理的重要组成部分。在承包队伍进入作业现场前，应接受消防安全、设备设施保护及社会治安方面的教育，组织教育的责任主体是（）。


11
根据《安全生产法》，生产经营单位的从业人员，其安全生产权利包括（）。


12
《企业安全生产标准化基本规范》（GB/T33000）对承包商管理提出了具体要求,主要有（）。


13
习近平主持召开中央全面深化改革委员会时强调,既要立足当前,科学精准打赢疫情防控阻击战,更要放眼长远,总结经验、吸取教训,针对这次疫情暴露出来的短板和不足,抓紧补短板、堵漏洞、强弱项,（）,完善重大疫情防控体制机制,健全国家公共卫生应急管理体系。


14
处理矿井火灾事故时,应遵循的基本技术原则有（）。


15
为了规范安全生产责任保险工作,强化事故预防,切实保障投保的生产经营单位及有关人员的合法权益,保险机构应当建立生产安全事故预防服务制度,协助投保的生产经营单位开展相关工作。依据《安全生产责任保险实施办法》,应开展的工作包括（）。


16
安全监管有关部门的监督检查人员依法履行事故隐患监督检查职责时，生产经营单位应当积极配合，不得拒绝和阻挠。


17
生产经营单位与从业人员订立的劳动合同，应当载明有关保障从业人员劳动安全，防止职业危害的事项。


18
矿山井下特种设备，必须按照国家有关规定，由专业生产单位生产，并经具有专业资质的检测、检验机构检测、检验合格，取得安全使用证或者安全标志，方可投入使用。


19
承担安全评价、认证、检测，检验工作的机构，出具虚假证明的，给他人造成损害的，与生产经营单位承担连带赔偿责任；构成犯罪的，依照刑法有关规定追究刑事责任。


20
安全生产费用在成本中据实列支。

Process finished with exit code 0
'''