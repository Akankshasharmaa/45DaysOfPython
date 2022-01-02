def round_sum(a, b, c):
    round_a = round10(a)
    round_b = round10(b)
    round_c = round10(c)

    round_sum = round_a + round_b + round_c
    return round_sum

def round10(num):
    if num % 10 >= 5:
        num = num + (10 - (num%10))
        return num
    elif num % 10 < 5:
        num = num - (num%10)
        return num

result = round_sum(16, 17, 18)
print(result)
result = round_sum(12, 13, 14)
print(result)
result = round_sum(6, 4, 4)
print(result)