# import random
# choices = ['r','p','s','rock','paper','scissors']


# def check_winner(player_choice, com_choice):
#     if player_choice == "r" or 'rock' and com_choice == 's' or 'scissors':
#         return "Player wins"
#     elif player_choice == "p" or 'paper' and com_choice == 'r' or 'rock':
#         return "Player wins"
#     elif player_choice == "s" or 'scissors' and com_choice == 'p' or'paper':
#         return "Player wins"  
#     elif player_choice == "s" or 'scissors'and com_choice == 'r' or 'rock':
#         return "computer wins" 
#     elif player_choice == "r" or 'rock' and com_choice == 'p' or 'paper':
#         return "Computer wins"   
#     elif player_choice == "p" or 'paper' and com_choice == 's' or'scissors':
#         return "Computer wins"  
#     else:
#         return "It's a tie!"        

# print("Welcome to rock, paper, scissors.\n Enter R for Rock. P for Paper. S for Scissors.")    

# player_choice = input(">").lower()
# com_choice = random.choice(choices)
# if player_choice in choices:
#     result = check_winner(player_choice, com_choice)

#     print(result)
#     print(f"computer selected {com_choice}")

# else:
#     print("Invalid input!")
    
# h = 10
# while h>0:
#     print(h)
#     h-=1
# print(h)

# h = 0
# while h<9:
#     print(h)
#     h+=1
# print(h)
# print('BOOM!')

# h = 1
# while h <= 10:
#     if h == 10:
#        print('Boom!')
#     else:
#         print(h)
#     h+=1


i = 1
while True:
    print(f"keep playing {i}")     
    c = input('continue?\n>')
    if c == "y":
        i+=1
        continue
    else:
        break   