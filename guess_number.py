number = 10
max_guesses = 3
remaining_guesses = max_guesses

print("I'm thinking of a number...")
while remaining_guesses > 0:
    guess = input("What number am I thinking of? ")
    
    if guess.lower() == 'q':
        print(f"The number was {number}.")
        break
    
    if guess.isdigit():
        guess = int(guess)
        remaining_guesses -= 1
        if guess == number:
            print("Congratulations! You guessed the right number.")
            break
        elif remaining_guesses > 0:
            print(f"Sorry! Incorrect guess. You have {remaining_guesses} guesses left.")
        else:
            print(f"Sorry! Incorrect guess. No more guesses left. The number was {number}.")
            break
    else:
        print("Invalid input. Please enter a number or 'q' to quit.")
