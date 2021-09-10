import random
#This is an updated version by clairemont and whitespring students 
# Adding variable of user.... this will give every user a name and call back using the variable x
username = "BrownPortal"

def rps():
    user = input(f"Hey {username}, please make your choice \n'r' for rock. \n's' for scissor \n'p' for paper \n")
    # backward slah was used to jump to the next line as seen above
    comp = random.choice(['r', 'p', 's'])
    # random.choice([1,2,'5']) it could be Rock, Paper or Scissors

    if user == comp:
        return (f"Oh {username}, it's a tie. comp chose {comp}")
        # print('checking')

    if win(user, comp):
        return (f'Hurray {username} you won. Comp chose {comp}')

    return(f'Sorry {username} you lost. Comp chose {comp}')

def win(player, opponent):
    if (player == 'r' and opponent == 's') \
            or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True
        
print(rps())
