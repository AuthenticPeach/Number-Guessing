import random

def guess_number():
    play_again = True

    while play_again:
        number = random.randint(1, 100)  # Generate a random number between 1 and 100
        attempts = 0

        while True:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break

        play_again_input = input("Do you want to play again? (yes/no): ")
        play_again = play_again_input.lower() == "yes"

guess_number()
