# x_6_5
#
# 「members」が最後にどんな値となるかを予想してください

members = ['桃太郎', 'いぬ', 'さる', 'きじ']

members.append('うす')
print(members)

members.remove('さる')
print(members)

members.insert(0, 'うらしまたろう')
print(members)

members.insert(1, 'きんたろう')
# => ['うらしまたろう', 'きんたろう', '桃太郎', 'いぬ', 'さる', 'きじ', 'うす']
members.remove('きじ')
# => ['うらしまたろう', 'きんたろう', '桃太郎', 'いぬ', 'さる', 'うす']
members.append('かに')
# => ['うらしまたろう', 'きんたろう', '桃太郎', 'いぬ', 'さる', 'うす', 'かに']

print(members)
