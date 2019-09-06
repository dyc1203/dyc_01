# 导入unittest框架
import unittest
# 导入HTMLTestRunner_cn工具
from common import  HTMLTestRunner_cn
# 拿到测试用例存放路径
casePath = 'E:/pom-auto//case'
# 筛选开头为test结尾为.py的测试用例文件
rule = "test*.py"

# 调出unittest.defaultTestLoader中discover方法，查找用例目录       匹配规则
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
# 打印出discover的值查看输入的值是否有效
print(discover)

# 报告路径的存放地址+明见名称和后缀名称
reportPath = 'E:/pom-auto//repory'+'report.html'
# 打开这个路径，切换到写入模式
fp = open(reportPath,"wb")
# 使用HTMLTestRunner_cn.HTMLTestRunner方法输入参数来获取测试报告
# （参数一：填写输出报告路径、参数二：报告的title、参数三：报告说明、参数四：如果遇到问题在重新执行一遍）
runneer = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title='本次测试报告结果',description="这是一个好帅的报告",retry=1)

# 通过调用工具调用run方法，填写用例路径参数开始执行
runneer.run(discover)

# 执行完要养成关闭的好习惯
fp.close()