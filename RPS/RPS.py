import random
print("Let's Play Rock, Paper, Scissors!!!")
pChoice = input('Choose one of the following: rock, paper, scissors, or quit: ')
while pChoice != 'quit':
    choices = ("rock", "paper", "scissors")
    cChoice = random.choice(choices)
    print("You chose: "+ pChoice)
    print("Computer chose: "+ cChoice)
    if pChoice == cChoice:
        print('Tie')
    elif pChoice == 'scissors':
        if cChoice == 'rock':
            print('You lost!')
        else:
            print('You won!')
    elif pChoice == 'rock':
        if cChoice == 'scissors':
            print('You won!')
        else:
            print('You lost!')
    elif pChoice == 'paper':
        if cChoice == 'scissors':
            print('You lost!')
        else:
            print("You won!")
    else:
        print('TypeError: Can not read inputed information')
        
    pChoice = input('Choose one of the following: rock, paper, scissors, or quit: ')
