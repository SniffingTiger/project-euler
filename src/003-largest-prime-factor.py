# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?

# Function to determine if a number is a factor of a number
def isFactor(potentialFactor, number):
    if (potentialFactor == 0 or number == 0):
        raise ZeroDivisionError
    if (number % potentialFactor == 0):
        return True
    else:
        return False

# Function to determine if a number is prime
def isPrime(number):
    # If number is zero, throw an exception (Zero cannot be a prime number)
    if (number == 0):
        print("0 [Zero] cannot be a prime number")
        raise ZeroDivisionError
    # If number is one, return True because one is a prime number
    if (number == 1):
        return True
    if (isinstance(number, float)):
        # If number is divisible by anything between 2 and the largest whole number up to its true half, then the number is divisible by more than just one and itsef, so return False
        for x in range(float(2), number / float(2)):
            if isFactor(x, number):
                return False
    else:
        for x in range(2, number / 2): # If number is divisible by anything between 2 and the largest whole number up to its true half, then the number is divisible by more than just one and itsef, so return False
            if isFactor(x, number):
                return False
    return True # If the above loop finishes without 

# Declare result variable
result = 0

# for loop
for x in range(1, 600851475143):
    if (isFactor(x, 600851475143) and isPrime(x)):
        result = x

print(x)