# x_2_9
#
# 実行すると「バナナを何房買いましたか？:」と表示されるので、その後に続けてキーボードから数字を入力できます
# バナナとリンゴを買った合計金額を表示してください

banana_price = 200
apple_price = 100

banana_count = input('バナナを何房買いましたか？:')
apple_count = input('リンゴを何個買いましたか？:')

total = banana_price * int(banana_count) + apple_price * int(apple_count)

print('合計は' + str(total) + '円です')
