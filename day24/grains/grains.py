"""
The functions are calculating the number of grains of wheat on a chessboard given that the number
on each square doubles.
"""
def square(number):
    # constraint for chessboard square number
    if 1 <= number <= 64:
        return 2 ** (number-1)
    else:
        raise ValueError("square must be between 1 and 64")

def total():
    # Initialising a variable
    mysum = 0
    for i in range(64):
        mysum += (2 ** i)
    return mysum

