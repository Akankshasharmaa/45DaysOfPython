def make_bricks(smallNum, bigNum, goal):
    small_brick = 1 * smallNum
    big_brick = 5 * bigNum
    if goal % big_brick == 0:
        return True
    elif goal % big_brick == small_brick:
        return True
    else:
        return False

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