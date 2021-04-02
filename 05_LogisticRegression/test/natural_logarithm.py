n = 100000000
e = (1 + (1 / n)) ** n
print(e)


result = 10
for i in range(1, 10):
    result -= 1
    print(result)

    if(result == 0):
        print("Result is 0")
        break
