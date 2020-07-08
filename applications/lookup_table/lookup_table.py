# Your code here
import math
import random
import time

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    cache = {}
    def slowfun_inner(x, y):
        v = math.pow(x,y)
        if v not in cache:            
            cache[v] = math.factorial(v)
            cache[v] //= (x + y)
            cache[v] %= 982451653
        v = cache[v]
        return v 
    return slowfun_inner(x, y)

fastcache = {}
def fastfun(x, y):
    v = math.pow(x,y)
    if v not in fastcache:            
        fastcache[v] = math.factorial(v)
        fastcache[v] //= (x + y)
        fastcache[v] %= 982451653
    v = fastcache[v]
    return v




# Do not modify below this line!
start = time.time()

for i in range(500000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {fastfun(x, y)}')

end = time.time()
print(f"Time elapsed: {end - start}:1f")
