# x_4_2
#
# 「4-1」で使った繰り返し処理の構文を「while文」と呼びます
# 九九の9の段「9,18,27,,,,81」を表示するように修正してください

number = 9  # 初期値

while number <= 81:
    print(number)

    number += 9

# こちらの書き方でも問題ありません

number = 1  # 初期値

while number < 10:
    print(number * 9)

    number += 1

# [応用問題]
# 「9 X 1 = 9」「9 X 2 = 18」のように表示させてみてください

number = 1  # 初期値

while number < 10:
    print(9, 'X', number, '=', number * 9)

    number += 1
