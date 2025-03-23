# Code for simple quiz game

print("Welcome to the quiz game!!!")

play = input("Are you want to play? ")

if play.lower() != "yes":
    quit()

name = input("Please Enter your Name: ")
score = 0

# first question
answer = input("1. What is the primary function of the CPU in a computer? ")

if answer.lower() == "process instructions":
    print("Correct Answer!")
    score += 1
else:
    print("Incorrect Answer!")


# Second question
answer = input("2. What technology is used to create virtual machines? ")

if answer.lower() == "hypervisor":
    print("Correct Answer!")
    score += 1
else:
    print("Incorrect Answer!")


# Third question
answer = input("3. What does the term 'cloud storage' refer to? ")

if answer.lower() == "online data storage":
    print("Correct Answer!")
    score += 1
else:
    print("Incorrect Answer!")


# forth question
answer = input("4. What is the purpose of a DNS server? ")

if answer.lower() == "translate domain names":
    print("Correct Answer!")
    score += 1
else:
    print("Incorrect Answer!")


# fifth question
answer = input(
    "5. Which algorithm is commonly used for searching in a sorted array? ")

if answer.lower() == "binary search":
    print("Correct Answer!")
    score += 1
else:
    print("Incorrect Answer!")


print("Your Quiz is over!!! \n")

# choose pass or fail
if score >= 3:
    print("You passed!")
else:
    print("You Failed!")

print(name + " you achived " + str(score) + " marks.")
