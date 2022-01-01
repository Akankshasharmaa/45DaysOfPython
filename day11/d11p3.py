def make_bricks(smallNum, bigNum, goal):
    small_brick = 1 
    big_brick = 5
    if (smallNum * small_brick) + (bigNum * big_brick) >= goal:
        return True
    else:
        return False 

result = make_bricks(3, 1, 8)
print(result)
result = make_bricks(3, 1, 9)
print(result)
result = make_bricks(3, 2, 10)
print(result)