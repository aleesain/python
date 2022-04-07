logo =  """
  _____                       _____  _       _     _   _       _ 
  / ____|                     |  __ \(_)     | |   | | | |     | |
 | |  __ _   _  ___  ___ ___  | |__) |_  __ _| |__ | |_| |_   _| |
 | | |_ | | | |/ _ \/ __/ __| |  _  /| |/ _` | '_ \| __| | | | | |
 | |__| | |_| |  __/\__ \__ \ | | \ \| | (_| | | | | |_| | |_| |_|
  \_____|\__,_|\___||___/___/ |_|  \_\_|\__, |_| |_|\__|_|\__, (_)
                                         __/ |             __/ |  
                                        |___/             |___/   


"""
import random
print(logo)
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
print("Welcome to the Number guessing game")
print("I'm guessing of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
chances = 0
if level == "easy":
  chances = 10
else:
  chances = 5
x  = random.randint(1,100)
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
con_game = True
while con_game:
  while chances > 0:
    print(f"You have {chances} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > x:
      chances-=1
      if chances > 0:
        print("Too High")
        print("Guess Again")
    elif guess < x:
      chances-=1
      if chances > 0:
        print("Too Low")
        print("Guess Again")
    elif guess == x:
      print(f"You got it! The correct answer is: {x}")
      con_game = False
      break
    if chances == 0:
      print("You've run out of guesses. YOU LOST!")
      con_game = False
      break