# x_2_7
#
# q_1 ~ q_4がそれぞれどんな値となるかを予想してください

from module import qa

# ヒント

hint_1 = str(19.5)
hint_2 = int(19.5)
hint_3 = float(400)
hint_4 = float(45) + int(70)

# ここから問題

q_1 = str(110 + 119)
q_2 = float(110 + 119)
q_3 = str(110) + str(119)
q_4 = int('110') + float('119.5')


# ここはとりあえず無視
qa.execute(locals())
