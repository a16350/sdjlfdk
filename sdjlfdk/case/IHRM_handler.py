import unittest
import requests

from sdjlfdk import app
from sdjlfdk.api.IHRM_api import GetApi


class HandlerIHRM(unittest.TestCase):

    def setUp(self):
        self.session = requests.Session()
        self.add = GetApi()


    def tearDown(self):
        self.session.close()

    def test_emp_add(self):
        response = self.add.emp_add(self.session)
        # self.assertEqual(True,response.json().get("success"))
        # self.assertEqual(10000,response.json().get("code"))
        # self.assertIn("操作成功！",response.json().get("message"))
        data = response.json().get("data")
        id = data.get("id")
        app.ID = id
        print("新增员工成功")
    def test_emp_update(self):
        self.add.emp_update(self.session)
        print("员工信息修改成功")
    def test__emp_get(self):
        response = self.add.emp_get(self.session)
        result = response.json()
        print("查看id",result)
        print("查看数据")
    def test_emp_delete(self):
        self.add.emp_delete(self.session)
        print("新增的数据已经删除")