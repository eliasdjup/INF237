
N, T, K = map(int,input().split())
deck_list = map(int,input().split())

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

