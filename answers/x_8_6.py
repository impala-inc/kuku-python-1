# x_8_6
#
# 日付を入力してもらい「2021-04-19は火曜日です」のように表示するようにコードを修正してください

import datetime

day = input('日付を入力してください(例2021-12-29):')

date = datetime.datetime.strptime(day, '%Y-%m-%d')

print(date)

wday = ['月', '火', '水', '木', '金', '土', '日']

print(day + 'は' + wday[date.weekday()] + '曜日です')
