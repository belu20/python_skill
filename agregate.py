def aggregate(message, numbers, f):
    res = f(numbers)
    print(f"{message} is {res}")

def sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def avg(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

aggregate("total", [24, 67, 22, 98, 3, 50], sum)
# output ➜ total is 264

aggregate("average", [24, 67, 22, 98, 3, 50], avg)
# output ➜ average is 44.0

aggregate("max number", [24, 67, 22, 98, 3, 50], max)
# output ➜ max number is 98

aggregate("min number", [24, 67, 22, 98, 3, 50], min)
# output ➜ min number is 3