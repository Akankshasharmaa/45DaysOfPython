def front_times(str, n):
    newstr = ''
    if n >= 0:
        if len(str) <= 3:
            return str * n
        elif len(str) > 3:
            newstr = str[0] + str[1] + str[2]
            return newstr * n

result = front_times('Chocolate', 2)
print(result)
result = front_times('Chocolate', 3)
print(result)
result = front_times('', 3)
print(result)