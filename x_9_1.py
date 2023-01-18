# x_9_1
#
# 「files」フォルダにある「prefecture.csv」を読み込んでいます。
# 「北海道の都道府県番号は01」のように全ての県を表示してください

import csv

# ここでファイルを開いている
file = open('./files/prefecture.csv', encoding="utf-8")

# 辞書として読み込む
reader = csv.DictReader(file)
for row in reader:
    print(row)

# ここでファイルを閉じている
file.close()
