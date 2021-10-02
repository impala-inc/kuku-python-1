# x_4_9
#
# 入力した文章が全て逆さ言葉で１行の表示でするように修正してください

text = input('何か文章を入力してください:')

number = len(text) - 1

while number >= 0:
    print(text[number])
    number -= 1
