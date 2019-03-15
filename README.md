# Sanic Excercises
This repo contains Sanic exercises

Currently contains an API which returns the the first n prime numbers. To get
the API running on your local machine, do the following:

1. Run command `python prime_numbers_api.py`. Leave running in terminal
2. To get recursive computation of first n primes, make GET request to
`http://0.0.0.0:8000/first_n_primes?n={n_primes}`
3. To get asynchronous computation of first n primes, make GET request to
`http://0.0.0.0:8000/async_first_n_primes?n={n_primes}`
