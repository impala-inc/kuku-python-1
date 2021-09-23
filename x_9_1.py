# x_9_1
#
# 「files」フォルダにある「prefecture.csv」を読み込んで「北海道県の都道府県番号は01」のように表示してください

import csv

path = '99-entry/9/files/prefecture.csv'

with open(path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
