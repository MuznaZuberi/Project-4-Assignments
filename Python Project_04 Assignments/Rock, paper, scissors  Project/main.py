# ============= Rock , Paper , Scissor Game | Built by Muzna Amir Zubairi =============
import random

print("🎮 Rock | Paper | Scissors `Game Developed by Muzna Amir Zubairi")
def RPS_Game():
    user = input('Whats Your Choice? "r" for rock , "p" for paper , "s" for scissor: ')
    computer = random.choice(["r", "p", "s"])
    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return "🎉 Congrats! You Won"

    else:
    	return "❌ Opzzzzzzz You Lost Plz Try Again Later!"
def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

print(RPS_Game())
