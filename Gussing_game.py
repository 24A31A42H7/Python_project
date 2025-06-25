import random

top_of_range=int(input("type a number"))
if top_of_range <=0:
    print("please type a number than 0 a next time")
    quit()
def random_number():
    random_number=random.randint(0,top_of_range)
    return random_number

guess=0
while True:
    guess_number=int(input("enter a number "))
    if guess_number==random_number():
        print("you got it ")
        guess+=1
        break
    elif guess_number >=random_number():
        print("you entered larger number")
    else:
        print("you entered smaller number")
if guess>0:
    print(f"congratulations you gessed {guess} times")
else:
    print("don't worry ! you can try it again ")
