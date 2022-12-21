# x_6_5
#
# 「members」が最後にどんな値となるかを予想してください
# 「members」の値を確認したら、append、remove、insertを使って「members」を元に戻してください

members = ['桃太郎', 'いぬ', 'さる', 'きじ']

members.append('うす')
print(members)

members.remove('さる')
print(members)

members.insert(0, 'うらしまたろう')
print(members)

members.insert(1, 'きんたろう')
members.remove('きじ')
members.append('かに')

print(members)

# ここで「members」を元に戻す

print(members)
