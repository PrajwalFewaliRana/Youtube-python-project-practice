print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play :)")
score =0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
answer = input("What does GUI stand for? ").lower()
if answer == "graphical user interface":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
answer = input("What does ROM stand for? ").lower()
if answer == "read only memory":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
answer = input("What does IO stand for? ").lower()
if answer == "input output":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
print("You scored ",score,"out of 5 questions correct")
print("You got ",(score/5)*100,"% correct ansyeswers")