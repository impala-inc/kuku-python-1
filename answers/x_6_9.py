# x_6_9
#
# while文を使って次のリストを数が小さい順に並び替えてください
# ヒント: min()とremove()を使ってnumbersの最小値を求めていくと簡単です

numbers = [70, 29, 23, 12, 77, 55, 29, 62]
new_numbers = []

while True:
    if not numbers:
        break

    new_numbers.append(min(numbers))
    numbers.remove(min(numbers))

print(new_numbers)
