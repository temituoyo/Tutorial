def welcome():
    while True:
        message = input("Enter a greeting: ")
        try:
            if ((message == "Hi") or (message == "HI") or (message == "hi") or (message == "hI")):
                print("Hello World!")
            else:
                raise Exception
        except:
            print("Say hi")
        else:
            break

welcome()
