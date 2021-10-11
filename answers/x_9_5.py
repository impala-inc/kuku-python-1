# x_9_5
#
# 「mode='r+'」で開くとファイルの読み込み上書き保存されるので、攻撃を受けた結果を「momotaro.csv」に保存してください。

import csv

file = open('./files/momotaro.csv', mode='r+', encoding="utf-8")
labels = ['名前', '攻撃力', '守備力', 'ヒットポイント']

members = csv.DictReader(file)
writer = csv.DictWriter(file, fieldnames=labels)

for member in members:
    if member['名前'] == '桃太郎':
        print('青鬼の攻撃。桃太郎は150のダメージを受けた')
        hp = int(member['ヒットポイント']) - 150
        member['ヒットポイント'] = hp

    writer.writerow(member)

file.close()
