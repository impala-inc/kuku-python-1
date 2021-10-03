# x_8_4
#
# 今日の日付を「2021年8月31日(土)」のように「月」や「日」などを使って表示するようににコードを追加してください

import datetime

now = datetime.datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.weekday())

wday = ['月', '火', '水', '木', '金', '土', '日']

print(str(now.year) + '年' + str(now.month) + '月' +
      str(now.day) + '日(' + wday[now.weekday()] + '）')
