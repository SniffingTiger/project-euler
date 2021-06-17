from largest_prime_factor import *
import random

class TestLargestPrimeFactor:
    def test_isPrime(self):
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        for number in prime_numbers:
            assert isPrime(number) == True

        for i in range(1, 11):
            assert isPrime(random.randrange(2, 100000, 2)) == False

    def test_isFactor(self):
        should_succeed = [[2, 4], [123, 615], [10, 1000], [11, 121]]
        for numbers in should_succeed:
            assert isFactor(numbers[0], numbers[1]) == True

        should_fail = [[3, 4], [5, 7], [11, 32], [11, 100], [100, 1001]]
        for numbers in should_fail:
            assert isFactor(numbers[0], numbers[1]) == False