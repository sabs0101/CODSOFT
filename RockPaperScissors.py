import random

def rock_paper_scissors():
    print("🎮 Welcome to Rock-Paper-Scissors 🎮")
    print("Instructions: Type rock, paper, or scissors to play.")
    
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = input("\nEnter your choice (rock, paper, scissors): ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice! Please try again.")
            continue
        
    
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"🤖 Computer chose: {computer_choice}")
        
        
        if user_choice == computer_choice:
            print("It's a tie! 😐")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("💻 Computer wins this round!")
            computer_score += 1
        
        
        print(f"Score: You {user_score} - {computer_score} Computer")
        
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nFinal Score:")
            print(f"You {user_score} - {computer_score} Computer")
            print("Thanks for playing! 👋")
            break


rock_paper_scissors()
