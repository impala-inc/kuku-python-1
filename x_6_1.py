# x_6_1
#
# ヒントを参考にq_1 ~ q_4がそれぞれどんな値となるかを予想してください

from module.qa import qa, ex

members = [['桃太郎', 'いぬ', 'さる', 'きじ'], ['かに', 'くり', 'うす', 'はち', '牛糞']]

# ヒント

hint_1 = members[0][0]
hint_2 = members[0][2]
hint_3 = members[1][2]

# ここから問題

q_1 = members[1][0]
q_2 = members[0][-1]
q_3 = len(members[1])
q_4 = members[1][len(members[1]) - 2]

# ここはとりあえず無視
for i in range(3):
    ex(f'hint_{i + 1}', locals()[f'hint_{i + 1}'])
for i in range(4):
    qa(f'q_{i + 1}', locals()[f'q_{i + 1}'])
