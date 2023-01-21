# x_3_4
#
# ヒントを参考にq_1 ~ q_4がそれぞれどんな値となるかを予想してください

from module import qa

# ヒント

hint_1 = type(True)
hint_2 = type(False)
hint_3 = int(True)
hint_4 = int(False)

# ここから問題

q_1 = bool(1)
q_2 = bool(-100)
q_3 = bool(0)
q_4 = bool('abc')
q_5 = bool('')


# ここはとりあえず無視
qa.execute(locals())
