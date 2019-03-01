import time,unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.testtwo_homepage import Test_Two_HomePage

class Testtwo_test(BaseTestCase):
    def test_two(self):
        test_two_homepage=Test_Two_HomePage(self.driver)
        # 登录
        test_two_homepage.admin_login('admin','admin')
        # 删除帖子
        test_two_homepage.delete()
        # 进入版块管理(管理中心 - -论坛)
        test_two_homepage.enter_plate('admin')
        # 创建新的版块
        test_two_homepage.new_plate('自动化测试')
        # 管理员退出
        test_two_homepage.logout()
        # 普通用户登录
        test_two_homepage.login('lucky ','lucky')
        # 在新的版块下发帖
        test_two_homepage.send_post('你好呀','大家好，今天是2月27日')
        # 回复帖子
        test_two_homepage.reply_post('是的呀,加油鸭，加油鸭')

if __name__=='__main__':
    unittest.main()