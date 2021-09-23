# xx_1_9
#
#

import random

momotaro = {
    '名前': '桃太郎',
    'ヒットポイント': 1800,
    '攻撃力': 230,
    '守備力': 200,
    '命中率': 80,
}

aka_oni = {
    '名前': '赤鬼',
    'ヒットポイント': 2500,
    '攻撃力': 250,
    '守備力': 250,
    '命中率': 50,
}

momotaro_attack = (momotaro['攻撃力'] - (aka_oni['守備力'] / 2)) * \
    (random.randint(momotaro['命中率'], 100) / 100)
aka_oni_attack = (aka_oni['攻撃力'] - (momotaro['守備力'] / 2)) * \
    (random.randint(aka_oni['命中率'], 100) / 100)
