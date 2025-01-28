print('Welcome to my Computer quiz!')

playing = input("Do u want to play? ")

if playing.lower() != "yes":
    quit()

print("okey! lets play! :) ")
scoer = 0

answer = input(" what does RAM stand for? ")
if answer.lower() == "random access memory" :
    print("correct")
    scoer += 1
else :
    print("wrong!") 

answer = input(" what does cpu stand for? ")
if answer.lower() == "central processing unit" :
    print("correct")
    scoer += 1
else :
    print("wrong!") 

answer = input("what does GPU stand for? ").lower()
if answer == "graphic processing unit" :
    print("correct")
    scoer += 1
else :
    print("wrong!") 

answer = input(" what does PSU stand for? ")
if answer.lower() == "power supply" :
    print("correct")
    scoer += 1
else :
    print("wrong!") 

print ("you got " + str(scoer/4 *100) + "percent of questions correct!")