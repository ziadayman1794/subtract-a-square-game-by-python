# Ziad Ayman Farouk 20210147
number_of_piles = int(input("enter the total number of piles to play \n"))
k = 5
w = 0  # }
x = 0  # }    decaliring varaibles to be used
b = 0  # }
z = number_of_piles

for j in range(0, number_of_piles):  # loop to make players take turns
    while k < 8:  # infinte loop to make player choose the proper number to play
        x = float(input("enter your number player 1 \n"))
        y = int(x) ** 0.5
        if int(x) < x or int(y) < y or x > number_of_piles or int(x) > z or int(x) == 0:  # condtions of the game
            print("please enter non zero square integer number smaller than: " + str(z))
        else:
            break
    z = z - int(x)  # assign the reminder of piles after player 1 choose
    print("the reminder is " + str(z))

    if z == 0:  # checkimg for the winner
        print("player 1 is the winner")
        exit()
    else:
        pass

    while k < 8:  # infinte loop to make player choose the proper number to play
        b = float(input("enter your number player 2: \n"))
        s = int(b) ** 0.5
        if int(b) < b or int(s) < s or b > number_of_piles or int(b) > z or b == 0:  # condtions of the game
            print("please enter non zero square integer number smaller than " + str(z))
        else:
            break
    w = z - int(b)  # assign the reminder after player 2 choosing
    print("the reminder is: " + str(w))
    if w == 0:  # checking for the winner
        print("player 2 is winner")
        exit()

    z = w  # assign the new total number to play after the turn
