# x_8_7
#
# 以下は気象庁ホームページ防災気象情報のURLから取得したデータの一部です。
# 「weathers」に今日、明日、明後日の天気が含まれています。
# 東京地方の明日の天気を表示してください。

import requests

url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"

response = requests.get(url)
json = response.json()

print(json[0]['timeSeries'][0]['areas'])
print('東京地方の明日の天気は')
