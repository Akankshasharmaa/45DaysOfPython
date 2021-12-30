def date_fashion(you, date):
    if 2 < you >= 8 or 2 < date >= 8:
        result = '2'
        return result
    elif  0 <= you <= 2 or 0 <= date <= 2:
        result = '0'
        return result
    else:
        result = '1'
        return result

result = date_fashion(5, 10)
print(result)
result = date_fashion(7, 3)
print(result)
result = date_fashion(5, 0)
print(result)