import math
def is_prime(n):
    if n <= 1: return False
    elif n == 2: return True
    else: # for all other numbers, excluding even ones (except for the case of 2 itself) and greater than sqrt(number) to find divisors efficiently.
        b = int(math.sqrt(n)) + 1
        for i in range(2, b):  
            # print(n,i,b)
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
print("Non Prime numbers are", not_primes)
# print(is_prime(86982341))
# print(is_prime(25))

