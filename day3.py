print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
print("You're at a cross road. Where do you want to go? Type 'Left' or 'right'")
a = input()
if a == 'left':
    print("Your arrived at the island unharmed. There is a house with three door. One Red, one yellow and one blue. Which color do you choose?")
    b = input()
    if b == 'blue':
        print("You win!!!")
    elif b == 'yellow':
        print("Game over")
    elif b == 'red':
        print('Game over')
    else:
        print("Error")

else:
    print("You lose! Game over")
