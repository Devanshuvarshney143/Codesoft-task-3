import random  # Importing the 'random' module for generating random choices

def winner(user_choice, computer_choice):
    # Function to determine the winner 
    if user_choice == computer_choice: 
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        
        return "You win!"
    else:  
        return "You lose!"

def play_game():
    user_score = 0  # Initialize user's score
    computer_score = 0  # Initialize computer's score
    
    while True:  # Begin the game loop
        print("\nRock, Paper, Scissors \n\nLet's play!\n")  
        
        # user input
        user_choice = input("Enter your choice (rock/paper/scissors or q(quit)): ").lower()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])  # Generate computer's choice
        
        if user_choice == 'q': 
            break  # Exit the game loop
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Please enter a valid choice!")  
            continue  
        
        # Display choices made by the user and computer
        print(f"\nYou chose: {user_choice} \ncomputer chose: {computer_choice}")
        
        # result of the game
        result = winner(user_choice, computer_choice)
        print(result)
        
        # 
        if result == "You win!":
            user_score += 1  # Increment user's score
        elif result == "You lose!":
            computer_score += 1  # Increment computer's score
        
        # Display  scores
        print(f"\nScores - You: {user_score}  Computer: {computer_score}")
        
    print(" \nThanks for playing ") 

play_game()
