import random
responce  = "y"
while responce == "y":
    num = random.randint(1,6)
    if num == 1:
        print("         ")
        print("  [ 0 ]  ")
        print("         ")
    if num  == 2:
        print("         ")
        print(" [ 0   0 ]")
        print("         ")
    if num  == 3:
        print(" [   0   ]")
        print(" [ 0   0 ]   ")
        print("         ")
    if num  == 4:
        print("  [0  0]  ")
        print("  [0  0]   ")
    if num  == 5:
        print(" [ 0   0 ] ")
        print(" [   0   ] ")
        print(" [ 0   0 ] ")
    if num  == 6:
        print(" [ 0   0 ]  ")
        print(" [ 0   0 ] ")
        print(" [ 0   0 ]  ")
    responce = input("Enter y to roll the dice and n to exit: ")
    if responce == "n":
        break