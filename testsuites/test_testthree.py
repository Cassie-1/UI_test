import time,unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.testthree_homepage import Test_Three_HomePage
from ddt import ddt,data,unpack

@ddt
class Test_test_three(BaseTestCase):
    @unpack
    def test_test_three(self):
        three_homepage=Test_Three_HomePage(self.driver)
        three_homepage.login()
        three_homepage.search('haotest')
        three_homepage.enter_post()
        title=three_homepage.check()
        try:
            self.assertEqual(title,'haotest',msg=title)
            print('断言结果:帖子标题和期望的一致')
        except:
            print('断言结果:帖子标题和期望的不一致')
        three_homepage.logout()


if __name__=='__main__':
    unittest.main()

