

N, T, K = map(int,input().split())

deck={}
prices=[]

tmp = map(int, input().split())

for card in tmp:
    count = deck.get(card,0)
    count += 1
    deck[card] = count

for i in range(T):
    buy_price, sell_price = map(int, input().split())
    n = deck.get(i+1,0)
    buy = (2-n) * buy_price
    sell = n * sell_price
    prices.append((buy+sell, buy, sell))

prices.sort(key = lambda x: x[0])

cost = 0
for i in range(K):
    cost-= prices[i][1]

for i in range(K,T):
    cost+= prices[i][2]

print(cost)



'''
i = [int(x) for x in input().split()]
N = i[0]
T = i[1]
K = i[2]

n_cards={}
cardvalues=[]

for c in input().split():
    x = int(c)
    if x in n_cards:
        n_cards[x] += 1
    else:
        n_cards[x] = 1

for i in range(0,T):
    line = [int(x) for x in input().split()]
    n = n_cards.get(i+1,0)
    buy = (2-n)*line[0]
    sell = n*line[1]
    cardvalues.append([buy+sell,buy,sell])

cardvalues.sort(key = lambda x: x[0])

total=0
for i in range(0,K):
    total-= cardvalues[i][1]
for i in range(K,T):
    total+= cardvalues[i][2]

print(total)



N, T, K = map(int,input().split())
#deck_list = map(int,input().split())



buy_sell = []
for i in range(T):
    buy_price, sell_price = map(int, input().split())
    buy_sell.append((buy_price, sell_price))

#sorted_prices = sorted(buy_sell, key=lambda x: x[0])
#print(buy_sell)
#print(sorted_prices)

#print(sorted_prices)
# Transactions
# Buy up to two cards of a type
# Sell all cards of a type
kombos = 0
deck = {}
value = 0
for i in deck_list:
    count = deck.get(i,0)
    count += 1
    deck[i] = count
    if count >= K:
        kombos += 1

potential_per_transaction = []
for i, e in deck.items():
    buy, sell = buy_sell[i-1]
    potential_per_transaction.append((i, buy*e, sell*e))


#print(potential_per_transaction.sort(lambda x: x[2]))


'''