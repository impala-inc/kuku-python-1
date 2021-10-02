# x_5_6
#
# 「while文」を使って「鬼退治のメンバーは桃太郎いぬさるきじです」と表示するようにコードを追加してください

members = ['桃太郎', 'いぬ', 'さる', 'きじ']

text = '鬼退治のメンバーは'

number = 0

while number < len(members):
    text += members[number]
    number += 1

print(text)
