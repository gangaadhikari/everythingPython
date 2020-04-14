import random

def game():
    bot = (random.randint(1, 3))
    guess = int(input("Rock (1), Paper(2), or Scissor(3)?\n"))
    if (guess == bot):
        print("Tie")
    elif ((guess == 1 and bot == 2) or (guess == 2 and bot == 3) or (guess == 3 and bot == 1)):
        print("You lost")
        game()
    else:
        print("You won!")
        print(bot)


game()