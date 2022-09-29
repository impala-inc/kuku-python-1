# x_2_2
#
# ヒントを参考にq_1 ~ q_4がそれぞれどんな値となるかを予想してください
from module.qa import qa, ex

# ヒント

hint_1 = 5 + 3 * 8
hint_2 = (5 + 3) * 8
hint_3 = 5 ** 2
hint_4 = 2 ** 3

# ここから問題

q_1 = 3 + 7 * 5
q_2 = (3 + 7) * 5
q_3 = (3 * 3) ** 2
q_4 = 3 * 3 ** 2


# ここはとりあえず無視

for i in range(4):
    ex(f'hint_{i + 1}', locals()[f'hint_{i + 1}'])
for i in range(4):
    qa(f'q_{i + 1}', locals()[f'q_{i + 1}'])
