import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = input("Take a guess: ")

        try:
            guess = int(guess)
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number within the range 1-100.")
            elif guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    number_guessing_game()
