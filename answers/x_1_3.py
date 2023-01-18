# x_1_3
#
# ヒントを参考に指示された文を表示してください

where = '自宅で'
who = '私は'
how = '３杯も'
what = 'ビーフカレーを食べた'
when = '昨日の晩'
why = 'お腹が空いていたので'

# ヒント

print(when)
print(how)

# 「私は昨日の晩お腹が空いていたので自宅で３杯もビーフカレーを食べた」と１行で表示してください

print(who + when + why + where + how + what)

# このような書き方もできます

print(who, when, why, where, how, what, sep='')
print(f'{who}{when}{why}{where}{how}{what}')
