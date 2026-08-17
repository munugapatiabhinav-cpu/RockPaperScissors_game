while True:
   import random
   system_choice = ["Rock", "Paper", "Scissors"]
   system_choice = random.choice(system_choice)
   user_choice = int(input("Enter 1 for Rock, 2 for Paper, and 3 for Scissors: "))
   if user_choice not in [1,2,3]:
      print("Invalid input. Please try again.")
   elif (system_choice == "Rock" and user_choice == 2) or (system_choice == "Paper" and user_choice == 3) or (system_choice == "Scissors" and user_choice == 1):
      print("You win!")
   elif (system_choice == "Rock" and user_choice == 3) or (system_choice == "Paper" and user_choice == 1) or (system_choice == "Scissors" and user_choice == 2):
      print("You lose!")
   elif (system_choice == "Rock" and user_choice == 1) or (system_choice == "Paper" and user_choice == 2) or (system_choice == "Scissors" and user_choice == 3):
      print("It's a tie!")
   
   
   


