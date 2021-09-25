# x_9_2
#
# 「7-9」で入力した質問と回答を「chatbot.csv」に保存するように修正してください

import csv

file = open('./files/chatbot.csv', mode='a')

writer = csv.writer(file)
writer.writerow(['日本の首都', '東京'])

file.close()
