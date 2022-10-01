# x_7_1
#
# ヒントを参考にq_1 ~ q_2がそれぞれどんな値となるかを予想してください

from module.qa import qa, ex

momotaro = {
    '名前': '桃太郎',
    'ヒットポイント': 1800,
    '攻撃力': 230,
    '守備力': 200,
    '身長': 175,
    '体重': 65,
    '出身': '岡山',
    '好きな食べ物': 'きびだんご',
}

# ヒント

hint_1 = momotaro['名前']
hint_2 = momotaro['身長']

# ここから問題

q_1 = momotaro['守備力']
q_2 = momotaro['好きな食べ物']

# ここはとりあえず無視
for i in range(2):
    ex(f'hint_{i + 1}', locals()[f'hint_{i + 1}'])
for i in range(2):
    qa(f'q_{i + 1}', locals()[f'q_{i + 1}'])
