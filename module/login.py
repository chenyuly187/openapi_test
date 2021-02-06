# -*- coding: utf-8 -*-
# @File    : login.py
import json

from base.request_method import RequestMethod
from base.replace_data import ReplaceData
from config.request_data import RequestData
from config.request_header import RequestHeader
from config.request_url import RequestUrl


class AccoutLogin(object):
    def __init__(self):
        self.url = RequestUrl.login_url
        self.request_data = RequestData.login_request_data
        self.requestmethod = RequestMethod()
        self.replace_token = ReplaceData()

    def login(self):
        '''res 杩斿洖璇锋眰缁撴灉'''
        res = None
        res = self.requestmethod.run_main("POST",self.url,self.request_data)
        res_json = json.loads(res)          # 杞崲涓哄瓧鍏告牸寮�
        response_token = res_json["result"]["token"]
        '''join_token操作'''
        RequestData.token = self.replace_token.join_token(response_token)
        RequestData.enterprise = res_json["result"]["info"]["enterprise"]
        RequestData.userid = res_json["result"]["info"]["id"]
        ret_msg = res_json["ret_msg"]       # 鎺ュ彛鎴愬姛杩斿洖淇℃伅

        return ret_msg

    def bf_access_token(self):
        bf_access_token = None
        header = RequestHeader.header
        header['Authorization']=RequestData.token
        res = self.requestmethod.run_main("GET",RequestUrl.bf_access_token_url,self.request_data, header=header)
        res_json = json.loads(res)
        if res_json['status'] == 0:
            bf_access_token = res_json["result"]
            RequestData.bf_access_token=bf_access_token
            RequestData.access_token=bf_access_token

        return bf_access_token

