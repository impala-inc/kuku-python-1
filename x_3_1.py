# x_3_1
#
# ヒントを参考にq_1 ~ q_4がそれぞれどんな値となるかを予想してください

from module.qa import qa, ex

# ヒント

hint_1 = 100 > 90
hint_2 = 90 == 90
hint_3 = 90 != 90
hint_4 = 90 <= 90

# ここから問題

q_1 = 100 < 70
q_2 = 60 == 60
q_3 = 75 < 75
q_4 = 60 >= 55

# ここはとりあえず無視
for i in range(4):
    ex(f'hint_{i + 1}', locals()[f'hint_{i + 1}'])
for i in range(4):
    qa(f'q_{i + 1}', locals()[f'q_{i + 1}'])
