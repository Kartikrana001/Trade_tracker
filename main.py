while True:
    print("=====TRADE TRACKER=====\n\nADD TRADE        : 1\nVIEW TRADES      : 2\nEXIT             : 3")
    user_choice = input("Enter your choise: ")
    if user_choice == "1" :
        print("add trade")
    elif user_choice == "2":
        print("view trades ")
    elif user_choice == "3":
        break
    else:
        print("invelid choice")