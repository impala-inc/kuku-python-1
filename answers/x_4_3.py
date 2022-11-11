# x_4_3
#
# 「4-1」のカウントダウンを1秒ずつ実行するように修正してください

import time

print('今からカウントダウンを始めます')
time.sleep(2)

number = 10
while number >= 0:
    print(number)

    number -= 1
    time.sleep(1)
