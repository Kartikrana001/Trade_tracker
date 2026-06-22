trades = []
def add_trade():
    stock = input("Enter stock name: ").strip()
    buy_price = float(input("Enter buy price: "))
    trades.append({"stock":stock,"buy_price":buy_price})
def view_trades():
    for trade in trades:
        print(trade["stock"],"-",trade["buy_price"])
while True:
    print("=====TRADE TRACKER=====\n\nADD TRADE        : 1\nVIEW TRADES      : 2\nEXIT             : 3")
    user_choice = input("Enter your choise: ")
    if user_choice == "1" :
        add_trade()
    elif user_choice == "2":
        view_trades()
    elif user_choice == "3":
        break
    else:
        print("invelid choice")