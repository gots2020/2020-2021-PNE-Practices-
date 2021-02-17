
def fibon(n):
    new_list = [0, 1]
    x = 0
    y = 1
    for i in range(1, n - 1):
        sum = x + y
        x = y
        y = sum
        new_list.append(sum)
    return new_list

print("The first 11 fibonacci numbers are : " , fibon(11))
print("The first 15 fibonacci numbers are : " , fibon(15))
