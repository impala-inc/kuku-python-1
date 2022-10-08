# x_3_7
#
# 「number」が「5」で割り切れるかどうかを表示できるようにコードを追加してください

number = input('数字を入力してください:')

if int(number) % 3 == 0:
    print(number + 'は3で割り切れます')
else:
    print(number + 'は3で割り切れません')

if int(number) % 5 == 0:
    print(number + 'は5で割り切れます')
else:
    print(number + 'は5で割り切れません')
