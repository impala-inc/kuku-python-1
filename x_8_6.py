# x_8_6
#
# 「birthday」に自分の誕生日を入力して誕生日が何曜日だったかを表示するようにコードを修正してください

import datetime

birthday = '2021-12-29'
date = datetime.datetime.strptime(birthday, '%Y-%m-%d')

print(date)
print(date.weekday())

input('誕生日を入力してください(例2021-12-29):')
