# x_3_4
#
# ヒントを参考にq_1 ~ q_4がそれぞれどんな値となるかを予想してください

from module import qa

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
qa.execute(locals(), 4, 4)
