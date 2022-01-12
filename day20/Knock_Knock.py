import random
reply = {
    "Tank": "You're Welcome",
    "Luke": "Luke through the peephole and find out",
    "Figs": "Figs the doorbell, it’s not working!",
    "Cow says": "No, a cow says Mooooo",
    "Alice": "Alice fair in love and war",
    "Says": "Says me!",
    "Hawaii": "I'm good. Hawai are you?",
    "Woo": "Glad you're excited too!"
}
while True:
    print("Knock Knock")
    user_input = input()

    if user_input == "exit()":
        break

    hi = list(reply.keys())
    hello = random.choice(hi)
    print(hello)

    user_reply = input()
    mykey = user_reply.split()

    for item in reply:
        if mykey[0] == item:
            print(reply[item])
    
    
