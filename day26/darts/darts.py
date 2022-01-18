def score(x, y):
    point = 0
    if 0 < x <= 1 or 0 < y <= 1:
        point = 10
    if 1 <x <= 5 or 1 < y <= 5:
        point = 5
    if 5 < x <= 10 or 5 < y <= 10:
        point = 1
    else:
        point = 0
    return point
    

 