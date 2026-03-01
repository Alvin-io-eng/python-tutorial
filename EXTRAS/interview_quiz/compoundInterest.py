# principle = int(input("Principle? "))
# rate = int(input("Rate? "))
# time = int(input("Time? "))

# r = rate/100
# n = time
# p = principle
# ac = p*(1+r)**n
# ai = (p*r*n) + p

# print(f"Compound Interest is? {ac}\nSimple interest is? {ai}")

principle = int(input("Principle? "))
rate = float(input("Rate? "))
time = int(input("Time? "))

a = 0

r = rate/100
n = time
pc = principle
pi = principle

for i in range(10):
    
    ac = pc*(1+r)**n
    ai = (pi*r*n) + pi

    pc = ac + pc
    pi = ai + pi

    # a = a+1

print(f'Compound Interest: {ac}\nSimple Interest: {ai}')
