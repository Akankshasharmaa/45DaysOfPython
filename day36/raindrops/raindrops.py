"""Raindrops"""
def convert(number):
    """
    input: a number
    return: a string
    """
    sound = ""
    if number % 3 == 0:
        sound = "Pling"
    if number % 5 == 0:
        sound = sound + "Plang"
    if number % 7 == 0:
        sound = sound + "Plong"
    if sound == "":
        sound = str(number)
    return sound
