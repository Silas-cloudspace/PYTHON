print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()
if playing != "yes":
    quit()

print("Ok! Let's play!") 
score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1    
else:
    print("Incorrect!")
    
answer = input("What goes GPU stand for? ").lower()
if answer == "graphics pricessing unit":
    print("Correct!")
    score += 1   
else:
    print("Incorrect!")
    
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1   
else:
    print("Incorrect!")
    
answer = input("What doe PSU stand for? ").lower()
if answer == "power supply":
    print("Correct!")
    score += 1   
else:
    print("Incorrect!")
    
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")