import unittest
from fengz_page import fengz_page
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
class test_case(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Firefox()
        sleep(2)
    def tearDown(self) -> None:
        self.driver.quit()#退出
    def test_01(self):#===登录===
        try:
            po = fengz_page(self.driver)
            po.luoji1()
        except  Exception as e:
            print(e)
    def test_02(self):#====加入购物车===
        try:
            po = fengz_page(self.driver)
            po.luoji2()
        except  Exception as e:
            print(e)
    def test_03(self):#====购物车购买商品===
        try:
            po = fengz_page(self.driver)
            po.luoji3()
        except  Exception as e:
            print(e)
    def test_04(self):#====搜索===
        try:
            po = fengz_page(self.driver)
            po.luoji4()
        except  Exception as e:
            print(e)
if __name__ == '__main__':
    unittest.main()
