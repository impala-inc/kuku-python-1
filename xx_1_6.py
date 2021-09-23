# xx_1_6
#
# 日付を引数にとりその日が何曜日であるかを返す「get_weekday()」を定義してください。

import datetime

birthday = '2021-12-29'
date = datetime.datetime.strptime(birthday, '%Y-%m-%d')

print(date)
print(date.weekday())

input('誕生日を入力してください(例2021-12-29):')


def get_weekday(birthday):
    pass
