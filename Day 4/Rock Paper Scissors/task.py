rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("welcome to rock paper and scissors")
users_move=input("enter your move rock paper or scissors")
if users_move=="rock":
    print("you have entered rock" +rock)
elif users_move=="paper":
    print("you have entered paper" +paper)
else:
    print("you have entered scissor"+ scissors)
moves = [rock, paper, scissors]
import random
random_move=random.randint(0,2)
print(moves[random_move])
if users_move =="rock" and random_move == 1 or random_move==0:
    print("you lose")
elif users_move =="rock" and random_move == 2:
    print("you win")
elif users_move == "paper" and random_move == 2:
    print("you lose")
elif users_move == "paper" and random_move == 0:
    print("you win")
elif users_move == "scissors" and random_move == 0:
    print("you lose")
elif users_move == "scissors" and random_move == 1:
    print("you win")


