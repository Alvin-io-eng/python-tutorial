from random import choice, randint, shuffle

# import random
# coin = random.choice(["Heads","Tails"])

coin = choice(["Heads","Tails"])
print(coin)

number = randint(1,10)
print(number)

cards = ["JACK","QUEEN","KING"]
shuffle(cards)
print(cards)
for card in cards:
    print(card)