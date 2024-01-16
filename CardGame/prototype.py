import random
'''
lambda arguments: expression

add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8
'''

MAX_PLAYER_HAND = 7

def displayBox(msg):
    if len(msg) > 20:
        msg = [msg[i*20:(i+1)*20] for i in range(0, len(msg, 20))]
    else:
        msg = [msg]
    print('+' + ('='*20) + '+')
    for row in msg:
        print('|'+ msg.center(20)+'|')
    print('+' + ('='*20) + '+')

#Creation of Data
class Card:
    def __init__(self, name, text, effect):
        self.name = name
        self.text = text
        self.effect = effect

    def __str__(self):
        return "\t" + self.name + ": " + self.effect

class Effect:
    def __init__(self, name, target, effectFunc):
        self.name = name
        self.target = target
        self.effectFunc = effectFunc

class Potion:
    def __init__(self):
        self.effects = []

    def addEffect(self, effect):
        self.effects.append(effect)

class Player:
    def __init__(self, maxHealth):
        self.hand = []
        self.maxHealth = maxHealth
        self.health = maxHealth

    def gainCard(self, card):
        if(self.handSize() >= 7):
            return False
        self.hand.append(card)
        return True

    def playCard(self, index):
        card = self.index.pop[index]
        self.index.pop(index)
        return card
    
    def handSize(self):
        return len(self.hand)

    def displayHand(self):
        todisp = 'Your hand:\n'
        first = True
        for card in self.hand:
            if not first:
                todisp += '\n'
            else:
                first = False
            todisp += card.__str__()
        displayBox(todisp)

    def displayStats(self):
        statstr = 'Health: ' + self.health
        displayBox(statstr)

    def displayMenu(self):
        self.displayHand()
        self.displayStats()
        displayBox('What will you do now?\n' + 
                   '\t1. Play Card\n'+
                   '\t2. Play Potion\n' +
                   '\t3. End Turn')

    def takeTurn(self):
        while True:
            self.displayMenu()
            ui = input()
            while len(ui) > 1 or not ui.isnumeric():
                ui = input('Invalid Input. Try again: ')
            val = int(ui)
            if val == 1:
                self.displayHand()
                print('Which card will you play?')
            elif val == 2:
                pass
            elif val == 3:
                break

    def applyPotion(self, potion, target):
        pass

class CPUPlayer(Player):
    def takeTurn(self):
        pass

class Game:
    pass

#Initialize All Cards
card_reg = [
    Card('Healium', 'Restores Your Health', Effect(
        
    )),
    Card('Corrosite', 'Adds 1 \'Infliction\' to enemy', Effect(

    )),
    Card('Slogium', 'Adds 1 \'Frost\' to enemy', Effect(

    )),
]