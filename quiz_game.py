print("Welcome to the quiz!")

playing = input("Do you want to play? ").lower() #user writes in the console
score = 0

if playing != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct!")
    score +=1
else: print("Incorrect!")

answer = input("What does GPU stand for? ").lower()

if answer == "graphics processing unit":
    print("Correct!")
    score +=1
else: print("Incorrect!")

answer = input("What does RAM start for? ").lower()

if answer == "random access memory":
    print("Correct!")
    score += 1
else: print("Incorrect!")


answer = input("What does PSU stand for? ").lower()

if answer == "power supply unit":
    print("Correct!")
    score += 1
else: print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")