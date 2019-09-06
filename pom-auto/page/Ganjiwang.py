from common.base import Duogongnneg
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
ershouche = (By.XPATH, './/*[@class="tab-nav tab-nav-l fl"]/dl[4]/dt')
chengwu = (By.XPATH, './/*[@id="pet"]/h3/a[1]')
shurukuang = (By.XPATH, './/*[@id="search_keyword"]')
sousuoanniu = (By.XPATH, './/*[@id="search_button"]')
xinzhilipin = (By.XPATH, ".//*[text()='闲置礼品']")

class ganjicase(Duogongnneg):

   # 点击二手车
   def ckcar(self):
       self.click(ershouche)

   # 点击宠物
   def ckchongwu(self):
       self.element_progress_bar(xinzhilipin)

       self.click(chengwu)

   # 判断当前title是否符合用例标准
   def iftitle(self,coke):

       istitle = self.is_title(coke)

       return istitle
   # 搜索框输入数据
   def sysousuo(self,value):

       self.sendkey(shurukuang,value)
   # 点击搜索按钮
   def ckbutt(self):

       self.click(sousuoanniu)

   # 切换当前窗口

   def switch_the_current_window(self):


        all= self.driver.window_handles
        newhand = all[-1]
        self.driver.switch_to.window(newhand)
        self.driver.close()
        self.driver.switch_to.window(all[0])

        time.sleep(3)
   def switch_the_current_window_now(self):

        all= self.driver.window_handles
        newhand = all[-1]
        self.driver.switch_to.window(newhand)

# if __name__ == "__main__":
#     driver = webdriver.Chrome()
#     driver.get("http://bj.ganji.com/")
#     gu = ganjicase(driver)
#     i = gu.is_title("【北京赶集网】-免费发布信息-北京分类信息门户")
#     print(i)















