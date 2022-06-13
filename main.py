import art
import random

print(art.logo) ##print the logo
print("I am thinking of a number between 1 and 100")##print instruction
target=random.randint(0,101)

global HARD_MODE
global EASY_MODE
HARD_MODE=5
EASY_MODE=10
guess=0
def check_easy():
  if guess>target:
    print("too high")
    EASY_MODE=EASY_MODE-1
  elif guess<target:
    print("too low")
    EASY_MODE=EASY_MODE-1
  else:
    print("good guess")

def check_hard():
  if guess>target:
    print("too high")
    HARD_MODE=HARD_MODE-1
  elif guess<target:
    print("too low")
    HARD_MODE=HARD_MODE-1
  else:
    print("good guess")
  

def difficulty():
  while True:
    global difficulty
    difficulty=input("Choose your difficulty between 'easy' and 'hard' ")
    if difficulty.lower() not in("easy","hard"):
      print("please enter the valid input such as easy or hard.")
    else:
      life=difficulty+"_mode"
      print(difficulty)
      break

difficulty()
if difficulty=="hard":
  guess=int(input("Choose a number between 1 and 100: "))
  while True:
    check_hard()
elif difficulty=="easy":
  guess=int(input("Choose a number between 1 and 100: "))
  while True:
    check_easy()
  
    


