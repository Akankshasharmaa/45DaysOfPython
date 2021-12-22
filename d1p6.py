def sum_double(n, m):
    sum = (n+m)
    if n == m:
        return 2 * sum
    else:
        return sum
    



result = sum_double(1, 2)
print(result)
result = sum_double(3, 2)
print(result)
result = sum_double(2, 2)
print(result)
