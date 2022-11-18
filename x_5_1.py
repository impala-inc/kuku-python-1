# x_5_1
#
# ヒントを参考にq_1 ~ q_4がそれぞれどんな値となるかを予想してください

from module import qa

members = ['桃太郎', 'いぬ', 'さる', 'きじ', 'かに', 'くり', 'うす', 'はち', '牛糞']

print(members)

# ヒント

hint_1 = members[0]
hint_2 = members[3]
hint_3 = members[-1]
hint_4 = len(members)

# ここから問題

q_1 = members[2]
q_2 = members[4]
q_3 = members[-2]
q_4 = len(members) - 2


# ここはとりあえず無視
qa.execute(locals(), 4, 4)
