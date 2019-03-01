import unittest
from unit_test.sort import sort
from ddt import ddt,data,unpack
@ddt
class SortTest(unittest.TestCase):
    def setUp(self):
        print('开始执行测试')
    @data([1,0,2],[1,1,10],[1,2,20],[0,0,0])
    @unpack
    def test_sort(self,num1,num2,expect_value):
        result=sort(num1,num2)
        self.assertEqual(result,expect_value,msg=result)
    def tearDown(self):
        print('结束测试。。。')

if __name__=='__main__':
    unittest.main(verbosity=2)
