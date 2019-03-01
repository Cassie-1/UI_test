import unittest,os,HTMLTestRunner
import sys
sys.path.append("G:\\pythonWorkSpace\\workspace\\UI_autotest\\")

test_dir='./'
suite=unittest.TestLoader().discover(test_dir,pattern='test_test*.py')

cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(cur_path,"reports")
if not os.path.exists(report_path):
    os.mkdir(report_path)

if __name__=='__main__':
    html_report = report_path + r"\result.html"
    fp = open(html_report, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title='单元测试报告', description='用例执行情况')

    # runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)