# rock paper sissor game
import random as r
rock = '0'
paper = '1'
scissors = '2'
list = [rock,paper,scissors]




print("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors")
a = input()
if a == list[0]:
    # Rock
    print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)
if a == list[1]:
    # Paper
    print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)
if a == list[2]:
    # Scissors
    print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)

print("Computer choose:")
c = r.randint(0,2)
b = list[c]
if b == list[0]:
    # Rock
    print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)
if b == list[1]:
    # Paper
    print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)
if b == list[2]:
    # Scissors
    print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)


if a == rock and b == paper:
    print("Your lose")
elif a == paper and b== scissors:
    print("You lose")
elif a == scissors and b== rock:
    print("You lose")
elif a == b:
    print("It's a draw")
else:
    print("You win")
