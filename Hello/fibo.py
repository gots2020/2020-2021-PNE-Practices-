
def fibon(n):
    x = 0
    y = 1
    for i in range(1, n):
        sum = x + y
        x = y
        y = sum
    return sum

print("The sum of the first 10 fibonacci numbers is : " , fibon(10))
