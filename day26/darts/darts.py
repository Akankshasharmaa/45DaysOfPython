""" Dart problem """
def score(x, y):
    point = 0
    if (x*x) + (y*y) <= 1*1:
        point = 10
    elif (x*x) + (y*y) <= 5*5:
        point = 5
    elif (x*x) + (y*y) <= 10*10:
        point = 1
    else:
        point = 0
    return point