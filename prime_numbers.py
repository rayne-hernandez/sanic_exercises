
import sys
from sanic import Sanic
from sanic.response import text


def is_prime_helper(n, previous_primes):
    for prime in previous_primes:
        if n % prime == 0:
            return False
    return True

def first_n_primes(n):
    if n == 1:
        return [2]
    primes = first_n_primes(n - 1)
    next_prime = max(primes) + 1
    while True:
        if is_prime_helper(next_prime, primes):
            primes.append(next_prime)
            return primes
        next_prime += 1

correct_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, \
    53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, \
    137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, \
    223, 227, 229]

pred_primes = first_n_primes(50)

test_passed = (correct_primes == pred_primes)

print("First 50 primes are: {}".format(correct_primes))
print("Calculated first 50 primes are: {}".format(pred_primes))
print("Are these lists the same?: {}".format(str(test_passed)))
