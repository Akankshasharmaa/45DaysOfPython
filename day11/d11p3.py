def make_bricks(smallNum, bigNum, goal):
    if (bigNum * 5) + smallNum < goal:
        return False
    
    if goal % 5 > smallNum:
        return False

    return True



result = make_bricks(3, 1, 8) #true
print(result)
result = make_bricks(3, 1, 9) #false
print(result)
result = make_bricks(3, 2, 10) #true
print(result)
result = make_bricks(3, 2, 9) #false
print(result)
result = make_bricks(1, 4, 12) #false
print(result)
result = make_bricks(2, 1000000, 100003) #False
print(result)