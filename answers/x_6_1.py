# x_6_1
#
# ヒントを参考にq_1 ~ q_4がそれぞれどんな値となるかを予想してください

members = [
    ['桃太郎', 'いぬ', 'さる', 'きじ'], 
    ['かに', 'くり', 'うす', 'はち', '牛糞']
]

# ヒント

hint_1 = members[0][0]
hint_2 = members[0][2]
hint_3 = members[1][2]

# ここから問題

q_1 = members[1][0]  # => かに（2番目のリストの先頭の値）
q_2 = members[0][-1]  # => きじ（1番目のリストの最後の値）
q_3 = len(members[1])  # => 5（2番目のリストの要素の数）
q_4 = members[1][len(members[1]) - 2]  # => はち（2番目のリストの最後から２番目）
