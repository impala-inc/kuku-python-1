# x_8_8
#
# 以下は気象庁ホームページ防災気象情報のURLから取得したデータの一部です。
# urlの中の「130000」は「都道府県番号」 + 「0000」です。
# 「都道府県番号」を入力してもらい「都道府県番号◯◯の明日の天気はxxです」と表示できるように修正してください。

import requests
import pprint

pref_code = input('都道府県番号を入力してください(01~47):')

url = "https://www.jma.go.jp/bosai/forecast/data/forecast/350000.json"

response = requests.get(url)
tenki = response.json()

pprint.pprint(tenki)
