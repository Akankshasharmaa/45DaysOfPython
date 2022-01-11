import math

def is_prime(n):
    for x in range(2, int(math.sqrt(n))):
        if n%x == 0:
            return False
    return True
        


result = is_prime(int(input()))
print(result)
