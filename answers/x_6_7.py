# x_6_7
#
# 「while文」を追加して以下のように表示してください
#
# 花花花花花
# 花花花花花
# 花花花花花
# 花花花花花
# 花花花花花
#
# [応用問題1]真ん中の文字だけ「桃」にしてみてください
# [応用問題2]縦横の文字数を5文字から変更できるようにしてみてください

gyou = 0
while gyou < 5:
    retu = 0
    text = ''
    while retu < 5:
        text += '花'
        retu += 1
    print(text)
    gyou += 1
