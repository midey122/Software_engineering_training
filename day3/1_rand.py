rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


import random

stats = True
score = {
    "user_score":0,
    "computer_score":0
}



while stats == True:
    print(f"welcome to RPS \n{rock} \n {paper} \n {scissors}")
    available_letter =("rock", "paper", "scisscor")
    chioce_letter = print(f"R stand for {available_letter[0]}\n, P stand for {available_letter[1]} \n, S stand for {available_letter[2]} ")
    user_letter = input(f"pick a letter ( r s p)\n" )
    letter_1 = ("r")
    letter_2 = ("s")
    letter_3 = ("p")
    my_letter =("r", "s" ,"p")
    computer_letter = random.choice(my_letter)
    print(f"the computer choice is {computer_letter} \n")
    if user_letter == "p" and computer_letter == "r":
        score["user_score"] += 1
        print(f"congratulation paper beats rock \n")
        print(f"{score} \n")
    elif user_letter == "r"  and computer_letter == "s":
        score["user_score"] += 1
        print(f"congratulation rock beat scissor\n")
        print(f"{score} \n")
    elif user_letter == "s" and computer_letter == "p":
        score["user_score"] += 1     
        print(f"congatulation scissor beat paper \n")
        print(f"{score} \n")
    elif user_letter == computer_letter:
        print(f"draw \n")
        print(f"{score} \n")
    else:
        score["computer_score"] += 1     
        print("you lose")
        print(f"{score} \n")
    choice = input(f"do you want to end this game  y or n")
    if choice == "y":
        stats = False