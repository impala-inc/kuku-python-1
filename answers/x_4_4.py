# x_4_4
#
#while True:とすると、無限ループになります。このまま実行してみてください
#Ctr + C　で止められます
# 「4-1」「4-2」を「if」と「break」を使って書き直してください


number = 1

while True:
    print(number)

    number += 1
    if number > 10:
        break

# x_4_1

number = 10

while True:
    print(number)

    number -= 1

    if number < 0:
        break

# x_4_2

number = 1

while True:
    if number % 2 == 0:
        print(str(number) + 'は偶数です')
    else:
        print(str(number) + 'は奇数です')

    number += 1

    if number > 10:
        break
