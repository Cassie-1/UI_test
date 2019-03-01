import time,unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.testfour_homepage import Test_four_homepage

class Test_test_four(BaseTestCase):
    def test_test_four(self):
        four_test_homepage=Test_four_homepage(self.driver)
        four_test_homepage.login()
        four_test_homepage.publish_post()
        four_test_homepage.vote()
        four_test_homepage.get_name_ratio()
        four_test_homepage.get_theme_name()

if __name__=="__main__":
    unittest.main()