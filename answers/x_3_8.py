# x_3_8
#
# 「number」が「3」で割り切れる場合は「Fizz」、「5」で割り切れる場合は「Buzz」
# 「3」でも「5」でも割り切れる場合は「FizzBuzz」
# それ以外は数字をそのまま表示するようにコードを修正してください

number = int(input('数字を入力してください:'))

if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print(number)
