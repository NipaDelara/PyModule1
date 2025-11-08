from math import isqrt
from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    elif n in (2,3):
        return True
    elif n % 2 == 0:
        return False
    r = isqrt(n)
    for d in range(3, r + 1, 2):
        if n % d == 0 :
            return  False
    return True

@app.get("/alkuluku/<int:n>")
def alkuluku(n: int):
    return jsonify({"Number": n, "isPrime": is_prime(n)})

app.run(host="127.0.0.1", port=3000, debug=True)
