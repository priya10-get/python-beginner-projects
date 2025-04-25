print("Hai, Welcome to my world.Type'bye' to exit.\n")
while True:
    user_input=input("you:").lower()
    if user_input=="hai":
        print("welcome to my world")
    elif user_input=="how are you doing?":
        print("I am doing good")
    elif user_input=="bye":
        print("Take care")
        break
    else:
        print("good bye")
