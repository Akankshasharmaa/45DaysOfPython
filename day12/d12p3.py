def close_far(a, b, c):
    if ((b + 1) == a or (b-1) == a) and ((c+2) == a or (c-2) == a):
        return False
    elif ((b + 2) == a or (b-2) == a) and ((c+1) == a or (c-1) == a):
        return False
    else:
        return True

result = close_far(1, 2, 10)
print(result)
result = close_far(1, 2, 3)
print(result)
result = close_far(4, 1, 3)
print(result)