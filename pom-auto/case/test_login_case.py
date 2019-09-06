from page import Loguser
import unittest
from selenium import webdriver
# 导入数据驱动
import ddt

'''
测试用例：
1.输入正确的密码错误的用户名，点击登录。期望结果登录失败
2.输入正确的用户名错误的密码，点击登录。期望结果登录失败
3.输入正确的用户名和正确的密码，期望结果登录成功

'''
# 驱动数据
test_datas=[{"username":"1761033166","userpass":"duanyu1203..", "expect":"false"},
            {"username":"17610331663","userpass":"duanyu1203.", "expect":"false"},
            {"username":"17610331663","userpass":"duanyu1203..", "expect":"true"}

]

@ddt.ddt
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

        cls.pg = Loguser.Longinuser(cls.driver)

    def setUp(self):
        self.driver.get("https://www.baidu.com")


    # 执行操作一样的用例我可以将用例参数化
    def longin_case(self, username, userpass, expect):
         self.pg.chufadenglu()
         self.pg.ckyonghumingdenglu()
         self.pg.sryonghuming(username)
         self.pg.srmima(userpass)
         self.pg.ckdengluanniu()
         if expect == "true":
             self.assertTrue(self.pg.jiancedenglu())
         elif expect == "false":
             self.assertFalse(self.pg.jiancedenglu())
         else:
             print("本次期望传参结果错误：" + expect)

             return "参数错误"




    @ddt.data(*test_datas)
    def test_01(self, data):
        # 用数据驱动前的代码
        # 输入正确的密码错误的用户名，点击登录。期望结果登录失败
        #  data1 = test_datas[2]
        #  print("测试数据：%s" % data1)
        #  self.longin_case(data1["username"], data1["userpass"], data1["expect"])
        #  用数据驱动后的代码

         print("测试数据：%s" % data)
         self.longin_case(data["username"], data["userpass"], data["expect"])


    #
    #
    # def test_02(self,data):
    #      # 输入正确的用户名错误的密码，点击登录。期望结果登录失败
    #      # 优化前的代码
    #      # self.pg.chufadenglu()
    #      # self.pg.ckyonghumingdenglu()
    #      # self.pg.sryonghuming()
    #      # self.pg.srmima("d4as668")
    #      # self.pg.ckdengluanniu()
    #      # self.assertFalse(self.pg.jiancedenglu())
    #      '''优化后的代码'''
    #      data1 = test_datas[1]
    #      print("测试数据：%s" % data1)
    #      self.longin_case(data1["username"], data1["userpass"], data1["expect"])
    #
    #
    # def test_03(self,data):
    #      # 输入正确的用户名和正确的密码，期望结果登录成功
    #      data1 = test_datas[2]
    #      print("测试数据：%s" % data1)
    #      self.longin_case(data1["username"], data1["userpass"], data1["expect"])
    #
    #
    #
    #
    #
    # def test_04(self):
    #     # 执行自动化登录
    #     self.pg.longin()
    #     self.assertTrue(self.pg.jiancedenglu())
    #







    @classmethod
    def tearDownClass(cls):
         cls.driver.quit()



if __name__ == "__main__":
    unittest.main()



