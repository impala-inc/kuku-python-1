# x_6_2
#
# 「6-1」のmembersのように要素にリストを持つリストを多重リストと呼びます
# 「〒700-0045 岡山県岡山市 桃太郎様」のように１行づつ表示してください。

addresses = [
    ['桃太郎', '700-0045', '岡山県', '岡山市'],
    ['いぬ', '701-0101', '岡山県', '倉敷'],
    ['さる', '708-0000', '岡山県', '津山市'],
    ['きじ', '706-0000', '岡山県', '玉野市'],
]

for address in addresses:
    print('〒' + address[1] + ' ' + address[2] +
          address[3] + ' ' + address[0] + '様')

# フォーマット文「f」を使うと、変数を埋め込むことが出来ます
for address in addresses:
    print(f'〒{address[1]} {address[2]}{address[3]} {address[0]}様')
