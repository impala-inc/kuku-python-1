# x_3_4
#
# ヒントを参考にq_1 ~ q_4がそれぞれどんな値となるかを予想してください

# ヒント

hint_1 = type(True).__name__
hint_2 = type(False).__name__
hint_3 = int(True)
hint_4 = int(False)

# ここから問題

q_1 = bool(1)      # => True
q_2 = bool(0)      # => False
q_3 = bool('abc')  # => True
q_4 = bool('')     # => False(空文字「''」はFalseと判定される)
