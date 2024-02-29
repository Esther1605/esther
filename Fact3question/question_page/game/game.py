import random

#rules
#1. scissors wins against rock
#2. scissors wins against paper
#3. paper wins agaist rock


# 0 rep rock
# 1 rep paper
# 2 rep scissors



user_choice=int(input("Enter your choice: Type 0 for rock, 1 for paper, 2 for scissors."))
computer_choice= (0)
print("computer chose")
print(computer_choice)


if computer_choice == user_choice:
   print("it's a draw")
elif computer_choice>user_choice:
   print ("You lose")
elif user_choice>computer_choice:
   print ("You win")
elif computer_choice == 0 and user_choice==2:
   print ("You lose")

elif user_choice  == 0 and computer_choice==2:
    print ("You win")
   