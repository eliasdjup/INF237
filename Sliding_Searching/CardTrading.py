

from collections import Counter

def kcombo(cardDeck):
    counterz = Counter(cardDeck)
    # TODO
    #check if there are at least 2 values for k distinct
    #card
    return False

deck, cards, combos = [int(i) for i in input().split()]

cardDeck = [int(i) for i in input().split()]
print(cardDeck)

cardSellBuy = []
for x in range(0, cards):
    buy, sell = [int(i) for i in input().split()]

    cardSellBuy.append((buy,sell))

print(" maxSell {} cardSell {} minBuy {} cardBuy {}".format(maxSell, cardSell, minBuy, cardBuy))

combo = False
money = 0
maxMoney = 0
while (not combo): #while combo is not reached
    for i in cardSellBuy:
        money -= cardSellBuy[i][1]
        cardDeck.remove(i+1)    

    combo = kcombo(cardDeck)