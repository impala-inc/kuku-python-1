# x_6_4
#
# セリーグの対戦カードの組み合わせを「巨人 x 阪神」のように表示してください（ただし同一チーム同志は対戦しないこと）

central_league = ['巨人', 'ヤクルト', '横浜', '中日', '阪神', '広島']

for team in central_league:
    for team2 in central_league:
        if not team == team2:
            print(team + ' x ' + team2)
