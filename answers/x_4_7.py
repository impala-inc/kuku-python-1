# x_4_7
#
# 「4-3」のカウントダウンを1秒ずつ同じ行に表示するように修正してください

import time

print('今からカウントダウンを始めます')
time.sleep(2)

number = 10
while True:
    if number < 10:
        print('\r0' + str(number), end='')
    else:
        print('\r' + str(number), end='')

    number -= 1
    time.sleep(1)

    if number < 0:
        break

# ほかにも様々な「0埋め」の方法があります
