# x_4_2
#
# 「4-1」で使った繰り返し処理の構文を「while文」と呼びます
# 「number」が偶数の時は「○は偶数です」と奇数の時「○は奇数です」と表示されるように修正してください

number = 1# 初期値

while number <= 10:
    if number % 2 == 0:
        print(str(number) + 'は偶数です')
    else:
        print(str(number) + 'は奇数です')

    number += 1

