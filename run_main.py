# -*- coding: utf-8 -*-
import unittest
from module.login import AccoutLogin
from module.openapi import OpenApi

class TestAll(unittest.TestCase):
    @unittest.skip("")
    def test_01_login(self):
        '''执行登陆操作'''
        accountlogin = AccoutLogin()
        response_result = accountlogin.login()
        accountlogin.bf_access_token()
        try:
            self.assertEqual(response_result,"success","登陆接口断言正确")
        except:
            raise
    def test_02_chat_openapi(self):
        chat_openapi = OpenApi()
        chat_openapi.run_openapi()

if __name__ == "__main__":
    unittest.main(verbosity=2)
