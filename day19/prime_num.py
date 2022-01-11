import math

def is_prime(n):
    if n < 2:
        return False
    for x in range(2, int(math.sqrt(n))+ 1):
        if n%x == 0:
            return False
    return True

result = is_prime(int(input()))
print(result)
