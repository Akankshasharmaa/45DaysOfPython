def no_teen_sum(a, b, c):
    new_a = fix_teen(a)
    new_b = fix_teen(b)
    new_c = fix_teen(c)

    mysum = new_a + new_b + new_c
    return mysum

def fix_teen(n):
    if n == 15 or n == 16:
        return n
    elif 13 <= n <= 19:
        n = 0
        return n
    else:
        return n

result = no_teen_sum(1, 2, 3)
print(result)
result = no_teen_sum(2, 13, 1)
print(result)
result = no_teen_sum(2, 1, 14)
print(result)