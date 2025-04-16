# ============= Guess the Number Game (User) | Built by Muzna Amir Zubairi =============
import random

print("🎯 Number Guessing Game (User Version) | Built by Muzna Amir Zubairi")
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


def computer(x):
    to_low = 1
    to_high = x
    feedback = ""

    while feedback != "c":
        guess_num = random.randint(to_low , to_high)
        feedback = input(f"Is {guess_num} Too High(h) , Too Low(l) or correct (C)").lower()
        if feedback == "h":
            to_high = guess_num -1 
        elif feedback == "l":
            to_low = guess_num +1
    print("Yey!" , guess_num)

computer(10)

Number_Guessing_Game(10)
