# x_8_6
#
# 日付を入力してもらい「2021-04-19は火曜日です」のように表示するようにコードを修正してください

import datetime

day = '2021-12-29'

date = datetime.datetime.strptime(day, '%Y-%m-%d')

print(type(date))
