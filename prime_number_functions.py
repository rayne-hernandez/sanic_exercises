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
