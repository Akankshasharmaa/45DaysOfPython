def double_char(str):
    newstr = ''

    for i in range(len(str)):
        newstr = newstr + (str[i] * 2)
    return newstr 

result = double_char('The')
print(result)
result = double_char('AAbb')
print(result)
result = double_char('Hi-There')
print(result)