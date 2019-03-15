import prime_number_functions as pf
from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route("/"  )
async def test(request):
    return json({"hello": "world"})

@app.route("/first_n_primes")
def primes_handler(request):
    n = int(request.args["n"][0])
    primes = pf.first_n_primes(n)
    return json({"n": n, "primes": primes})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
