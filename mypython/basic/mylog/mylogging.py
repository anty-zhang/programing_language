# -*- coding: utf-8 -*-
##################################################################################
# logging 模块学习
##################################################################################


import logging
logger = logging.getLogger(__name__)
# logger = logging.getLogger("myapplication")


def test1():
    """
    输出到文件
    """
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp1.log',
                    filemode='w')

    logging.debug('This is debug message')
    logging.info('This is info message')
    logging.warning('This is warning message')


def test2():
    """
    输出到控制台和文件
    """
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='w')

    #################################################################################################
    # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
    # 将日志同时输出到文件和屏幕
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    ################################################################################################

    logging.debug('This is debug message')
    logging.info('This is info message')
    logging.warning('This is warning message')


def test3():

    # logger.setLevel(logging.DEBUG)
    logger.debug("test logging")

if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    test1()