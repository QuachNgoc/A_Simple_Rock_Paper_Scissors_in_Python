import random
import time
print("Welcome to the Rock, Paper, Scissor!!\n")
print("Rock: 1, Paper: 2, Scissors: 3\n")
player = int(input("Player: "))
bot = random.randint(1,3)
UI =['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
''', 
'''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''', '''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
time.sleep(2)
print(UI[player-1])
print(UI[bot-1])

if(player == bot):
    print("DRAW")
if(player > bot):
    if(player == 3 and bot == 1): #player: scissors(3), bot: rock(1)
        print("Bot wins!")
    else:
        print("Player wins!")
elif(player < bot):
    if(player == 1 and bot == 3): #bot: scissors(3), scissors: rock(1)
        print("Player wins!")
    else:
        print("Bot wins!")