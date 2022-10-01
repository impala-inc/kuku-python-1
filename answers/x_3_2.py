# x_3_2
#
# 正しいか正しくないかを表すデータの型を「真偽値(boolean)」と呼びます
# q_1 ~ q_4がそれぞれどんな値となるかを予想してください

# ヒント

hint_1 = True and True
hint_2 = False and True
hint_3 = True or True
hint_4 = False or True

# ここから問題

q_1 = True and True and True and False  # => False(一つでもFalseがあるとFalse)
q_2 = True and (False or True)          # => True
q_3 = not True                          # => False(「not」は右の判定の否定)
q_4 = True and not False                # => True(「not」は右の判定の否定)
