# x_3_9
#
# 12才以下の人には「オレンジジュース」
# 20才以上でお酒が好きな人には「ビール」
# それ以外は「烏龍茶」を出すように修正してください

nenrei = int(input('年齢を入力してください:'))
osake = input('お酒は好きですか？(はい/いいえ):')

if nenrei <= 12:
    print('オレンジジュースをどうぞ')
elif nenrei >= 20 and osake == 'はい':
    print('ビールをどうぞ')
else:
    print('烏龍茶をどうぞ')

# もしくは

# nenrei = int(input('年齢を入力してください:'))
# if nenrei <= 12:
#     print('オレンジジュースをどうぞ')
# elif nenrei < 20:
#     print('烏龍茶をどうぞ')
# else:
#     osake = input('お酒は好きですか？(はい/いいえ):')
#     if osake == 'はい':
#         print('ビールをどうぞ')
#     else:
#         print('烏龍茶をどうぞ')
