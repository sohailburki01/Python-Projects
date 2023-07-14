from numpy import random

def get_num():
    num = random.randint(1,7)
    return num
   

while True:
    choice = input("Roll (y/n): ")    
    if choice == ("y" or "Y"):
        num = get_num()
        print(num)
        print()
        if num == 6:
            print("Again Rolled: ")
            num2 = get_num()
            print(num2)
            print()

            if num2 == 6:
                print("Sorry you can only get 2 '6's")
                print()

    else:
        print("Program Exited... Bye !")
        break

