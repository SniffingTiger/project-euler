# https://projecteuler.net/problem=3

# -----
# Problem:
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
# -----

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

    # Fractional numbers can never be prime
    if not number.is_integer():
        return False

    # If number is one through three, return True because they are prime numbers
    if (number > 0 and number < 4):
        return True

    # if (number % 2 == 0):
    #     return False

    # # If number is divisible by anything between 2 and the largest whole number
    # # up to its true half, then the number is divisible by more than just one 
    # # and itsef, so return False
    # for x in range(2, int(number / 2)):
    #     if isFactor(x, number):
    #         return False
    # return True

    if number - 1 % 6 == 0:
        return True
    elif number + 1 % 6 == 0:
        return True
    else:
        return False

number = 600851475143
divisor = 2
result = 0

while (number / 2) > divisor:
    result = number / divisor
    if not result.is_integer():
        divisor += 1
        continue
    if isPrime(result):
        break
    divisor += 1

print(result)