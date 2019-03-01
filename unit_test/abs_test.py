import unittest
from unit_test.abs import abs
from ddt import data,unpack,ddt
@ddt

class AbsTest(unittest.TestCase):
    def setUp(self):
        print("开始执行测试。。。")
    @data([1,1],[-1,1],[0,0])
    @unpack
    def test_abs(self, n, expext_value):
        result=abs(n)
        self.assertEqual(result,expext_value,msg=result)

    def tearDown(self):
        print('结束测试。。。')

if __name__=="__main__":
        unittest.main(verbosity=2)