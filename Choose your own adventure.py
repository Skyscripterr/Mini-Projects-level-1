name = input("Type your name: ")
print("Welcome", name, "to this this adventure!")

answers = input(
    "You are on a dirt road, it has come to an end and you can go left or right. which way would like you can go? ").lower()

if answers == "left":
    answer = input(
        "You come to a river and you can walk around it or swim across? type walk around and swim to swim across: ")
    if answer == "walk":
        print("You walked out many miles and you lost the game ")
    elif answer == "swim":
        print("You swam across and were eaten by an aligator")
    else:
        print("not a valid input.You lose.")

elif answers == "right":
    answer = input("You came to a bridge, it looks wobbly, do you want to keep walking or turn back? type turn back or walk ")
    if answer == "back":
        print("You back out and i consider you looser ")
    elif answer == "walk":
        print("You walk across and were eaten by an donkey")
    else:
        print("not a valid input.You lose.")
else:
    print("Not a valid option. You lose.")


print("Thankyou for playing")