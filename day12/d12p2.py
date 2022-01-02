def make_chocolate(smallNum, bigNum, goal):
    bigsize = 5
    if (bigNum * 5) + smallNum < goal:
        return -1

    if goal % bigsize > smallNum:
        return -1
    
    smallused = goal - (bigNum * bigsize)
    return smallused

result = make_chocolate(4, 1, 9)
print(result)
result = make_chocolate(4, 1, 10)
print(result)
result = make_chocolate(4, 1, 7)
print(result)