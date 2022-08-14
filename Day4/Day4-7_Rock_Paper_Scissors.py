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

#Write your code below this line 👇
# print(rock)
# print(paper)
# print(scissors)
import random
game_art = [rock, paper, scissors]


player_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors.\n"))
print(game_art[player_choice])

random_choice = random.randint(0, 2)
print("Computer chose:")
print(game_art[random_choice])

if player_choice >= 3 or player_choice < 0:
  print("You typed an invalid number, you lose!")
elif player_choice == 0 and random_choice == 2:
  print("You win!")
elif random_choice == 0 and player_choice == 2:
  print("You lose")
elif random_choice > player_choice:
  print("You lose")
elif player_choice > random_choice:
  print("You win!")
elif player_choice == random_choice:
  print("Its a draw")




