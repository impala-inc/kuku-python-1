# x_3_4
#
# ヒントを参考にq_1 ~ q_4がそれぞれどんな値となるかを予想してください

# ヒント

hint_1 = type(True)
hint_2 = type(False)
hint_3 = int(True)
hint_4 = int(False)

# ここから問題

q_1 = bool(1)      # => True(「0」以外の数字はTrueと判定される)
q_2 = bool(-100)   # => True(「0」以外の数字はTrueと判定される)
q_3 = bool(0)      # => False(「0」はFalseと判定される)
q_4 = bool('abc')  # => True(空文字「''」以外はTrueと判定される)
q_5 = bool('')     # => False(空文字「''」はFalseと判定される)
