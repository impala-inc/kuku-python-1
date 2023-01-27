# x_9_3
#
# 「7-9」で入力した質問と回答を「chatbot.csv」に保存するように修正してください
# 前後でファイルの中身を確認してください

import csv

while True:
    question = input('質問を登録してください:')
    if question == 'やめる':
        break

    answer = input('質問の回答を登録してください:')

    file = open('./files/chatbot.csv', mode='a', encoding="utf-8")

    labels = ['question', 'answer']
    writer = csv.DictWriter(file, fieldnames=labels)
    writer.writerow({'question': question, 'answer': answer})

    file.close()
