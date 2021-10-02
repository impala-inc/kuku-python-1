# x_4_8
#
# 1~15までの数字について
# 「3」で割り切れる場合は「Fizz」、「5」で割り切れる場合は「Buzz」
# 「3」でも「5」でも割り切れる場合は「FizzBuzz」
# それ以外はそのまま数字を表示するようにコードを修正してください

number = 1

while number <= 15:
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)

    number += 1
