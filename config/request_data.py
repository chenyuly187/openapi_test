# -*- coding: utf-8 -*-
# @File    : request_data.py
import os
class RequestData(object):
    # 维护Appid
    appid = '06cb264f5655425cb2a08d641103b42b'


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
    userid = 'bb3e3925f0ad11e7bd860242ac120003'
    openapi_dialogue_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)) + '/Files/automatic_file.xlsx'
    openapi_dialogue_data_result_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)) + '/Files/general_result.xlsx'



