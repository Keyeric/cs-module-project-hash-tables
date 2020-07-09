import time
"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

def sumdiff(numbers):
    numbers = list(numbers)
    plus = {}
    minus = {}

    for i in range(len(numbers)):
        # for loop that goes from 0 to whatever the end is (10, 200, 5) so that we can have i
        for j in range(len(numbers)):
            # for loop that goes from 0 to whatever the end is (10, 200, 5) so that we can have j
            plus_key = (numbers[i], numbers[j]) #1,1 1,2 etc
            # print(f"Plus Key: {plus_key}")
            plus_value = f(numbers[i]) + f(numbers[j])  #1+1 1+2 etc
            # print(f"Plus Value: {plus_value}")
            plus[plus_key] = plus_value  #add our key to the dict
            # print(f"Plus: {plus[plus_key]}\n") #Just to show you the value is the same, its just adding to dict
            
            # Do the same thing you did for plus but for minus
            minus_key = f(numbers[i]) - f(numbers[j])
            # print(f"Minus Key: {plus_key}")
            minus_value = (numbers[i], numbers[j])
            # print(f"Minus Value: {plus_value}")
            minus[minus_key] = minus_value
            # print(f"Minus: {minus[minus_key]}\n")

            

    for (key, value) in plus.items():
        # print(f"Key Value Pair:\n {key} \n{value}\n") #The Key is the two number thats created the Value (1,1 made 20, etc)
        if minus.__contains__(value):
            # if the minus dict has the same value as plus dict
            minus_tuple = minus[value]
            # assign it and print it
            print(f"f({key[0]}) + f({key[1]}) = f({minus_tuple[0]}) - f({minus_tuple[1]})  ***  {f(key[0])} + {f(key[1])} = {f(minus_tuple[0])} - {f(minus_tuple[1])}")     


 



start_time1 = time.time()
sumdiff(q)
end_time1 = time.time()

print(f"Time Elapsed: {end_time1 - start_time1}")