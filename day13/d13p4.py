def end_other(a, b):
    str_a = a.lower()
    str_b = b.lower()

    sub_str = ''

    if len(str_a) > len(str_b):
        for i in range(len(str_a) - len(str_b) + 1):
            sub_str = str_a[i : i + len(str_b)]

        if str_b == sub_str:
            return True
        else:
            return False
    else: 
        for i in range(len(str_b) - len(str_a) + 1):
            sub_str = str_b[i : i + len(str_a)]

        if str_a == sub_str:
            return True
        else:
            return False

result = end_other('abcab', 'ab')
print(result)
result = end_other('AbC', 'HiaBc')
print(result)
result = end_other('abc', 'abXabc')
print(result)