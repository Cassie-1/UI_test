import unittest,os,HTMLTestRunner
from unit_test.abs_test import AbsTest
from unit_test.sort_test import SortTest

test_dir='./'
suite=unittest.TestLoader

cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(cur_path,"report")
if not os.path.exists(report_path):
    os.mkdir(report_path)


suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(AbsTest))
suite.addTest(unittest.makeSuite(SortTest))

if __name__=='__main__':
    html_report=report_path+r"\result.html"
    fp=open(html_report,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title='单元测试报告',description='用例执行情况')
    # runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
