# x_9_7
#
# 「momotaro」と「aka_oni」が交互に攻撃してどちらかのヒットポイントが0以下になると「◯◯の勝ち」と表示してください
# ただしそれぞれの相手に与えるダメージは「momotaro_attack」と「aka_oni_attack」とする

import random

momotaro = {
    '名前': '桃太郎',
    'ヒットポイント': 1800,
    '攻撃力': 230,
    '守備力': 200,
}

aka_oni = {
    '名前': '赤鬼',
    'ヒットポイント': 2500,
    '攻撃力': 250,
    '守備力': 250,
}

while True:
    momotaro_attack = ((momotaro['攻撃力'] / 2) - (aka_oni['守備力'] / 4)) * \
        (random.randint(7, 9) / 8)
    print(aka_oni['名前'] + 'は' + str(momotaro_attack) + 'のダメージを受けた')
    aka_oni['ヒットポイント'] -= momotaro_attack
    if aka_oni['ヒットポイント'] <= 0:
        print('桃太郎の勝ち')
        break

    aka_oni_attack = ((aka_oni['攻撃力'] / 2) - (momotaro['守備力'] / 4)) * \
        (random.randint(7, 9) / 8)
    print(momotaro['名前'] + 'は' + str(aka_oni_attack) + 'のダメージを受けた')
    momotaro['ヒットポイント'] -= aka_oni_attack
    if momotaro['ヒットポイント'] <= 0:
        print('赤鬼の勝ち')
        break
