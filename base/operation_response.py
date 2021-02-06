# -*- coding: utf-8 -*-
import json
from base.replace_data import ReplaceData
from base.request_method import RequestMethod
from config.request_data import RequestData
from config.request_url import RequestUrl

class OperationResponse(object):
    def __init__(self,dialogue):
        self.dialogue = dialogue
        self.replace_data = ReplaceData()
        self.run_main = RequestMethod()
        self.header = self.replace_data.reaplace_openapi_header()
        self.url = RequestUrl.openapi_url
        # 获取response
        self.response = self.get_response()

    def replace_dialogue(self):
        '''替换对话内容'''
        dialogue = self.replace_data.replace_openapi_request_data(self.dialogue)

        return dialogue

    def get_response(self):
        try:
            response = self.run_main.run_main("POST",self.url,self.replace_dialogue(),self.header)
            return json.loads(response)
        except Exception as e:
            pass

    def get_response_value(self):
        '''获取响应值中的value值'''
        try:
            value = self.response["data"][0]["value"]
        except Exception as e:
            vlaue = "value 返回值为空"
        finally:
            return value

    def get_response_module(self):
        '''获取相应值中的module'''
        try:
            module = self.response["info"]["module"]
        except Exception as e:
            module = "module 返回值为空"
        finally:
            return module

    def get_response_source(self):
        '''获取相应值中的source'''
        try:
            source = self.response["info"]["source"]
        except Exception as e:
            source = "source 返回值为空"
        finally:
            return source

    def get_response_intent(self):
        '''获取相应值中的intent'''
        try:
            intent = self.response["info"]["intent"]
        except Exception as e:
            intent = 'intent 返回值为空'
        finally:
            return intent

    def get_response_emotion(self):
        '''获取响应中的emotibot'''
        try:
            emotion = self.response["info"]["emotion"]
        except Exception as e:
            emotion = "emotion 返回值为空"
        finally:
            return emotion
