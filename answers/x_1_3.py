# x_1_3
#
# 「私は昨日の晩お腹が空いていたので自宅で３杯もビーフカレーを食べた」と表示してください

where = '自宅で'
who = '私は'
how = '３杯も'
what = 'ビーフカレーを食べた'
when = '昨日の晩'
why = 'お腹が空いていたので'

print(when)
print(how)

print(who + when + why + where + how + what)

# このような書き方もできます

print(who, when, why, where, how, what, sep='')
print(f'{who}{when}{why}{where}{how}{what}')
