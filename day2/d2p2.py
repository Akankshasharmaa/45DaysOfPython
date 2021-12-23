def front_back(str):
    if len(str) <= 1:
        return str
    else:
        first_char = str[0]
        last_char = str[len(str) - 1]
        middle_str = ''
        for i in range(1,len(str) - 1):
            middle_str = middle_str + str[i]
        new_str = last_char + middle_str + first_char
        return new_str

new_str = front_back('code')
print(new_str)
new_str = front_back('a')
print(new_str)
new_str = front_back('ab')
print(new_str)