# x_5_1
#
# ヒントを参考にq_1 ~ q_4がそれぞれどんな値となるかを予想してください

members = ['桃太郎', 'いぬ', 'さる', 'きじ', 'かに', 'くり', 'うす', 'はち', '牛糞']

# ヒント

hint_1 = members[0]
hint_2 = members[3]
hint_3 = members[-1]

# ここから問題

q_1 = members[2]  # => さる
q_2 = members[4]  # => かに
q_3 = members[-2]  # => はち（後ろから２番目）
q_4 = members[len(members) - 1]  # => 牛糞（一番後ろ: len(members)がmembersの要素の数を表すため）
