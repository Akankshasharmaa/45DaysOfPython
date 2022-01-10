import random

number = random.randint(1,9)
if __name__ == '__main__':
    #user input
    while True:
        n = int(input("Guess the number b/w 1-9... "))
        if 1<= n <= 9:
            if n == number:
                print("You're right!!")
                break
            elif n < number:
                print("Too low")
            else:
                print("Too high")
        else:
            print("Give number b/w 1-9 only.")