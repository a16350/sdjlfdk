import unittest

from sdjlfdk import app
from sdjlfdk.case.IHRM_handler import HandlerIHRM
from sdjlfdk.case.TestIHRMUser import TsetIhrmUsser
from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(TsetIhrmUsser("test_login_success"))
suite.addTest(HandlerIHRM("test_emp_add"))
suite.addTest(HandlerIHRM("test_emp_update"))
suite.addTest(HandlerIHRM("test__emp_get"))
suite.addTest(HandlerIHRM("test_emp_delete"))
filename = app.Get_Path +"/report/result.html"
print(filename)
with open(filename ,"wb") as f:
    runner = HTMLTestRunner(f,title="测试报告",description="v1.0")
    runner.run(suite)