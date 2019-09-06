from common.base import Duogongnneg
from selenium.webdriver.common.by import By
from selenium import webdriver

# 触发登录按钮元素
ckdenglu=(By.XPATH,'.//*[@id="u1"]/a[7]')
# 点击用户名登录按钮元素
ckyhmdl=(By.XPATH,".//*[@id='TANGRAM__PSP_10__footerULoginBtn']")
# 用户名输入框元素
syusername=(By.XPATH,'.//*[@id="TANGRAM__PSP_10__userName"]')
# 密码输入框元素
syuserpassword=(By.XPATH,'.//*[@id="TANGRAM__PSP_10__password"]')
# 记住密码点选矿元素
ckbcdl=(By.XPATH,'.//*[@id="TANGRAM__PSP_10__memberPass"]')
# 登录按钮元素
ckdl=(By.XPATH,'.//*[@id="TANGRAM__PSP_10__submit"]')

jianceyuansu=(By.XPATH,'.//*[@id="TANGRAM__39__content_msgtext"]')


# 登录界面封装方法
class Longinuser(Duogongnneg):


    # 触发登录框方法
    def chufadenglu(self):
        self.click(ckdenglu)
    # 点击用户名登录方法
    def ckyonghumingdenglu(self):
        self.click(ckyhmdl)
    # 输入用户名方法
    def sryonghuming(self, username="17610661663"):
        self.sendkey(syusername, username)
    # 输入用户密码方法
    def srmima(self,userpass="duanyu1203.."):
        self.sendkey(syuserpassword, userpass)
    # 点击记住密码单选框方法
    def ckjizhnima(self):
        self.click(ckbcdl)
    # 点击登录按钮方法
    def ckdengluanniu(self):
        self.click(ckdl)


    def jiancedenglu(self):
        isE = self.isElementI(jianceyuansu)

        return isE



    # 执行登录自动化
    def longin(self, username="17610331663", userpassword="duanyu1203.."):
        self.click(ckdenglu)
        self.click(ckyhmdl)
        self.sendkey(syusername, username)
        self.sendkey(syuserpassword,userpassword)
        self.click(ckbcdl)
        self.click(ckdl)





