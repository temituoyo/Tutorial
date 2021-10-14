def welcome():
    while True:
        message = input("Enter a greeting: ")
        message = message.upper()
        try:
            if ((message == "HI") or (message == "HI!")):
                print("Hello World!\n")
            else:
                raise Exception
        except:
            print("Say hi.\n")
        else:
            break

welcome()
