import random

number = random.randint(1,9)
if __name__ == '__main__':
    #user input
    n = int(input("Guess the number b/w 1-9... "))

    if 1<= n <= 9:
        if n == number:
            print(number)
            print("You're right!!")
        else:
            print(number)
            print("Opsi Dopsi")
    else:
        print("Give number b/w 1-9 only.")