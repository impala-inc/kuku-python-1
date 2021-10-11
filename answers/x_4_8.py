# x_4_8
#
# 「も」
# 「もも」
# 「ももた」
# 「ももたろ」
# 「ももたろう」
# と表示するように修正してください

import time

number = 0
text = 'ももたろう'
text2 = ''

while number < 5:
    text2 += text[number]
    print('\r' + text2, end='')
    number += 1
    time.sleep(1)

# または

# number = 0
# text = 'ももたろう'

# while number <= 5:
#     print('\r' + text[0:number], end='')
#     number += 1
#     time.sleep(1)
