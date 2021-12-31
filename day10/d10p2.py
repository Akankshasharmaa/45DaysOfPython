def love6(a, b):
    if a == 6 or b == 6 or (a-b) == 6 or (b-a) == 6 or (a+b) == 6:
        return True
    else:
        return False

result = love6(6, 4)
print(result)
result = love6(4, 5)
print(result)
result = love6(1, 5)
print(result)