
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

def sumn(list1):
    sum = 0
    for i in range(0, len(list1)):
        sum += int(list1[i])
    return sum

print("The first 11 fibonacci numbers are : " , fibon(11))
print("The sum of the first 5 fibon numbers is : " , sumn(fibon(5)))
