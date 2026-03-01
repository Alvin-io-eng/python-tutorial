def main():

    # prompt to enter variables
    # variables()

    # enter no of possibilities
    # possibilities = int(input("Enter number of possibilities youl'd like to see: "))

    # account balaces returned from each function

    account_balance = playcoinFlip1()
    # account_balance = playcoinFlip2(possibilities)

    return account_balance

def variables():
    # our coin with heads / Tails
    coin = ["Heads","Tails"]
    # play prompt
    play = str(input("Would you like to play(y/n): "))

    import random 

    if play.lower() == 'y':
        play = True
        account_balance = int(input("Enter Amount: "))
    elif play.lower() == 'n':
        play = False
        print("Nice meeting you sucker",play)
    else: 
        play = False
        print("Invalid input")

    return coin, play, account_balance


# for heads is +1 while tails is -1
def playcoinFlip1():
    values = variables()
    coin = values[0]
    play = values[1]
    account_balance = values[2]

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
            # # print(f"Your balance now is: Ksh {account_balance}")
            # return account_balance
            continue
        else:
            account_balance -= 1
            # print(f"Your balance now is: Ksh {account_balance}")
            # return account_balance
    
        continuePlaying  = str(input("Would you like to placebet again (y/n): "))

        if continuePlaying.lower() == 'y':
            play = True
        elif continuePlaying.lower() == 'n':
            play = False
        else: 
            print("Invalid Input we'll continue by default")
            return account_balance

        


def playcoinFlip2(possibilities):
    values = variables()
    coin = values[0]
    # play = values[1]
    account_balance = values[2]

    import random

    for possibility in range(1,possibilities+1):
        if random.choice(coin) == 'Heads':
            account_balance += 1
        else:
            account_balance -= 1

        possibility += 1



    return account_balance


def playcoinFlip3():
    # This time if Heads it (1 * 1.1) if Tails (1 * 0.9)
    return None

def playcoinFlip4():
    # This time the payout double each time you toss a coin
    """
    if you get head in the first toss you get 1*2 = ksh 2.00 
    but if you flip 8 imes is when you get a heads payout is 1 * 2^8 
    if you get a heads game stops and you withdraw payout

    """
    return None

if __name__ == "__main__":
    print(main())