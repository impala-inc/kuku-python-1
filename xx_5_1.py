# xx_5_1
#
# 「minus()」の関数をテストするコードを追加してください。

import unittest


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


class TestMethods(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(plus(3, 5), 8)


if __name__ == '__main__':
    unittest.main()
