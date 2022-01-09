# x_6_9
#
# while文を使って次のリストを数が小さい順に並び替えてください
# ヒント: 隣り合った数字を比べて「右」の数字が「左」の数字よりも大きければ「右」と「左」の数字を入れ替えます
# ヒント: numbers[0], numbers[1] = numbers[1], numbers[0] で１番目と２番目の数字を入れ替えることができます

numbers = [70, 29, 23, 12, 77, 55, 29, 62]

while True:
    i = 0
    changed = False

    while i < len(numbers) - 1:
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            changed = True
        i += 1

    if not changed:
        break

print(numbers)
