def lone_sum(a, b, c):
    sum = a + b + c
    if a == b == c:
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return sum

result = lone_sum(1, 2, 3)
print(result)
result = lone_sum(3, 2, 3)
print(result)
result = lone_sum(3, 3, 3)
print(result)
