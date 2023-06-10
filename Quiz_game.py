print("WELCOME")

play = input("Do you wish to play? ")

if play.lower() != "yes":
    quit()

print("Okay! Let's Go!")
score = 0

answer = input("How many seasons does big bang theory have? ")
if answer.lower() == "12":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("Who does Sheldon get married to? ")
if answer == "Amy":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("Did Leonard and Penny ever get married? ")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("You got " + str(score) + " questions correct")
print("You got " + str(score/3 * 100) + "%")