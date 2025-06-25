print("welcome to my computer quiz")
playing=input("Do you want to play game ? ")
if playing.lower() !="yes":
    quit()
print("okay lets Play :")
score=0
answer=input("what does cpu stands for ? ")
if answer.lower()=="central processing unit":
    print("correct ?")
    score+=1
else:
    print("incorrect")

answer=input("what does th GPU stands for ? ")
if answer.lower()=="graphics processing unit":
    print("correct ")
    score+=1
else:
    print("incorrect")
answer=input("what does the RAM stands for ? ")
if answer.lower()=="random access memory":
    print("correct ")
    score+=1
else:
    print("incorrect")
answer=input("what does the ROM stands for ? ")
if answer.lower()=="read only memory":
    print("correct ")
    score+=1
else:

    print("incorrect")
print(f"you scored {score} points")