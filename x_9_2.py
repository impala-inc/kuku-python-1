# x_9_2
#
# 「7-9」で入力した質問と回答を「chatbot.csv」に保存するように修正してください

import csv

path = '99-entry/9/files/chatbot.csv'

with open(path, mode='a') as f:
    writer = csv.writer(f)
    writer.writerow(['日本の首都は', '東京です'])
