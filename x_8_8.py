# x_8_8
#
# 以下は気象庁ホームページ防災気象情報のURLから取得したデータの一部です。
# urlの中の「130000」は「都道府県番号」 + 「0000」です。
# 「都道府県番号」を指定して「◯◯の明日の天気はxxです」と表示できるように修正してください。

import requests

url = "https://www.jma.go.jp/bosai/forecast/data/forecast/350000.json"

response = requests.get(url)
json = response.json()

print(json[0]['timeSeries'][0]['areas'])
