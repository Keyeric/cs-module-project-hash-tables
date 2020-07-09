import time

cache = {}
# global cache
def expensive_seq(x, y, z):
    if (x, y, z) not in cache:
    # if the 3 variables passed in are not in the cache
        if x <= 0:
        # and the x variable is zero or lower (negative numbers)
            cache[(x, y, z)] = y + z
            # add these 3 numbers to the cache as a singular number which is y+z in this case
        else:
        # or if the x variable is a positive non-zero number
            cache[(x, y, z)] = expensive_seq(x - 1, y + 1, z) + expensive_seq(x - 2, y + 2, z * 2) + expensive_seq(x - 3, y + 3, z * 3)
            # add these three variables together using this recursive math as a singlular number
        
    return cache[(x, y, z)]
    # return the singular number given through any of these statements


if __name__ == "__main__":
    start = time.time()

    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i}: {i*2} {i*3} {i*4} = {x}")
        end = time.time()


    print(expensive_seq(150, 400, 800))
    print(f"Time elapsed: {end - start}")
