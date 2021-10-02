# x_7_8
#
# 「7-7」のコードを「やめる」と入力するまで何度でも繰り返し質問できるようにコードを追加してください

chatbot = {
    'おはよう': 'おはようございます',
    'おやすみ': 'おやすみなさい',
    '今日は何日ですか': '2021年11月14日です',
    '今日の天気は': '雨です',
    '何か歌って': 'もーもたろさんももたろさん',
}

while True:
    conversation = input('何か話しかけてください:')
    if conversation == 'やめる':
        break

    if conversation in chatbot:
        print(chatbot[conversation])
    else:
        print('わかりません')
