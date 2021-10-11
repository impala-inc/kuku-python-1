# x_2_9
#
# バナナとリンゴを買った金額を表示してください

banana = 200
apple = 100

banana_count = input('バナナを何房買いましたか？:')
apple_count = input('リンゴを何個買いましたか？:')

total = banana * int(banana_count) + apple * int(apple_count)

print('掛け算した結果は' + str(total) + '円です')
