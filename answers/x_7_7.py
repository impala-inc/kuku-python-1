# x_7_7
#
# チャットボットに何か話しかけてquestionと一致すればanswerを表示するようにコードを追加してください

chatbot = [
    {'question': 'おはよう', 'answer': 'おはようございます'},
    {'question': 'おやすみ', 'answer': 'おやすみなさい'},
    {'question': '今日は何日ですか', 'answer': '2021年11月14日です'},
    {'question': '今日の天気は', 'answer': '雨です'},
    {'question': '何か歌って', 'answer': 'もーもたろさんももたろさん'},
    {'question': 'ジャンケン', 'answer': 'グー'},
]

conversation = input('何か話しかけてください:')

for q_and_a in chatbot:
    if q_and_a['question'] == conversation:
        print(q_and_a['answer'])
        break
