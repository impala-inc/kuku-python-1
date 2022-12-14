# x_7_3
#
# 繰り返し構文を用いて、「status」の全ての値について「名前は桃太郎」などのように表示してください。
# プログラムを参考にして、値が存在しない場合は無視するような処理にしてください。

momotaro = {
    '名前': '桃太郎',
    'ヒットポイント': 1800,
    '攻撃力': 230,
    '守備力': 200,
}

print('名前' in momotaro)
print('血液型' in momotaro)

status = ['名前', 'ヒットポイント', '血液型', '攻撃力', '星座', '守備力']

for stats in status:
    print(stats)
    print(stats in momotaro)
