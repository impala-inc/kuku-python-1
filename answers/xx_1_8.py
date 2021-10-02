# xx_1_8
#
#

def greeting(now):
    if is_morning(now):
        return 'おはよう'
    if is_afternoon(now):
        return 'こんにちは'

    return 'こんばんは'


def is_morning(now):
    return 4 <= now < 11


def is_afternoon(now):
    return 11 <= now < 18


now = 14
print(greeting(now))
