# x_2_5
#
# ヒントを参考にq_1 ~ q_4がそれぞれどんな値となるかを予想してください

from module.qa import qa, ex

# ヒント

hint_1 = 1_1_1_1
hint_2 = 1.0 + 2.0
hint_3 = 5.0e3

# ここから問題

q_1 = 10_000 + 4
q_2 = 4 + 1.0
q_3 = 3 / 3
q_4 = 5.0e-3

# ここはとりあえず無視

for i in range(3):
    ex(f'hint_{i + 1}', locals()[f'hint_{i + 1}'])
for i in range(4):
    qa(f'q_{i + 1}', locals()[f'q_{i + 1}'])
