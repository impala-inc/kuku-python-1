# x_9_1
#
# 「files」フォルダにある「prefecture.csv」を読み込んで「北海道の都道府県番号は01」のように全ての県を表示してください

import csv

file = open('./files/prefecture.csv')

reader = csv.DictReader(file)
for row in reader:
    print(row)

file.close()
