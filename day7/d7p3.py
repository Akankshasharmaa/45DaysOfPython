def extra_end(str):
    if len(str) >= 2:
        newstr = (str[len(str)-2] + str[len(str)-1]) * 3
        return newstr
    else:
        return False

result = extra_end('Hello')
print(result)
result = extra_end('ab')
print(result)
result = extra_end('')
print(result)