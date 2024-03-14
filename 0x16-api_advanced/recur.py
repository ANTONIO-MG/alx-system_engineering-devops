def recursion(num):
    if  num == 0 or num == 1:
        return 1
    else:
        num -= recursion(num)
        return num

print(recursion(10))