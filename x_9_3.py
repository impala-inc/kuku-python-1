# x_9_3
#
# 「momotaro.csv」を読み込んで「7-5」のmembersリストを作成してください

import csv

file = open('./files/momotaro.csv')

reader = csv.DictReader(file)
for row in reader:
    print(row)

file.close()
