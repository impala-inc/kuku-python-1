# x_3_3
#
# ヒントを参考にq_1 ~ q_4がそれぞれどんな値となるかを予想してください

from module.qa import qa, ex

# ヒント

hint_1 = '桃太郎' == '桃太郎'
hint_2 = 'a' >= 'b'
hint_3 = '101' < '102'
hint_4 = '205' < '2000'
hint_5 = 'れんしゅう' in 'ぱいそんのれんしゅうもんだい'

# ここから問題

q_1 = '桃太郎' != 'うらしまたろう'
q_2 = 'かに' not in 'いぬさるきじ'
q_3 = 'aaab' < 'aabc'
q_4 = '1000' > '200'

# ここはとりあえず無視
for i in range(5):
    ex(f'hint_{i + 1}', locals()[f'hint_{i + 1}'])
for i in range(4):
    qa(f'q_{i + 1}', locals()[f'q_{i + 1}'])
