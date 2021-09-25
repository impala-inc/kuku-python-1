# xx_5_2
#
# 「assertFalse()」のテストを追加してください。

import unittest


def is_adult(age):
    return age >= 20


class TestMethods(unittest.TestCase):

    def test_plus(self):
        self.assertTrue(is_adult(20))


if __name__ == '__main__':
    unittest.main()
