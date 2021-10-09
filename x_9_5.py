# x_9_5
#
# 「mode='r+'」で開くとファイルの読み込み上書き保存されるので、攻撃を受けた結果を「momotaro.csv」に保存してください。

import csv

file = open('./files/momotaro.csv', mode='r+')

members = csv.DictReader(file)
for member in members:
    print(member)

print('青鬼の攻撃。桃太郎は150のダメージを受けた')

file.close()
