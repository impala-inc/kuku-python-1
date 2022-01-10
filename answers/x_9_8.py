# x_9_8
#
# 「8-4」を参考にチャットボットを「今何時」という質問に「○○時○○分です」と現在時刻を回答できるように修正してください
# ヒント: 時間と分は「now.hour」と「now.minute」を使います

import datetime

chatbot = [
    {'question': 'おはよう', 'answer': 'おはようございます'},
    {'question': 'おやすみ', 'answer': 'おやすみなさい'},
    {'question': '今日は何日ですか', 'answer': '2021年11月14日です'},
    {'question': '今日の天気は', 'answer': '雨です'},
    {'question': '何か歌って', 'answer': 'もーもたろさんももたろさん'},
    {'question': 'ジャンケン', 'answer': 'グー'},
]

message = input('何か話しかけてください:')

if message == '今何時':
    now = datetime.datetime.now()
    print(str(now.hour) + '時' + str(now.minute) + '分です')
else:
    for q_and_a in chatbot:
        if q_and_a['question'] == message:
            print(q_and_a['answer'])
            break
