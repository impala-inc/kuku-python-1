# x_7_6
#
# 「kibidango」はきび団子一つずつ食べた順番です。誰が何個食べたのかを辞書「counts」集計して表示してください

kibidango = ['桃太郎', 'いぬ', 'さる', '桃太郎', 'きじ', '桃太郎',
             'いぬ', '桃太郎', 'きじ', 'さる', 'いぬ', 'さる', '桃太郎']
counts = {}

for member in kibidango:
    if member in counts:
        counts[member] += 1
    else:
        counts[member] = 0

print(counts)
