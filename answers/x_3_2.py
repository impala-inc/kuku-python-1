# x_3_2
#
# 正しいか正しくないかを表すデータの型を「真偽値(boolean)」と呼びます
# 正しい場合の値は「True」、正しくない場合の値は「False」になります
# ヒントを参考にq_1 ~ q_6がそれぞれどんな値となるかを予想してください

# ヒント

hint_1 = True and True
hint_2 = False and True
hint_3 = True and False
hint_4 = False and False
hint_5 = True or True
hint_6 = False or True
hint_7 = True or False
hint_8 = False or False
hint_9 = not True

# ここから問題

q_1 = True and False and True  # => False(一つでもFalseがあるとFalse)
q_2 = True and False or True   # => True
q_3 = True or False and False  # => True(「and」が「or」よりも先に評価される(優先順位が高い))
q_4 = False or True and False  # => False(「and」が「or」よりも先に評価される(優先順位が高い))
q_5 = True and not False       # => True(「not」が「and」よりも先に評価される(優先順位が高い))
q_6 = 30 <= 40 and 100 < 90    # => False
