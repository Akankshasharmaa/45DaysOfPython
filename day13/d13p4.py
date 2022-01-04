def end_other(a, b):
    str_a = a.lower()
    str_b = b.lower()

    i = len(str_a)
    j = len(str_b)

    if i >= 3 and j >= 3:
        if str_a[i-1] == str_b[j-1] and str_a[i-2] == str_b[j-2] and str_a[i-3] == str_b[j-3]:
            return True
        else:
            return False


result = end_other('Hiabc', 'abc')
print(result)
result = end_other('AbC', 'HiaBc')
print(result)
result = end_other('abc', 'abXabc')
print(result)