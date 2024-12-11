import time

print("Welcome to Quiz Game!")

playing =  input("Do you want to play? ")


if playing.lower() != "yes":
    quit()

print("Okey! Let's Play the Quiz!")
score = 0

# Question 1
print("What does CPU stand for? ")
question = input()
if question.lower() == "central processing unit":
    # print("Correct! 🎉 Great Job! 🎉")
    print(r"""
    🎉 🎉 🎉
    Correct!
    🎉 🎉 🎉
        """)

    score += 1
    time.sleep(2)
else:
    print("Incorrect! 😒")
    time.sleep(2)

# Question 2
print("What does RAM stand for? ")
question = input()
if question.lower() == "random access memory":
    print(r"""
    🎉 🎉 🎉
    Correct!
    🎉 🎉 🎉
        """)
    score += 1
    time.sleep(2)
else:
    print("Incorrect! 😒")
    time.sleep(2)

# Question 3
print("What does HTML stand for? ")
question = input()
if question.lower() == "hypertext markup language":
    print(r"""
    🎉 🎉 🎉
    Correct!
    🎉 🎉 🎉
        """)
    score += 1
    time.sleep(2)
else:
    print("Incorrect! 😒")
    time.sleep(2)

# Question 4
print("What does LAN stand for? ")
question = input()
if question.lower() == "local area network":
    print(r"""
    🎉 🎉 🎉
    Correct!
    🎉 🎉 🎉
        """)
    score += 1
    time.sleep(2)
else:
    print("Incorrect! 😒")
    time.sleep(2)

# Question 5
print("What does HTTP stand for? ")
question = input()
if question.lower() == "hypertext transfer protocol":
    print(r"""
    🎉 🎉 🎉
    Correct!
    🎉 🎉 🎉
        """)
    score += 1
    # time.sleep(2)
else:
    print("Incorrect! 😒")
    # time.sleep(2)


time.sleep(1)
print(f"Your final score is: {score} out of 5! " )
time.sleep(2)





if score == 5 : 
    print("you are doing great! 🎉")
elif score == 4:
    print("Your are doing good! 🎉 ")
else: 
    print("Try again 🙄")