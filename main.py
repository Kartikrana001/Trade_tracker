trades = []
try:
    with open("trades.txt","r") as file:
        lines = file.readlines()
    for line in lines:
        stock,buy_price,sell_price,quantity = line.strip().split(",")
        trades.append({"stock": stock,"buy_price": float(buy_price),"sell_price": float(sell_price),"quantity":float(quantity)})
except FileNotFoundError:
    print("No previous data found...")
def add_trade():
    stock = input("Enter stock name: ").strip()
    try:
        buy_price = float(input("Enter buy price: "))
        sell_price = float(input("Enter sell price: "))
        quantity = int(input("Enter the quantity: "))
    except ValueError as v:
        print("invalid input...")
        return
    trades.append({"stock":stock,"buy_price":buy_price,"sell_price":sell_price,"quantity":quantity})
    with open("trades.txt","a") as file:
        file.write(f"{stock},{buy_price},{sell_price},{quantity}\n")
def view_trades():
    if len(trades) == 0:
        print("No trade found...")
    else:
        for trade in trades:
            print(f"{trade['stock']}: {trade['buy_price']} - {trade['sell_price']} - quantity: {trade['quantity']}")
            profit = (trade['sell_price'] - trade['buy_price'])* trade['quantity']
            if profit > 0:
                print(f"profit: {profit}")
            elif profit == 0:
                print("No profit...")
            else:
                print(f"loss: {profit}")
def total_trades():
    print(f"TOTAL TRADES     : {len(trades)}")
def trade_statistics():
    profit_count =0
    loss_count =0
    for trade in trades:
        if (trade['sell_price'] -trade['buy_price']) > 0:
            profit_count += 1
        elif  (trade['sell_price'] -trade['buy_price']) < 0:
            loss_count += 1
    print(f"\nTOTAL TRADES     : {len(trades)}",f"\nPROFIT TRADES    : {profit_count}",f"\nLOSS COUNT       : {loss_count}")
while True:
    print("=====TRADE TRACKER=====\n\nADD TRADE        : 1\nVIEW TRADES      : 2\nTOTAL TRADES     : 3\nSTATISTICS       : 4\nEXIT             : 5\n")
    user_choice = input("Enter your choise: ")
    if user_choice == "1" :
        add_trade()
    elif user_choice == "2":
        view_trades()
    elif user_choice =="3":
        total_trades()
    elif user_choice == "4":
        trade_statistics()
    elif user_choice == "5":
        break
    else:
        print("invelid choice")