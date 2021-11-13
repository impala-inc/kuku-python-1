# x_6_8
#
# for文またはwhile文を使ってmax_numがリストの中の最も大きな数字になるようにコードを追加してください

nums = [15, 29, 23, 12, 77, 55, 29, 62]

max_num = nums[0]

for num in nums:
    if max_num < num:
        max_num = num

print(max_num)
