# x_8_7
#
# requestsという外部ライブラリを使用します。
# requestsが見つからないというエラーが出た場合はコンソールで
# pip3 install requests
# と打ち込むとインストールしてくれます
#
# 以下は気象庁ホームページ防災気象情報のURLから取得したデータの一部です。
# 「weathers」に今日、明日、明後日の天気が含まれています（参考: files/tokyo.py）。
# 東京地方の明日の天気を表示してください。

import requests
import pprint

url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"

response = requests.get(url)
tenki = response.json()

pprint.pprint(tenki)

print('東京地方の明日の天気は')
