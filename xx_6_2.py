# xx_6_2
#
# 例外処理を使うことで数字が入力されるまで何度でも入力を繰り返すように修正してください。

num = input('数字を入力してください:')

try:
    num = int(num)
except ValueError:
    print('数字に変換できない値が入力されました')

print(num)
