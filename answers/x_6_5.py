# x_6_5
#
# 「members」の値を確認したら、append、remove、insertを使って「members」を元に戻してください
# 'さる'を追加する時はappendは使わないようにしてください

members = ['桃太郎', 'いぬ', 'さる', 'きじ']

members.append('うす')
print(members)

members.remove('さる')
print(members)

members.insert(0, 'うらしまたろう')
print(members)

members.insert(1, 'きんたろう')
# => ['うらしまたろう', 'きんたろう', '桃太郎', 'いぬ', 'きじ', 'うす']
members.remove('きじ')
# => ['うらしまたろう', 'きんたろう', '桃太郎', 'いぬ', 'うす']
members.append('かに')
# => ['うらしまたろう', 'きんたろう', '桃太郎', 'いぬ',　'うす', 'かに']

members.remove('うらしまたろう')
members.remove('きんたろう')
members.insert(2, 'さる')
members.remove('うす')
members.remove('かに')
members.append('きじ')

print(members)
