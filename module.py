import sys
from statistics import *
from random import *



def random_user_id(user_id):
    random_id = ''.join(sample(user_id, len(user_id)))
    return random_id

#a function that generates random 6 digit characters

def random_user_id_6():
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    random_id = ''.join(sample(characters, 6))
    return random_id

print(random_user_id("muiz"))
print(random_user_id_6())

# from list import m, n, o

# from ayo_game import AyoGame


# import ('csc310.ayo_game/ayo_game.py') as ayo_game
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2

# print(sys.argv[0])  # this line would print out: ['filename', 'argument1', 'argument2']
# print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
# n = 1
# if len(sys.argv) < 3:
#     print("Usage: python module.py <player1_name> <player2_name>")
#     sys.exit(n) 


# arg1 = sys.argv[1] = "muiz"
# arg2 = sys.argv[2] = "AYO GAME"
# sys.__builtins__().print("Welcome {}. Enjoy  {} challenge!".format(sys.argv[1], sys.argv[2]))

# mean_of_m = mean(m)
# median_of_m = median(m)
# mode_of_m = mode(m)
# stdev_of_m = stdev(m)

# print(f"mean of m: {mean_of_m}, median of m: {median_of_m}, mode of m: {mode_of_m}, stdev of m: {stdev_of_m}")

# print(f'mean of n: {mean(n)},median of n: {median(n)}, mode of n : {mode(n)}')

