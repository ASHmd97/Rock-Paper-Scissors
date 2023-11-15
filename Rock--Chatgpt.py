import random

# Initialize scores
user_score = 0
computer_score = 0

# Welcome message
print("Welcome to Rock, Paper, Scissors!")

while True:
    # Get user input
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Validate user input
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice: ").lower()

    # Generate computer choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    # Display user and computer choices
    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")

    # Determine the winner and update scores
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    # Display current scores
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")

    # Check if either player has reached 10 points
    if user_score == 10:
        print("Congratulations! You won!")
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing. Goodbye!")
            break
    elif computer_score == 10:
        print("Computer wins. Better luck next time!")
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing. Goodbye!")
            break
