# -*- coding: utf-8 -*-
# @File    : openapi.py
from base.send_mail import sendMail
from base.readexcel import ReadExcel
from config.request_url import RequestUrl
from base.replace_data import ReplaceData
from config.request_data import RequestData
from base.writeexcel import WriteToExcel
from base.request_method import RequestMethod
from base.operation_response import OperationResponse

class OpenApi(object):
    def __init__(self):
        self.url = RequestUrl.openapi_url
        replace_data = ReplaceData()
        self.requestdata = RequestData()
        self.request_data = self.requestdata.openapi_request_data
        self.header =replace_data.replace_openapi_header()
        self.openapi_dialogue_data_path = self.requestdata.openapi_dialogue_data_path
        self.Save_Result = []
        self.readexcel = ReadExcel(self.openapi_dialogue_data_path)
        self.request_method = RequestMethod()
        self.replace_data = ReplaceData()


    def run_openapi(self):
        Total_Data = self.readexcel.Read_Total_Data()

        for row in range(len(Total_Data)):
            '''获取每行index的数值'''
            row_value = Total_Data[row]
            row_index = row_value[0]

            # 获取标准问题
            value = row_value[1]
            print ("Question",value)
            # 替换对话数据
            opera_dialogue = OperationResponse(value)
            response_answer = opera_dialogue.get_response_value()
            response_module = opera_dialogue.get_response_module()
            response_source = opera_dialogue.get_response_source()
            response_intent = opera_dialogue.get_response_intent()
            response_emotion = opera_dialogue.get_response_emotion()

            if row_index == 0:
               # 标准问题
                excel_answer = row_value[3]    # 从excel中读取answer
                '''进行判断'''
                if response_module == "faq" and excel_answer == response_answer:
                    row_value.append("Pass")
                    self.Save_Result.append(row_value)
                else:
                    row_value.append("Fail")
                    row_value.append(response_answer)           # 写入正确的答案
                    self.Save_Result.append(row_value)
            elif row_index == 1:
                # Function 技能
                excel_source = row_value[2]  # 从excel中读取answer'
                '''进行判断'''
                if response_source == excel_source:
                    row_value.append("Pass")
                    self.Save_Result.append(row_value)
                else:
                    row_value.append("Fail")
                    row_value.append(response_answer)
                    self.Save_Result.append(row_value)
            elif row_index == 2:
                '''机器人形象'''
                excel_answer = row_value[2]
                '''进行判断'''
                if response_module == "chat" and response_source == "robot_custom" and response_answer == excel_answer:
                    row_value.append("Pass")
                    self.Save_Result.append(row_value)
                else:
                    row_value.append("Fail")
                    row_value.append(response_answer)
                    self.Save_Result.append(row_value)
                pass
            elif row_index == 3:
                '''意图触发TDE'''
                excel_answer = row_value[3]
                '''进行判断'''
                if response_module == "task_engine" and excel_answer == response_answer:
                    row_value.append("Pass")
                    self.Save_Result.append(row_value)
                else:
                    row_value.append("Fail")
                    row_value.append(response_answer)
                    self.Save_Result.append(row_value)
            elif row_index == 4:
                '''指令配置'''
                excel_answer1 = row_value[3]
                excel_model = row_value[2]
                '''进行判断'''
                if excel_answer1 == response_answer and response_module == excel_model:
                    row_value.append("Pass")
                    self.Save_Result.append(row_value)
                else:
                    row_value.append("Fail")
                    row_value.append(response_answer)
                    self.Save_Result.append(row_value)
            elif row_index == 5:
                '''敏感词出话测试'''
                excel_answer = row_value[3]
                excel_model = row_value[2]

                '''进行判断'''
                if response_answer == excel_answer and response_module == excel_model:
                    row_value.append("Pass")
                    self.Save_Result.append(row_value)
                else:
                    row_value.append("Fail")
                    row_value.append(response_answer)
                    self.Save_Result.append(row_value)
            elif row_index == 6:
                '''知识图谱'''
                excel_answer = row_value[2]
                excel_model = row_value[3]

                '''进行判断'''
                if response_answer == excel_answer and response_module == excel_model:
                    row_value.append("Pass")
                    self.Save_Result.append(row_value)
                else:
                    row_value.append("Fail")
                    row_value.append(response_answer)
                    self.Save_Result.append(row_value)
            elif row_index == 7:
                '''意图引擎'''
                excel_intent = row_value[2]
                '''进行判断'''
                if response_intent == excel_intent:
                    row_value.append("Pass")
                    self.Save_Result.append(row_value)
                else:
                    row_value.append("Fail")
                    row_value.append(response_intent)
                    self.Save_Result.append(row_value)
            elif row_index == 8:
                '''第三方闲聊'''
                excel_answer = row_value[2]
                excel_module = row_value[3]

                '''进行判断'''
                if response_module == excel_module and excel_answer == response_answer:
                    row_value.append("Pass")
                    self.Save_Result.append(row_value)
                else:
                    row_value.append("Fail")
                    row_value.append(response_answer)
                    self.Save_Result.append(row_value)
            elif row_index == 9:
                '''同义词转换'''
                excel_answer = row_value[3]
                excel_module = row_value[2]

                '''进行判断'''
                if response_module == excel_module and excel_answer == response_answer:
                    row_value.append("Pass")
                    self.Save_Result.append(row_value)
                else:
                    row_value.append("Fail")
                    row_value.append(response_answer)
                    self.Save_Result.append(row_value)
            elif row_index == 10:
                '''情绪话术'''
                '''从excel中读取answer'''
                excel_emotion = row_value[2]

                '''进行判断'''
                if response_emotion == excel_emotion:
                    row_value.append("Pass")
                    self.Save_Result.append(row_value)
                else:
                    row_value.append("Fail")
                    row_value.append(response_emotion)
                    self.Save_Result.append(row_value)
            elif row_index == 11:
                '''chat 闲聊'''
                if response_module == "chat":
                    row_value.append("Pass")
                    self.Save_Result.append(row_value)
                else:
                    row_value.append("Fail")
                    row_value.append(response_answer)
                    self.Save_Result.append(row_value)
            elif row_index == 12:
                '''Ner 解析器'''
                excel_answer = row_value[2]
                if response_module == "task_engine" and response_answer == excel_answer:
                    row_value.append("Pass")
                    self.Save_Result.append(row_value)
                else:
                    row_value.append("Fail")
                    row_value.append(response_answer)
                    self.Save_Result.append(row_value)
            elif row_index == 13:
                '''Custom_Skill 技能开发'''
                excel_answer = row_value[2]
                if response_module == "custom_skill" and response_answer == excel_answer:
                    row_value.append("Pass")
                    self.Save_Result.append(row_value)
                else:
                    row_value.append("Fail")
                    row_value.append(response_answer)
                    self.Save_Result.append(row_value)
            elif row_index == 14:
                '''Chat_Story聊天小故事'''
                excel_answer = row_value[2]
                if response_module == "chat_story" and response_answer == excel_answer:
                    row_value.append("Pass")
                    self.Save_Result.append(row_value)
                else:
                    row_value.append("Fail")
                    row_value.append(response_answer)
                    self.Save_Result.append(row_value)
            elif row_index == 15:
                '''To_Human转人工'''
                excel_answer = row_value[2]
                if response_answer == excel_answer and response_module == "to_human":
                    row_value.append('Pass')
                    self.Save_Result.append(row_value)
                else:
                    row_value.append('Fail')
                    row_value.append(response_answer)
                    self.Save_Result.append(row_value)

        #将测试结果写入到excel中
        write = WriteToExcel(self.Save_Result,self.requestdata.openapi_dialogue_data_result_path)
        write.write_result_to_excel()

        # 发送邮件
        sendMail()



if __name__ == "__main__":
    run_openapi = OpenApi()
    run_openapi.run_openapi()
