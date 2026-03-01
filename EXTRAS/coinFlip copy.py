coin = ["Heads","Tails"]
# play prompt
play = str(input("Would you like to play(y/n): "))
house_money = 100


if play.lower() == 'y':
    play = True
    account_balance = int(input("Enter Amount: "))
elif play.lower() == 'n':
    play = False
    account_balance = 0
    print("Nice meeting you sucker")
else: 
    play = False
    print("Invalid input")


import random

while play:
    # check account_balance
    if account_balance == 0:
        print(f"You cannot play with no money: Ksh {account_balance}")
        play = False
        break
    
    # random choice of ('Heads' & 'Tails') adding +1 if Heads minus -1 if Tails
    if random.choice(coin) == 'Heads':
        account_balance += 1
        house_money -= 1
        print(f"Your balance now is: Ksh {account_balance} & house money: Ksh {house_money}")
    else:
        account_balance -= 1
        house_money += 1
        print(f"Your balance now is: Ksh {account_balance} & house money: Ksh {house_money}")
        # return account_balance
    
    continuePlaying  = str(input("Would you like to placebet again (y/n): "))

    if continuePlaying.lower() == 'y':
        play = True
    elif continuePlaying.lower() == 'n':
        play = False
    else: 
        print("Invalid Input we'll continue by default")

print(f"You can with draw: Ksh {account_balance} & house: Ksh {house_money}")


