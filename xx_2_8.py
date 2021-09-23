# xx_2_8
#

num = 0


def loop(num):
    print('aho')
    result = 0

    if num < 10:
        result = loop(num + 1)

    return result


print(loop(num))
