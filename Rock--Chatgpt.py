import random

def get_user_choice():
    """Get user's choice from input."""
    return input("What's your choice? ('r' for Rock, 'p' for Paper, 's' for Scissors):\n")

def get_pc_choice():
    """Generate a random choice for the PC."""
    return random.choice(['r', 'p', 's'])

def determine_winner(user_choice, pc_choice):
    """Determine the winner of the game."""
    if user_choice == pc_choice:
        return "It's a tie!!"
    elif (
        (user_choice == 'p' and pc_choice == 'r') or
        (user_choice == 'r' and pc_choice == 's') or
        (user_choice == 's' and pc_choice == 'p')
    ):
        return "You Won!"
    else:
        return 'Pc Won!'

def main():
    """Run the Rock, Paper, Scissors game."""
    while True:
        user_choice = get_user_choice()
        
        if user_choice in ['r', 'p', 's']:
            pc_choice = get_pc_choice()
            print(f"Your choice: {user_choice}")
            print(f"PC choice: {pc_choice}")
            
            result = determine_winner(user_choice, pc_choice)
            print(result)
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
