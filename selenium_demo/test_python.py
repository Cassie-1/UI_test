class TestPython:
    def __init__(self):
        self.name='你好'

    def eat(self):
        name=self.name
        print('吃东西')

tp=TestPython()
print('----------')
print(tp.name)
print('******')
print(tp.eat())