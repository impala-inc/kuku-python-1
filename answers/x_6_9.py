# x_6_9
#
# while文を使って次のリストを数が小さい順に並び替えてください
# ヒント: 隣り合った数字を比べて「右」の数字が「左」の数字よりも大きければ「右」と「左」の数字を入れ替えます
# ヒント: nums[0], nums[1] = nums[1], nums[0] で１番目と２番目の数字を入れ替えることができます

nums = [70, 29, 23, 12, 77, 55, 29, 62]

while True:
    i = 0
    converted = False
    while i < len(nums) - 1:
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            converted = True
        i += 1
    if not converted:
        break

print(nums)
