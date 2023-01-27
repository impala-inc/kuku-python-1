# x_9_4
#
# 「with文」を使うと、「file.close()」を自動でやってくれます。
# 「9-1」のように「北海道の都道府県番号は01」のように全ての県を表示してください

import csv

# ここでファイルを開いている
with open('./files/prefecture.csv', encoding="utf-8") as file:

    # 辞書として読み込む
    reader = csv.DictReader(file)
    for row in reader:
        print(row['都道府県名'] + 'の都道府県番号は' + str(row['都道府県番号']))

# 「file.close()」は必要ない
