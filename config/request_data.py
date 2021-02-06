# -*- coding: utf-8 -*-
# @File    : request_data.py
import os
class RequestData(object):
    # 维护Appid
    appid = ''


    token = ''
    access_token = ''
    enterprise = ''
    bf_access_token = ''
    delete_bot_data = {}
    openapi_request_data = {
	"text": "人工客服",
	"customInfo":{
 			"性别":"女",
 			"平台":"微信"
	}
}
    userid = ''
    openapi_dialogue_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)) + '/Files/automatic_file.xlsx'
    openapi_dialogue_data_result_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)) + '/Files/general_result.xlsx'



