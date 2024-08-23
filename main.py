import random

def game():
    while True:
        user = input("Enter your choice (snake, water, gun): ")
        possible_actions = ["snake", "water", "gun"]
        computer = random.choice(possible_actions)
        print(f"\nYou chose {user}, computer chose {computer}.\n")

        if user == computer:
            print(f"Both players selected {user}. It's a tie!")
        elif user == "snake":
            if computer == "water":
                print("Snake drinks water! You win!")
            else:
                print("Gun shoots snake! You lose.")
        elif user == "water":
            if computer == "gun":
                print("Water rusts gun! You win!")
            else:
                print("Snake drinks water! You lose.")
        elif user == "gun":
            if computer == "snake":
                print("Gun shoots snake! You win!")
            else:
                print("Water rusts gun! You lose.")
        else:
            print("invalid input")

        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
if __name__ == "__main__":
 game()
