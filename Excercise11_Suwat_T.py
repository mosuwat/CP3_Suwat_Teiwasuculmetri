time = int(input("Enter number: "))
for x in range(time):
    y = x+1
    space = time - x - 1
    print(" "*space + "*"*y + "*"*x)