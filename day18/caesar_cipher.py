import string

if __name__ == '__main__':
    #user input
    text = input("Give a text. ")
    n = int(input("Move by "))
    # check if upper case letters (65- 90)
    password = []
    for item in text:
        if item.isupper():
            result = chr((((ord(item)+ n)-65)%26)+65)
            password.append(result)

        elif item.islower():
            result = chr((((ord(item)+ n)-97)%26)+97)
            password.append(result)


        else:
            password.append(item)
    print("".join(password))
    