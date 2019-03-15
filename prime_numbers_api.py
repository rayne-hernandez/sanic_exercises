import prime_number_functions as pf
from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route("/")
async def test(request):
    return json({"hello": "world"})

@app.route("/first_n_primes")
async def primes_handler(request):
    n = int(request.args["n"][0])
    primes = pf.first_n_primes(n)
    return json({"n": n, "primes": primes})

@app.route("/async_first_n_primes")
async def async_prime_handler(request):
    n = int(request.args["n"][0])
    primes = await pf.async_first_n_primes_1(n)
    return json({"n":n, "primes":primes})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
