def front3(str):
    newStr = ''
    first_three_char = ''
    if len(str) <= 3:
        newStr = str + str + str
        return newStr
    elif len(str) > 3:
        first_three_char = str[0] + str[1] + str[2]
        newStr = first_three_char + first_three_char + first_three_char
        return newStr

result = front3('abc')
print(result)
result = front3('Java')
print(result)
result = front3('Chocolate')
print(result)