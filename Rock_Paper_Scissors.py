import random
user_wins=0
computer_wins=0

while True:
    user_input=input("type Rock or paper or Scissors or Q for quit ")
    if user_input.lower()=="q":
        break
    if user_input not in ["scissor","paper","rock"]:
        print("you entered invalid choice ")
        continue
    random_choice=random.choice(["scissor","paper","rock"])
    if random_choice==user_input:
        computer_wins+=1
        print("you lost")
    else:
        print("you wins ")
        user_wins+=1
print(f"you got {user_wins} points")
print(f"you got {computer_wins} points")