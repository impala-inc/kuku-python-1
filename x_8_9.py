# x_8_9
#
# 「cards」を「while文」と「random」を使ってランダムに並び替えてください

cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

print(cards)

cards[2], cards[11] = cards[11], cards[2]  # cards[2]とcards[11]の要素を交換

print(cards)
