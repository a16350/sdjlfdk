
# 封装的URL前缀
import os
import logging.handlers
import time

Base_URL = "http://182.92.81.159/api/sys/"


# 动态获取绝对路径
Pro_Path = os.path.abspath(__file__)
Get_Path = os.path.dirname(Pro_Path)
print(Get_Path)

Token = None

ID = None


def my_log_config():
    # # 创建日志器,(设置日志器)
    # logger = logging.getLogger()
    # logger.setLevel(logging.INFO)
    # # 创建处理器
    # filename = Get_Path+ "/report/log{}.log".format(time.strftime("%Y%m%d%H%M%S"))
    # to1 = logging.StreamHandler() # 默认打印到控制台
    # lht = logging.handlers.TimedRotatingFileHandler(filename= filename,when="M",
    #                                                 interval = 1,backupCount=2,encoding="utf-8")
    # # 创建格式化器
    # fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    # formatter = logging.Formatter(fmt)
    # # 给处理器添加格式
    # to1.setFormatter(formatter)
    # lht.setFormatter(formatter)
    # # 给日志器添加处理器
    # logger.addHandler(to1)
    # logger.addHandler(lht)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    to1 = logging.StreamHandler()
    filename = Get_Path+ "/report/log{}.log".format(time.strftime("%Y%m%d%H%M%S"))
    to2 = logging.handlers.TimedRotatingFileHandler(filename=filename,when="M",interval=1,
                                                    backupCount=2,encoding="utf-8")
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt=fmt)
    to1.setFormatter(formatter)
    to2.setFormatter(formatter)
    logger.addHandler(to1)
    logger.addHandler(to2)