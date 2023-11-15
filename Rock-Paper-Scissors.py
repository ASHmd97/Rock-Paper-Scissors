import random

while True:
    user_choice = input("What's your choice? ('r' for Rock, 'p' for Paper, 's' for Scissors):\n")
    
    if user_choice in (['r', 'p', 's']):
        pc_choice = random.choice(['r', 'p', 's'])
        print(f"Your choice: {user_choice}")
        print(f"PC choice: {pc_choice}")
        
        if user_choice == pc_choice:
            print("It's a tie!!")

        elif  (user_choice == 'p' and pc_choice == 'r') or (user_choice == 'r' and pc_choice == 's') or (user_choice == 's' and pc_choice == 'p'):
            print("You Won!")
        
        else:
            print('Pc Won!')
    
    else:
        print("invalid choice")

