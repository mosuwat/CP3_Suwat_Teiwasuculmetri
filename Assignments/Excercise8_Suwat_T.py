usernameInput = input("Enter username: ")
passwordInput = input("Enter password: ")
if usernameInput == "momo50" and passwordInput == "1234":
    print("Done!")
    print("----------Momo shop----------")
    print("1.Coke = 15฿\n2.Sprite = 12฿\n3.Water = 8฿")
    print("-----------------------------")
    order = int(input("What would you like to buy?: "))
    if order == 1:
                qnt = int(input("How many do you want?: "))
                price = qnt*15
                print("The price is", price)
    elif order == 2:
                qnt = int(input("How many do you want?: "))
                price = qnt*12
                print("The price is", price)
    elif order == 3:
                qnt = int(input("How many do you want?: "))
                price = qnt*8
                print("The price is", price)
    else:
        print("Error")
else:
    print("Error")