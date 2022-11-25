# x_3_2
#
# 正しいか正しくないかを表すデータの型を「真偽値(boolean)」と呼びます
# 正しい場合の値は「True」、正しくない場合の値は「False」になります
# ヒントを参考にq_1 ~ q_4がそれぞれどんな値となるかを予想してください

from module import qa

# ヒント

hint_1 = True and True
hint_2 = False and True
hint_3 = True or True
hint_4 = False or True

# ここから問題

q_1 = True and True and True and False
q_2 = True and (False or True)
q_3 = not True
q_4 = True and not False


# ここはとりあえず無視
qa.execute(locals(), 4, 4)
