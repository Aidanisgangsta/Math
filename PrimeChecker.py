import math
import time

primes = []

number = int(input("What number would you like to check to?: "))

start = time.time()
maxtest = int(math.sqrt(number))

def primecheck(num):
    if num == 1:
        return False
    elif num == 3 or num == 2:
        return True
    elif num % 2 == 0:
        return False
    elif (num + 1) % 6 == 0 or (num -1) % 6 == 0:
        for i in range(3, maxtest):
            if num % i == 0:
                return False
        return True
    else:
        return False

for n in range(1, number):
    isprime = primecheck(n)
    if isprime == True:
        primes.append(n)

print(primes)

print(f"Time take was {time.time()-start}")