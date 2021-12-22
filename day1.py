def diff21(n):
    if n <= 21:
        return (21 - n)

    elif n > 21:
        return 2 * (n - 21)


mydif = diff21(19)
print(mydif)

mydif = diff21(10)
print(mydif)

mydif = diff21(21)
print(mydif)

mydif = diff21(23)
print(mydif)