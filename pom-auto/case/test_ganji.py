from selenium import webdriver
from page.Ganjiwang import ganjicase
import unittest
import time
'''
1.进入赶集网，点击二手车能正常进入到二手车界面
2.进入赶集网，点击下方的宠物界面能正常进入宠物界面
3.把整个界面下拉到底部，点击上方输入框，输入内容，点击搜索可以正常搜索

'''

class GanjiwangTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.be = ganjicase(cls.driver)



    def setUp(self):
        self.driver.get("http://bj.ganji.com/")

    def test_01(self):
     # 进入赶集网，点击二手车能正常进入到二手车界面
     self.be.ckcar()
     self.be.switch_the_current_window_now()
     title = self.be.iftitle("【北京二手汽车网_北京二手车市场_北京二手车交易市场】-北京赶集网")
     print(title)
     self.assertTrue(title)
     self.be.switch_the_current_window()

    def test_02(self):
     # 进入赶集网，点击下方的宠物界面能正常进入宠物界面
     self.be.ckchongwu()
     self.be.switch_the_current_window_now()
     title = self.be.iftitle("【北京宠物网_北京宠物店_北京宠物市场】-北京赶集网")
     print(title)
     self.assertTrue(title)
     self.be.switch_the_current_window()


    def test_03(self):
     # 把整个界面下拉到底部，点击上方输入框，输入内容，点击搜索可以正常搜索
     self.be.down_progress_bar()
     self.be.sysousuo("本田金翼")
     self.be.ckbutt()
     self.be.switch_the_current_window_now()
     title = self.be.iftitle("【本田金翼信息】赶集网")
     self.assertTrue(title)





    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()






