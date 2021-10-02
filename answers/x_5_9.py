# x_5_9
#
# 「members」の全てのメンバーに対して「○○さんは桃太郎チーム(または猿蟹合戦チーム)です」と表示してください

members = ['かに', 'さる', 'きじ', 'くり', '牛糞', '桃太郎', 'うす', 'いぬ', 'はち']

momotaro_team = ['桃太郎', 'いぬ', 'さる', 'きじ']
sarukani_team = ['かに', 'くり', 'うす', 'はち', '牛糞']

for member in members:
    if member in momotaro_team:
        print(member + 'さんは桃太郎チームです')
    if member in sarukani_team:
        print(member + 'さんは猿蟹合戦チームです')
