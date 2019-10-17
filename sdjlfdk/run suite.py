import unittest

from sdjlfdk.case.IHRM_handler import HandlerIHRM
from sdjlfdk.case.TestIHRMUser import TsetIhrmUsser

suite = unittest.TestSuite()
suite.addTest(TsetIhrmUsser("test_login_success"))
suite.addTest(HandlerIHRM("test_emp_add"))
suite.addTest(HandlerIHRM("test_emp_update"))
suite.addTest(HandlerIHRM("test__emp_get"))
suite.addTest(HandlerIHRM("test_emp_delete"))
runner = unittest.TextTestRunner()
runner.run(suite)
