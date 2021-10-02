# x_6_3
#
# 全てのメンバーに対して「○○さんこんにちは」と表示できるようにプログラムを追加してください
# ヒント: for文の中でさらにfor文を使う

teams = [
    ['桃太郎', 'いぬ', 'さる', 'きじ'],
    ['かに', 'くり', 'うす', 'はち', '牛糞']
]
print(teams)

for team in teams:
    for member in team:
        print(member + 'さんこんにちは')
