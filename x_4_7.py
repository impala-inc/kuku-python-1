# x_4_7
#
# 「4-3」のカウントダウンを1秒ずつ同じ行に表示するように修正してください

import time

print('今からカウントダウンを始めます')
time.sleep(2)

print('\r' + '10', end='')
time.sleep(1)
print('\r' + '09', end='')
time.sleep(1)
