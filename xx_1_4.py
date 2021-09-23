# xx_1_4
#
# 「1-3」では関数を実行した結果を「result」という変数に代入しました。
# 関数を実行した際に関数から返って来る値を「戻り値（返り値）」と言い、「return」の後ろに値を置きます。
# 入力した内容を３回繰り返す「input_3」を定義してください。

def input_2(text):
    answer = input(text)
    return answer * 2


answer = input_2('あなたの名前を入力してください:')
print(answer)
