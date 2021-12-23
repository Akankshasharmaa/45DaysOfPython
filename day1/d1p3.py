def near_hundred(n):
    if 90 <= n <=110 or 190 <= n <= 210:
        return True
    else:
        return False  



result = near_hundred(93)
print(result)
result = near_hundred(90)
print(result)
result = near_hundred(89)
print(result)

result = near_hundred(190)
print(result)

result = near_hundred(210)
print(result)

result = near_hundred(211)
print(result)
