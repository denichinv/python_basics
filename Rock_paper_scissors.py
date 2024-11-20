import random

username = input("Enter your name - ")
score_to_reach = int(input("Choose a score you wish to play to - "))

user_score = 0
computer_score = 0

while user_score < score_to_reach and computer_score < score_to_reach:
    user_choice = input("Choose rock,paper or scissors - ").lower()
    my_list = ["rock","paper", "scissors"]
    computer_choice = random.choice(my_list)
    if user_choice in my_list:
        if user_choice == computer_choice:
            print("The result is draw.")
            print(f"{username} {user_score} - {computer_score} Computer")
        elif user_choice == "rock" and computer_choice == "paper":
            computer_score += 1
            print("You lost!")
            print(f"{username} {user_score} - {computer_score} Computer")

        elif user_choice == "rock" and computer_choice == "scissors":
            user_score+= 1
            print("You won!")
            print(f"{username} {user_score} - {computer_score} Computer")

        elif user_choice == "paper" and computer_choice == "rock":
            user_score+= 1
            print("You won!")
            print(f"{username} {user_score} - {computer_score} Computer")

        elif user_choice == "paper" and computer_choice == "scissors":
            computer_score += 1
            print("You lost!")
            print(f"{username} {user_score} - {computer_score} Computer")

        elif user_choice == "scissors" and computer_choice == "paper":
            user_score+= 1
            print("You won!")
            print(f"{username} {user_score} - {computer_score} Computer")

        elif user_choice == "scissors" and computer_choice == "rock":
            computer_score += 1
            print("You lost!")
            print(f"{username} {user_score} - {computer_score} Computer")


    else:
        print("Wrong command!")

print(f"FINAL SCORE: \n{username} {user_score} - {computer_score} Computer")

if user_score > computer_score:
    print(f"Congratulations, {username}! You won the game!")
else:
    print("Computer wins the game!")


