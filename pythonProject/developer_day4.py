import random
import Day1

# andom_interger = random.randint(1,10)
# print(random_interger)
# print(Day1.my_module)
# a = random.random() *10
# print(a)
#
# random_folat = random.uniform(1,50)
# print(random_folat)
#
# random_head_or_tails = random.randint(0,1)
# if random_head_or_tails == 1:
#     print("Head")
# else:
#     print("Tails")
#
# #Data structure
# states = ["Karnataka","kolkatta","UttarPradesh","Maharastra","Andrapradesh"]
# print(random.choice(states))
#
# random_index = random.randint(0,len(states))
# print(states[random_index])

Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
Paper =("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game = [Rock,Scissors,Paper]

start_game = input("Enter what u want ,type 0 rock ,1 for paper and 2 scissor")
if start_game == "0" or "1" or "2":
    computer = random.randint(0,2)
    print(game[computer])
    my_game = game[int(start_game)]
    print(my_game)
    if computer >= int(start_game):
        print("won")
    else:
        print("lose")

