def makes10(a, b):
    if a == 10 or b == 10:
        return True
    elif a + b == 10:
        return True
    else:
        return False


result = makes10(9, 10)
print(result)
result = makes10(9, 9)
print(result)
result = makes10(10, 10)
print(result)