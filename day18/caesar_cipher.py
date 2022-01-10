import string

if __name__ == '__main__':
    #user input
    text = input("Give a text. ")
    
    output = []
    cipher_text = []
    if len(text) >= 1:
        for item in text:
            cipher_text.append(ord(item)+ 4)

        for item in cipher_text:
            output.append(chr(item))
        print("".join(output))

    else:
        print("Give a text. ")
    