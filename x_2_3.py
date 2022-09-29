# x_2_3
#
# ヒントを参考にq_1 ~ q_4がそれぞれどんな値となるかを予想してください

from module.qa import qa, ex

# ヒント

hint_1 = 4 / 3
hint_2 = 4 // 3
hint_3 = 4 % 3
hint_4 = 5 / 3
hint_5 = 5 // 3
hint_6 = 5 % 3

# ここから問題

q_1 = 7 // 5
q_2 = 7 % 5
q_3 = 13 // 4
q_4 = 13 % 4

# ここはとりあえず無視

for i in range(6):
    ex(f'hint_{i + 1}', locals()[f'hint_{i + 1}'])
for i in range(4):
    qa(f'q_{i + 1}', locals()[f'q_{i + 1}'])
