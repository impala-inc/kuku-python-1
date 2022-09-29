# x_3_4
#
# ヒントを参考にq_1 ~ q_4がそれぞれどんな値となるかを予想してください

from module.qa import qa, ex

# ヒント

hint_1 = type(True).__name__
hint_2 = type(False).__name__
hint_3 = int(True)
hint_4 = int(False)

# ここから問題

q_1 = bool(1)
q_2 = bool(0)
q_3 = bool('abc')
q_4 = bool('')

# ここはとりあえず無視
for i in range(4):
    ex(f'hint_{i + 1}', locals()[f'hint_{i + 1}'])
for i in range(4):
    qa(f'q_{i + 1}', locals()[f'q_{i + 1}'])
