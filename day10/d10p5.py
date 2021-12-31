def sorta_sum(a, b):
    sum = a + b
    if 10 <= sum <= 19:
        return 20
    else:
        return sum

result = sorta_sum(3, 4)
print(result)
result = sorta_sum(9, 4)
print(result)
result = sorta_sum(10, 11)
print(result)