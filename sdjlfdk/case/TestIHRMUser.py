import json
import unittest
from parameterized import parameterized
import requests
import logging

from sdjlfdk import app
from sdjlfdk.api.IHRM_api import GetApi
from sdjlfdk.app import Get_Path


def data_json():
    read_json = []
    with open(Get_Path +"/data/data_login.json",'r',encoding="utf-8") as f:
        data_cs = json.load(f)
        for data_zz in data_cs.values():
            ele = (data_zz.get("mobile"),
                   data_zz.get("password"),
                   data_zz.get("success"),
                   data_zz.get("code"),
                   data_zz.get("message")
                    )
            read_json.append(ele)


    return read_json
class TsetIhrmUsser(unittest.TestCase):

    def setUp(self):
        self.session = requests.Session()
        self.login_test = GetApi()


    def tearDown(self):
        self.session.close()

    @parameterized.expand(data_json())
    def test_login(self,mobile,password,success,code,message):
        # print("*" * 100)
        # print(mobile,password,success,code,message)
        # print("*" * 100)
        response = self.login_test.get_login(self.session,mobile,password)
        # print("_"*100)
        # print(response.json())
        self.assertEqual(success, response.json().get("success"))
        self.assertEqual(code,response.json().get("code"))
        self.assertEqual(message,response.json().get("message"))
        logging.INFO("登录操作aaaaaaaa")
        print("sjdifsoif jsij时间都i")

    def test_login_success(self):
        response = self.login_test.get_login(self.session, "13800000002", "123456")
        print(response.json())
        self.assertEqual(True,response.json().get("success"))
        self.assertEqual(10000,response.json().get("code"))
        self.assertEqual("操作成功！",response.json().get("message"))
        logging.info("登录操作aaaaaaaa")
        tonken = response.json().get("data")
        print(tonken)
        app.Token = tonken
