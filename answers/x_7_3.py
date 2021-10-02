# x_7_3
#
# 「status」の各値について「名前は桃太郎」などのように表示してください（値が存在しない場合は無視する）

momotaro = {
    '名前': '桃太郎',
    'ヒットポイント': 1800,
    '攻撃力': 230,
    '守備力': 200,
}

print('名前' in momotaro)
print('血液型' in momotaro)

status = ['名前', 'ヒットポイント', '血液型', '攻撃力', '星座', '守備力']

for st in status:
    if st in momotaro:
        print(st + 'は' + str(momotaro[st]))
