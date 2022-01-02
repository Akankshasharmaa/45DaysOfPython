def lucky_sum(a, b, c):
    sum = a + b + c
    if a == 13:
        return 0
    elif b == 13:
        return a
    elif c == 13:
        return a+b
    else:
        return sum


result = lucky_sum(1, 2, 3)
print(result)
result = lucky_sum(1, 2, 13)
print(result)
result = lucky_sum(1, 13, 3)
print(result)