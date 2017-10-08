# A computer verion of Blackjack
import random
def changelog():
    print('''
Changelog:
    This game is updated almost every day
    This is a WIP game
    Thanks for all your support! -Devon Chang
''')
print('Welcome to Blackjack!')
print('By Devon Chang.')
changelog()
ask = input('Wanna play? Yes or no: ')
if ask.lower() == 'yes':
    print('''In this game, you will be playing with the dealer (CPU).
Each of you will start off with $2500.''')
    playerMoney = 2500
    dealerMoney = 2500
    # Gameplay
    while True:
        cards = {'ace':1,'ace':1,'ace':1,'ace':1,'2':2,'2':2,'2':2,'2':2,'3':3,'3':3,'3':3,'3':3,'4':4,'4':4,'4':4,'4':4,'5':5,'5':5,'5':5,'5':5,'6':6,'6':6,'6':6,'6':6,'7':7,'7':7,'7':7,'7':7,'8':8,'8':8,'8':8,'8':8,'9':9,'9':9,'9':9,'9':9,'10':10,'10':10,'10':10,'10':10,'jack':10,'jack':10,'jack':10,'jack':10,'queen':10,'queen':10,'queen':10,'queen':10,'king':10,'king':10,'king':10,'king':10}
        card = ['ace','ace','ace','ace','2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8','9','9','9','9','10','10','10','10','jack','jack','jack','jack','queen','queen','queen','queen','king','king','king','king']

        print('You now have: $%s'%playerMoney)
        money = int(input('How much do you want to bet? (Maximum of 2500): '))
        if money > 2500:
            print('You cannot bet higher than 2500.')
            break
        
        number = 0
        dealerNumber = 0
        face1 = random.choice(card)
        face2 = random.choice(card)
        print('Your two cards are: %s and %s'%(face1,face2))
        card1 = cards[face1]
        card2 = cards[face2]
        number += card1
        number += card2
        print('Your total points so far: %s'%number)

        face1 = random.choice(card)
        face2 = random.choice(card)
        card1 = cards[face1]
        card2 = cards[face2]
        dealerNumber += card1
        dealerNumber += card2
        stop = False
        astop = False
        while True:
            if stop == False:
                more = input('Do you want to hit or stand: ').lower()
                if more == 'hit':
                    face = random.choice(card)
                    card3 = cards[face]
                    print('You got: %s'%face)
                    number += card3
                    print('You now have %s points'%number)
                    if number > 21:
                        print('You burst!!!')
                        print('You lost $%s'%money)
                        playerMoney -= money
                        print('You now have: $%s'%playerMoney)
                        dealerMoney += money
                        print('The dealer now has: $%s'%dealerMoney)
                        break
                    elif number == 21:
                        print('BLACKJACK!!!')
                        stop = True
                elif more == 'stand':
                    stop = True
                else:
                    assert False, "That is not an option!"


            else:
                if dealerNumber <= 11:
                    face = random.choice(card)
                    card3 = cards[face]
                    number += card3
                else:
                    if astop == False:
                        if dealerNumber == 12:
                            chance = random.randint(1,100)
                            if chance <= 95:
                                face = random.choice(card)
                                card3 = cards[face]
                                number += card3
                            else:
                                astop = True
                        elif dealerNumber == 13:
                            chance = random.randint(1,100)
                            if chance <= 75:
                                face = random.choice(card)
                                card3 = cards[face]
                                number += card3
                            else:
                                astop = True
                        elif dealerNumber == 14:
                            chance = random.randint(1,100)
                            if chance <= 65:
                                face = random.choice(card)
                                card3 = cards[face]
                                number += card3
                            else:
                                astop = True
                        elif dealerNumber == 15:
                            chance = random.randint(1,100)
                            if chance <= 45:
                                face = random.choice(card)
                                card3 = cards[face]
                                number += card3
                            else:
                                astop = True
                        elif dealerNumber == 16:
                            chance = random.randint(1,100)
                            if chance <= 40:
                                face = random.choice(card)
                                card3 = cards[face]
                                number += card3
                            else:
                                astop = True
                        elif dealerNumber == 17:
                            chance = random.randint(1,100)
                            if chance <= 30:
                                face = random.choice(card)
                                card3 = cards[face]
                                number += card3
                            else:
                                astop = True
                        elif dealerNumber == 18:
                            chance = random.randint(1,100)
                            if chance <= 20:
                                face = random.choice(card)
                                card3 = cards[face]
                                number += card3
                            else:
                                astop = True
                        elif dealerNumber == 19:
                            chance = random.randint(1,100)
                            if chance <= 5:
                                face = random.choice(card)
                                card3 = cards[face]
                                number += card3
                            else:
                                astop = True
                        elif dealerNumber == 20:
                            chance = random.randint(1,100)
                            if chance <= 1:
                                face = random.choice(card)
                                card3 = cards[face]
                                number += card3
                            else:
                                astop = True
                    else:
                        if number > dealerNumber:
                            print("Dealer points:",str(dealerNumber))
                            print('You won $%s'%money)
                            playerMoney += money
                            print('You now have: $%s'%playerMoney)
                            print('The dealer lost $%s'%money)
                            dealerMoney -= money
                            print('He now has: $%s'%dealerMoney)
                            break
                        elif number < dealerNumber:
                            print("Dealer points:",str(dealerNumber))
                            print('You lost $%s'%money)
                            playerMoney -= money
                            print('You now have: $%s'%playerMoney)
                            print('The dealer won $%s'%money)
                            dealerMoney += money
                            print('He now has: $%s'%dealerMoney)
                            break
                        elif number == dealerNumber:
                            print("Dealer points:",str(dealerNumber))
                            print('Its a tie.')
                            print('Nobody won anything.')
                if dealerNumber > 21:
                    print("Dealer points:",str(dealerNumber))
                    print('The dealer burst!')
                    print('You won $%s'%money)
                    print('You now have: $%s'%playerMoney)
                    print('The dealer lost $%s'%money)
                    print('He now has: $%s'%dealerMoney)
                    break
        if playerMoney < 1:
            print('You ran out of money!!!')
            break
        elif dealerMoney < 1:
            print('The dealer ran out of money!!!')
            break
else:
    print('...')
