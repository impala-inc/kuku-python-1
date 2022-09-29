# x_2_6
#
# ヒントを参考にq_1 ~ q_4がそれぞれどんな値となるかを予想してください
from module.qa import qa, ex

# ヒント

hint_1 = type('桃太郎')  # => str(文字列)
hint_2 = type(10)       # => int(整数)
hint_3 = type(12.3)     # => float(浮動小数点数)

# ここから問題（strやintなどで答えてください）

q_1 = type('777')
q_2 = type(10 + 3.5)
q_3 = type(14 / 7)
q_4 = type(10_000_000)

# ここはとりあえず無視
for i in range(3):
    ex(f'hint_{i + 1}', locals()[f'hint_{i + 1}'].__name__)
for i in range(4):
    qa(f'q_{i + 1}', locals()[f'q_{i + 1}'].__name__)
