# x_9_3
#
# 「momotaro.csv」を読み込んで「7-5」のmembersリストを作成してください

import csv

path = '99-entry/9/files/momotaro.csv'

with open(path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
