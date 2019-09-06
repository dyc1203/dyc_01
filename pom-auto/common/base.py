# 底层公共方法调用类
# 导入webdriver
from selenium import webdriver
# 导入 WebDriverWait显示等待
from selenium.webdriver.support.ui import WebDriverWait
# 导入expected_conditions功能类call
from selenium.webdriver.support import expected_conditions as e

import time

class Duogongnneg():
    # 初始化传参driver
    def __init__(self, driver):
        # 将传入的driver进行初始化传参
        self.driver = driver

        # 定义查找元素时间间隔
        self.t = 1
        # 定义朝招元素超时啥上线
        self.times = 10


     # 通过expected_conditions工具类和WebDriverWait显示等待查找元素。传入元素对象
    def findelement(self, longk):

        if not isinstance(longk, tuple):
            print("定位longk参数传入错误，必须元组类型，否则该方法无法处理传入数据")
            print("longk参数说明：第一个参数为定位类型，第二个参数为定位值")
            print("请检查您传入的参数，该传入参数已经在下方展示。传入标准格式为：(XXXX,XXXX)")
            print(longk)
        else:
            try:                                                  # *longk分开转入两个值或者多个
            # 该对象=等待功能类（输入driver参数，总等待时长，间隔多少时间去重新搜索该元素）.
            # 去定位该元素（定位方法+定位坐标值）
             ele = WebDriverWait(self.driver, self.times, self.t).until(e.presence_of_element_located(longk))
             # 代码没报错返回该对象
             print("已经成功定位元素信息：定位方式->%s,value值为->%s" % (longk[0], longk[1]))
             return ele
            except:
                # 代码报错返回提示
                print("错误！！找不到传入元素参数位置，定位失败。请检查是否语法有误或者该元素不在当前界面")
                print("请检查传入参数是否正确")
                print(longk)
                return  "定位失败"

         # 定位多个对象
    def findelements(self, longk):


        if not isinstance(longk, tuple):
            print("定位longk参数传入错误，必须元组类型，否则该方法无法处理传入数据")
            print("longk参数说明：第一个参数为定位类型，第二个参数为定位值")
            print("请检查您传入的参数，该传入参数已经在下方展示。传入标准格式为：(XXXX,XXXX)")
            print(longk)
        else:
            # 该对象=等待功能类（输入driver参数，总等待时长，间隔多少时间去重新搜索该元素）.去定位该元素（定位方法+定位坐标值）
                try:

                    eles = WebDriverWait(self.driver, self.times, self.t).until(e.presence_of_all_elements_located(longk))  # *longk分开转入两个值或者多个
                    # 代码没报错返回该对象
                    return eles
                except:
                    # 代码报错返回空
                    print("错误！！找不到传入元素参数位置，定位失败。请检查是否语法有误或者该元素不在当前界面")
                    print("请检查传入参数是否正确")
                    print(longk)
                    return []

     # 二次封装创建给元素输入文本功能
    def sendkey(self,locator,text):

        try:
            sy = self.findelement(locator)
            sy.send_keys(text)
            return "当前元素文本输入成功"
        except:
            return "当前元素文本输入失败"
        # 二次封装点击元素功能
    def click(self,locator):
        # try:
            cs = self.findelement(locator)
            cs.click()

        #     return "当前元素点击成功"
        # except:
        #     return "当前元素点击失败"


    def isSelected(self,locator):
        '''判断该元素是否被选中（返回布尔值）'''
        ele = self.findelement(locator)
        r = ele.is_selected()

        return r

    def isElementI(self,locator):
        '''判断该元素是否存在（返回布尔值）'''

        ele = self.findelement(locator)
        if ele == "定位失败":

            return False
        else:
            return True


    def isElementI2(self,locator):
            '''定位多个元素判断定位回来的数据是否存在'''
            eles = self.findelements(locator)
            n = len(eles)

            if n == 0:
                return False
            else:
                print(n)
                return True

    def is_title(self, titles):
        '''判断该界面title是否符合当前预期,返回布尔值'''

        try:
            result = WebDriverWait(self.driver, self.times, self.t).until(e.title_is(titles))
            return result
        except:
            return False

    def is_title_contains(self, titles):
        '''判断该界面title部分是否包含当前预期,返回布尔值'''
        try:
            result = WebDriverWait(self.driver, self.times, self.t).until(e.title_contains(titles))
            return result
        except:
            return False

    def is_text_in_ele(self,_text,longk):
        '''判断当前文本元素是否符合预期，返回布尔值'''
        try:
            result = WebDriverWait(self.driver, self.times, self.t).until(e.text_to_be_present_in_element(longk, _text))
            return result
        except:
            return False


    def is_value_in_ele(self,longk,value):
        '''判断当前元素value值是否符合预期，符合返回布尔值，不符合返回False。为null时也返回False'''
        try:
         result = WebDriverWait(self.driver, self.times, self.t).until(e.text_to_be_present_in_element_value(longk, value))
         return result
        except:
            return False

    def is_alert(self):
        '''alert是否存在，存在返回该对象，不存在返回False'''
        try:
         result = WebDriverWait(self.driver, self.times, self.t).until(e.alert_is_present())
         return result
        except:
            return False

    def down_progress_bar(self):
        '''滚动条滚动到底部'''
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        print("您执行了滚动条拖到最下方")
    def up_progress_bar(self):
        '''滚动条滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)
        print("您执行了滚动条拖到最上方")

    def element_progress_bar(self,longk):
        '''滚动到该元素定位位置'''
        ele = self.findelement(longk)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        print("您执行了滚动条拖到对应元素位置")

#
# 进行调试代码，查看工具类方法是生效
# if __name__ == "__main__":

    # driver = webdriver.Chrome()
    # driver.get("http://bj.ganji.com/")
    # gu = Duogongnneg(driver)
    # i=gu.is_title("【北京赶集网】-免费发布信息-北京分类信息门户")
    # print(i)

#     denglus = ("xpath", './/*[text()="招商加盟"]')
#     # gu.down_progress_bar()
#     time.sleep(3)
#     # gu.up_progress_bar()
#     gu.element_progress_bar(denglus)

    #
    #
    # # gu.click(denglus)
    # #
    # # yonghumingdenglu=(By.XPATH,".//*[@id='TANGRAM__PSP_10__footerULoginBtn']")
    # # usershurukuang = (By.XPATH, './/*[@id="TANGRAM__PSP_10__userName"]')
    # # passwordshurukuang = (By.XPATH, './/*[@id="TANGRAM__PSP_10__password"]')
    # # jizhumima = (By.XPATH, './/*[@id="TANGRAM__PSP_10__memberPass"]')
    # # dengluanniu = (By.XPATH, './/*[@id="TANGRAM__PSP_10__submit"]')
    # # gu.click(yonghumingdenglu)
    # # gu.sendkey(usershurukuang, "17610331663")
    # # gu.sendkey(passwordshurukuang, "duanyu1203..")
    # # gu.click(jizhumima)
    # # gu.click(dengluanniu)
    # #
    #
    #
    # ne=gu.is_value_in_ele(denglus,"一百块都不给我")
    #
    # print(ne)
    #
    # # tiletext=(By.XPATH,".//*[@id='u1']")
    # # ne = gu.findelements(tiletext)
    # # se = len(ne)
    # # print(ne)
    #
    #
    #
    # time.sleep(5)
    # driver.quit()



