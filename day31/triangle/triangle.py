"""Functions to check triangle equality and inequality"""
def triangle_inequality(sides):
    if sides[0] > 0 and sides[1] > 0 and sides[2] > 0:
        if sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
            return True
    return False

def equilateral(sides):
    check = triangle_inequality(sides)
    if check:
        if sides[0] == sides[1] == sides[2]:
            return True
    return False

def isosceles(sides):
    check = triangle_inequality(sides)
    if check:
        if sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]:
            return True
    return False

def scalene(sides):
    check = triangle_inequality(sides)
    if check:
        if sides[0] != sides[1] != sides[2]:
            return True
    return False
