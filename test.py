# 单元测试
from _pytest import unittest


class TestDict(unittest.TestCase):

    def test_init(self):
        print('test_init')

    if __name__ == '__main__':
        unittest.main()