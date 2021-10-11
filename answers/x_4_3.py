# x_4_3
#
# 「4-1」のカウントダウンを1秒ずつ実行するように修正してください

import time

print('今からカウントダウンを始めます')
time.sleep(2)

number = 10
while True:
    print(number)

    number -= 1
    time.sleep(1)

    if number < 0:
        break
