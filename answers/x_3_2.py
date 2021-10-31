# x_3_2
#
# 正しいか正しくないかを表すデータの型を「真偽値(boolean)」と呼びます
# 「a」「b」「c」「d」がそれぞれどんな値となるかを予想してください

print(True and True)
print(False and True)
print(True or True)
print(False or True)

a = True and True and True and False  # => False(一つでもFalseがあるとFalse)
b = True and (False or True)          # => True
c = not True                          # => False(「not」は右の判定の否定)
d = True and not False                # => True(「not」は右の判定の否定)

# print(a)
# print(b)
# print(c)
# print(d)
