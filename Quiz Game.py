print("Welcome to Skyscripter's Quiz .04!")

confirm = input("Do you wanna play? ").lower()

if confirm != "yes":
    quit()

print("Alrihgt lets go!")
score = 0

question1 = input("What is full form of CPU? ").lower()
if question1 == "central proccessing unit":
    print("Correct answer!!")
    score += 1
else:
    print("Wrong answer")


question2 = input("What is full form of GPU? ").lower()
if question2 == "graphic proccessing unit":
    print("Correct answer!!")
    score += 1
else:
    print("Wrong answer!!")

question3 = input("What is full form of PU? ").lower()
if question3 == "power unit":
    print("Correct answer!!")
    score += 1
else:
    print("Wrong answer")

question4 = input("where is data stored in computer? ").lower()
if question4 == "Ram":
    print('Correct answer!!')
    score += 1
else:
    print("Wrong answer")

question5 = input("What is full form of RAM? ").lower()
if question5 == "Random access memory":
    print('Correct answer!!')
    score += 1
else:
    print("Wrong answer")

print("You got " + str(score) + " questions correct out of 5!")
print("Your percentage score is " + str(score/5 * 100))
