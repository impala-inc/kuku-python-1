# x_6_8
#
# for文またはwhile文を使ってmax_numberがリストの中の最も大きな数字になるようにコードを追加してください

numbers = [15, 29, 23, 12, 77, 55, 29, 62]

max_number = numbers[0]

for number in numbers:
    if max_number < number:
        max_number = number

print(max_number)
