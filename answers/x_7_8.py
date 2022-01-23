# x_7_8
#
# 「7-7」のコードを「やめる」と入力するまで何度でも繰り返し質問できるようにコードを追加してください

chatbot = [
    {'question': 'おはよう', 'answer': 'おはようございます'},
    {'question': 'おやすみ', 'answer': 'おやすみなさい'},
    {'question': '今日は何日ですか', 'answer': '2021年11月14日です'},
    {'question': '今日の天気は', 'answer': '雨です'},
    {'question': '何か歌って', 'answer': 'もーもたろさんももたろさん'},
    {'question': 'ジャンケン', 'answer': 'グー'},
]

while True:
    message = input('何か話しかけてください:')
    if message == 'やめる':
        break

    is_answered = False

    for q_and_a in chatbot:
        if q_and_a['question'] == message:
            print(q_and_a['answer'])
            is_answered = True
            break

    if not is_answered:
        print('わかりません')
