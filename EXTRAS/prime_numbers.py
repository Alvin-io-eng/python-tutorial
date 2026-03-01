# GEMINI

def get_primes_to_100():
    primes = []
    for num in range(2,101):
        is_prime = True
        for i in range(2,int(num**0.5+1)):
            if num % i == 0:
              is_prime = False
              break
            if is_prime:
                primes.append(num)
    return primes

# print(f"Primes 1-100: {get_primes_to_100()}")

# numbers = []

# for i in range(2,101):
#     numbers.append(i)

# # print(numbers)
# # print(int(2**1.5))

# base_divisors = [2,3,5,7]
# prime_numbers = []
# not_primes = []

# for number in range(2,21):
#         is_prime = True
#         for divisor in base_divisors:
#             if number % divisor == 0:
#                 if number != divisor:
#                     # is_prime = False
#                     numberXdivisor = {"number":number,"divisor":divisor}
#                     print(f"NOTPRIME: {numberXdivisor}")
#                     not_primes.append(number)
#                     break
#             else:
#                 # is_prime = True
#                 numberXdivisor = {"number":number,"divisor":divisor}
#                 print(f"PRIME: {numberXdivisor}")
#                 prime_numbers.append(number)

# print(f"PRIMES: {prime_numbers}")
# print(f"NOT PRIMES: {not_primes}")

# OUTPUT
# alvin@alvin-HP-ProBook-430-G3:~/Desktop/Programming Languages/Python$ python3 -u "/home/alvin/Desktop/Programming Languages/Python/EXTRAS/prime_numbers.py"
# PRIME: {'number': 2, 'divisor': 3}
# PRIME: {'number': 2, 'divisor': 5}
# PRIME: {'number': 2, 'divisor': 7}
# PRIME: {'number': 3, 'divisor': 2}
# PRIME: {'number': 3, 'divisor': 5}
# PRIME: {'number': 3, 'divisor': 7}
# NOTPRIME: {'number': 4, 'divisor': 2}
# PRIME: {'number': 5, 'divisor': 2}
# PRIME: {'number': 5, 'divisor': 3}
# PRIME: {'number': 5, 'divisor': 7}
# NOTPRIME: {'number': 6, 'divisor': 2}
# PRIME: {'number': 7, 'divisor': 2}
# PRIME: {'number': 7, 'divisor': 3}
# PRIME: {'number': 7, 'divisor': 5}
# NOTPRIME: {'number': 8, 'divisor': 2}
# PRIME: {'number': 9, 'divisor': 2}
# NOTPRIME: {'number': 9, 'divisor': 3}
# NOTPRIME: {'number': 10, 'divisor': 2}
# PRIME: {'number': 11, 'divisor': 2}
# PRIME: {'number': 11, 'divisor': 3}
# PRIME: {'number': 11, 'divisor': 5}
# PRIME: {'number': 11, 'divisor': 7}
# NOTPRIME: {'number': 12, 'divisor': 2}
# PRIME: {'number': 13, 'divisor': 2}
# PRIME: {'number': 13, 'divisor': 3}
# PRIME: {'number': 13, 'divisor': 5}
# PRIME: {'number': 13, 'divisor': 7}
# NOTPRIME: {'number': 14, 'divisor': 2}
# PRIME: {'number': 15, 'divisor': 2}
# NOTPRIME: {'number': 15, 'divisor': 3}
# NOTPRIME: {'number': 16, 'divisor': 2}
# PRIME: {'number': 17, 'divisor': 2}
# PRIME: {'number': 17, 'divisor': 3}
# PRIME: {'number': 17, 'divisor': 5}
# PRIME: {'number': 17, 'divisor': 7}
# NOTPRIME: {'number': 18, 'divisor': 2}
# PRIME: {'number': 19, 'divisor': 2}
# PRIME: {'number': 19, 'divisor': 3}
# PRIME: {'number': 19, 'divisor': 5}
# PRIME: {'number': 19, 'divisor': 7}
# NOTPRIME: {'number': 20, 'divisor': 2}
# PRIMES: [2, 2, 2, 3, 3, 3, 5, 5, 5, 7, 7, 7, 9, 11, 11, 11, 11, 13, 13, 13, 13, 15, 17, 17, 17, 17, 19, 19, 19, 19]
# NOT PRIMES: [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
# PRIME: {'number': 2, 'divisor': 3}


# def get_prime_numbers():
#     for number in range(2,21):
#         is_prime = True
#         for divisor in base_divisors:
#             if number % divisor == 0:
#                 if number != divisor:
#                     # is_prime = False
#                     numberXdivisor = {"number":number,"divisor":divisor}
#                     not_primes.append(number)
#                     break
#             else:
#                 # is_prime = True
#                 numberXdivisor = {"number":number,"divisor":divisor}
#                 prime_numbers.append(number)

#     return f"PRIME NUMBERS: {prime_numbers}", f"NOT PRIMES: {not_primes}"

# print(get_prime_numbers())

# for number in range(2,21):
#         is_prime = True
#         for divisor in base_divisors:
#             if number % divisor == 0:
#                 if number != divisor:
#                     # is_prime = False
#                     numberXdivisor = {"number":number,"divisor":divisor}
#                     print(f"NOTPRIME: {numberXdivisor}")
#                     not_primes.append(number)
#                     break
#                 else:
#                     continue
#             else:
#                 # is_prime = True
#                 numberXdivisor = {"number":number,"divisor":divisor}
#                 print(f"PRIME: {numberXdivisor}")
#                 prime_numbers.append(number)



import math
def is_prime(n):
    if n <= 1: return False
    elif n == 2: return True
    else: # for all other numbers, excluding even ones (except for the case of 2 itself) and greater than sqrt(number) to find divisors efficiently.
        for i in range(2, int(math.sqrt(n)) + 1):  
            if n % i == 0: return False, i # Early stop condition when a factor is found - not necessary but can improve performance slightly on larger ranges of input (but omitted here to keep code cleaner).
        return True 
    
prime_numbers = []
not_primes = []
for number in range(1, 100):  
    if is_prime(number): # calling our improved function for primality check.        
        prime_numbers.append(number)
    else: 
        not_primes.append(number)     

print("Prime numbers are", prime_numbers)    
# # for number in sorted(prime_numbers):  
# #     print(number, end=" ", flush=True) # for readability and to follow your output format closely (but this was already present). 
# # print()            
# print("Non-primes: " + str(not_primes))

# for i in range(1,20):
#     print(i)

# print(is_prime(473))

# abs1 = int(math.sqrt(5)+1)
# abs2 = int(5**0.5+1)
# print(abs1, abs2)

"""
why in when checking for a prime number in the is_prime() function we use the range from 2 to the square root of number + 1 whyis it specifically from the square root then we add one why no
... t any other root or not add one help me understand this part
The reason behind using only up to and including `sqrt(n) + 1` for checking primality has a few key advantages, which I'll explain below:

**Optimization in Primality Testing:** When determining if a number is prime (especially within the context of generating primes rather than testing specific numbers), we often use 
divisibility rules. Since every non-prime greater than 1 can be factored into two positive integers that are both less or equal to its square root, this becomes our efficient search limit 
for factors other than one and itself - effectively reducing unnecessary computation once you find a factor below the number's halfway point in terms of value (its square root).

**Mathematical Justification:** Suppose n is non-prime; then it must have divisors d1, d2 such that `d1 * d2 = n`. Without loss of generality assuming they are both less than or equal to 
sqrt(n) because if either were greater, their product would exceed the original number (as one divider can be larger and having an extra √ could compound this effect). Thus we don't need 
to check beyond √(n), as any divisors found before that point will have corresponding partners after.

**Practical Implementation:** In many programming languages, generating a list of numbers from sqrt(n) +1 ensures inclusivity—meaning if `n` is an integer square (perfect squares like 
4,9), it won't miss considering these cases as they would only have one divisor pair - themselves and itself.

**Efficiency in Code:** By adding one to the square root when using programming language functions that typically exclude the endpoint from their range methods or arrays (like Python’s 
`range`), we ensure checking of sqrt(n) if n is a perfect square, which might otherwise be missed due to integer casting issues. 

In essence, this logic ensures no needless checks beyond what's required for primality tests and it provides efficiency in both time (fewer computations) and space (a smaller loop range 
or iteration count). This is not about any particular root but rather a very effective method that balances between completeness of testing without overshooting the bounds necessary to 
conclude if something is prime. It's quite elegant because it cuts down on time complexity for larger numbers significantly, which in turn keeps your code running faster and more 
efficiently—key aspects when generating large sets like primes or handling big data problems where such optimizations are crucial.

I hope this provides a clear understanding of why we use `sqrt(n) + 1` specifically! Always remember that algorithms often involve trade-offs, but in primality checking and prime 
generation, time complexity is typically reduced using square root methods due to the way multiplication works for non-primes.


"""