# x_4_4
#
# 「4-1」「4-2」「4-3」を全て「break」を使わないように書き直してください

number = 1

while number <= 10:
    print(number)

    number += 1

# x_4_1

number = 1

while number <= 10:
    print(str(number) + '回目')

    number += 1

# x_4_2

number = 1

while number <= 10:
    if number % 2 == 0:
        print(str(number) + 'は偶数です')
    else:
        print(str(number) + 'は奇数です')

    number += 1

# x_4_3

number = 10

while number >= 0:
    print(number)

    number -= 1
