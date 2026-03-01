coin = ['HEADS', 'TAILS']
guest_money = 50
house_money = 49

while house_money and guest_money != 0:
    import random
    if random.choice(coin) == "TAILS":
        guest_money += 1
        house_money -= 1
        print("House Money Ksh", house_money)
        print("Guest Money Ksh", guest_money)
    else:
        guest_money -= 1
        house_money += 1
        print("House Money Ksh", house_money)
        print("Guest Money Ksh", guest_money)


if house_money > guest_money:
    print(f"House WINS!!! {house_money}")
else:
    print(f"Guest WINS!!! {guest_money}")
