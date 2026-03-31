import random
options = ['rock', 'paper', 'scissors']
users_input = str(input("please enter any of these:Rock,Paper and Scissors"))
computer_choice = random.choice(options)

print("computer choice was ", computer_choice,
      "and yours choice was ", users_input)

if computer_choice == users_input:
    print("tie")

elif computer_choice == "rock" and users_input == "paper":
    print("you won🎉🎉🎉")

elif computer_choice == "paper" and users_input == "scissiors":
    print("you won🎉🎉🎉")

elif computer_choice == "scissiors" and users_input == "rock":
    print("you won🎉🎉🎉")

else:
    ("invalid choice try again!")
