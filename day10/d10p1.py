def squirrel_play(temperature, is_summer):
# The squirrels in Palo Alto spend most of the day 
# playing. In particular, they play if the temperature 
# is between 60 and 90 (inclusive). Unless it is summer, 
# then the upper limit is 100 instead of 90. Given an 
# int temperature and a boolean is_summer, return True
# if the squirrels play and False otherwise.
    if is_summer == False and 60 <= temperature <= 90:
        return True
    elif is_summer == True and 60 <= temperature <= 100:
        return True
    else:
        return False

result = squirrel_play(70, False)
print(result)
result = squirrel_play(95, False)
print(result)
result = squirrel_play(95, True)
print(result)
