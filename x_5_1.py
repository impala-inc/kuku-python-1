# x_5_1
#
# ヒントを参考にq_1 ~ q_4がそれぞれどんな値となるかを予想してください

from module.qa import qa, ex

members = ['桃太郎', 'いぬ', 'さる', 'きじ', 'かに', 'くり', 'うす', 'はち', '牛糞']

# ヒント

hint_1 = members[0]
hint_2 = members[3]
hint_3 = members[-1]

# ここから問題

q_1 = members[2]
q_2 = members[4]
q_3 = members[-2]
q_4 = members[len(members) - 1]

# ここはとりあえず無視
for i in range(3):
    ex(f'hint_{i + 1}', locals()[f'hint_{i + 1}'])
for i in range(4):
    qa(f'q_{i + 1}', locals()[f'q_{i + 1}'])
