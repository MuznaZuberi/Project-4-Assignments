# ============= Guess the Number Game (Computer) | Built by Muzna Amir Zubairi =============
import random

print("💻 Number Guessing Game (Computer Version) | Built by Muzna Amir Zubairi")
def Number_Guessing_Game(n):
    random_number = random.randint(1, n)
    guess_num = 0

    while guess_num != random_number:
        try:
            guess_num = int(input(f"Guess a number between 1 and {n}: "))
            if guess_num < random_number:
                print("🔻 Too Low! Try again.")
            elif guess_num > random_number:
                print("🔺 Too High! Try again.")
        except ValueError:
            print("❌ Please enter a valid number.")

    print(f"🎉 Congrats! You correctly guessed the number: {random_number}")

Number_Guessing_Game(10)
