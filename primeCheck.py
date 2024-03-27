import math
def isPrime(num):
    for i in range(2, int(math.sqrt(num))):
        if num%i==0:
            return False
    return True

n = int(input("Enter a number: "))
print(isPrime(n))
