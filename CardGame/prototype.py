import random
import copy
'''
lambda arguments: expression

add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8
'''

MAX_PLAYER_HAND = 7

def displayBox(msg):
    finalmsg = []
    index = 0
    msg = msg.split('\n')
    for i in range(len(msg)):
        line = msg[i]
        finalmsg.append('')
        tokens = line.split(' ')
        for token in tokens:
            if len(finalmsg[index]) + len(token) >= 50:
                finalmsg.append('    '+token)
                index += 1
            else:
                finalmsg[index] += ' '+token
        index += 1
    print('+' + ('='*100) + '+')
    for row in finalmsg:
        print('|'+ row.ljust(75).center(100)+'|')
    print('+' + ('='*100) + '+')

#Creation of Data
class Card:
    def __init__(self, name, text, defaultVals, effects):
        self.name = name
        self.text = text
        self.vals = defaultVals
        self.effects = effects

    def modifyVar(self, var, val):
        self.vals[var] = val

    def discard(self):
        pass

    def __str__(self):
        newtext = self.text
        for key in self.vals:
            newtext = newtext.replace(key, str(self.vals[key]))
        return self.name + ": " + newtext

class EffectPacket:
    def __init__(self, card):
        self.target = None
        self.source = None
        self.effects = {
            'heal': None,
            'damage': None,
            'damageModifier': None,
            'damageType': None,
            'infliction': None,
            'frost': None,
            'weak': None,
            'adaptable': None,
            'cardCreation': None
        }
    
    def heal(self, val):
        self.effects['heal'] = val
        return self
    
    def damage(self, val, type):
        self.effects['damage'] = val
        self.effects['damageType'] = type
        return self
    
    def damageModifier(self, val, type):
        self.effects['damageModifier'] = val
        self.effects['damageType'] = type
        return self

    def infliction(self, val):
        self.effects['infliction'] = val
        return self

    def frost(self, val):
        self.effects['frost'] = val
        return self
    
    def weak(self, val):
        self.effects['weak'] = val
        return self

    def adaptable(self, val):
        self.effects['adaptable'] = val
        return self
    
    def cardCreation(self, cardToCopy, modifiers):
        for val in modifiers:
            copiedCard.modifyVar(val, copiedCard.vals[val] + modifiers[val])
        self.effects['cardCreation'] = copiedCard
        return self
    
    def cardDuplication(self, modifiers):
        pass

    def target(self, target):
        self.target = target
        return self

    def source(self, source):
        self.source = source
        return self


class Potion:
    def __init__(self):
        self.effects = []
        self.vars = {}

    def addEffect(self, effect):
        self.effects.append(effect)
    
    def setModifier(self, var, val):
        self.vars[var] = val

    def doPotion(self, source, target):
        pass

class Player:
    def __init__(self, maxHealth, deck):
        self.hand = []
        self.deck = deck
        self.maxHealth = maxHealth
        self.health = maxHealth
        self.statuses = {
            'infliction': 0,
            'frost': 0,
            'weak': 0
        }
        self.tempCards = []
        self.potions = []

    def drawCard(self):
        if self.handSize() >= 7 or len(self.deck) <= 0:
            return False
        self.hand.append(self.deck.pop())
        return True

    def gainCard(self, card):
        if self.handSize() >= 7:
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
        todisp = 'Your hand:\n\n'
        first = True
        for i,card in enumerate(self.hand):
            if not first:
                todisp += '\n'
            else:
                first = False
            todisp += str(i)+'. ' + card.__str__()
        displayBox(todisp)

    def displayStats(self):
        statstr = 'Health: ' + str(self.health)
        displayBox(statstr)

    def displayMenu(self):
        self.displayHand()
        self.displayStats()
        displayBox('What will you do now?\n' + 
                   '1. Craft Potion\n'+
                   '2. Place Potion\n' +
                   '3. Throw Potion\n' +
                   '4. Drink Potion\n' +
                   '5. End Turn')

    def startGame(self):
        for i in range(5):
            self.drawCard()

    def takeTurn(self):
        self.drawCard()
        while True:
            self.displayMenu()
            ui = input()
            while len(ui) > 1 or not ui.isnumeric():
                ui = input('Invalid Input. Try again: ')
            val = int(ui)
            if val == 1:
                self.displayHand()
                cardsToPlayStr = input('Which cards will you play? Enter as a comma-separated list (ex: 1,2,4) ')
                cardsToPlay = cardsToPlayStr.split(",")
                cardsToPlay = [int(i) for i in cardsToPlay] 
                p = Potion()
                for card in cardsToPlay:
                    for effect in card.effects:
                        p.add(effect)
            elif val == 2:
                pass
            elif val == 3:
                pass
            elif val == 4:
                pass
            elif val == 5:
                pass

    def applyEffects(self, effects):
        pass

    def dealStatuses(self):
        pass

    def giveTempCard(self, card):
        if len(self.hand) < 7:
            self.hand.append(card)
        else:
            displayBox('Hand is too full!')

    def heal(self, val):
        pass

class CPUPlayer(Player):
    def takeTurn(self):
        pass

class Game:
    def __init__(self):
        self.player1 = None
        self.player2 = None

    def addPlayers(self, player1, player2):
        self.player1 = player1
        self.player2 = player2



#-------------------Initialize All Cards

duplicatePlaceholder = None

# smoodelite needs an object that we can make copies out of
smoodelite = Card('Smoodelite', 'Adds a temporary smoodelite to potionmaker\'s hand but with 1 more damage. Does +@X damage', {'@X':1},
         [EffectPacket()])
smoodelite.effects[0].cardCreation(smoodelite, {'@X':1})
card_reg = [
    Card('Healium', 'Restores target health by @X', {'@X': 1},
         [ EffectPacket().heal('@X')]),
    Card('Corrosite', 'Adds @X \'Infliction\' to target', {'@X': 1},
         [EffectPacket().infliction('@X')]),
    Card('Slogium', 'Adds @X \'Frost\' to target', {'@X': 1}, 
         [EffectPacket().frost('@X')]),
    Card('Angrium', 'Makes target \'Weak\' (@X). Adds @Y damage to target', {'@X':1, '@Y':10}, 
         [EffectPacket().weak('@X').damageModifier(10,'rage')]),
    smoodelite,
    Card('Spedesium', 'If three of these are in your potion, your next potion happens twice', {},[]),
    Card('Energy Core', 'Makes your potion deal @X damage (*Adaptable*)', {'@X':1},
         [EffectPacket().damage('@X', 'neutral')])
]

def generateDeck():
    deck = []
    for card in card_reg:
        for i in range(3):
            deck.append(copy.deepcopy(card))

    random.shuffle(deck)

    return deck

playingGame = True

deck = generateDeck()

p1 = Player(10, deck)
p1.startGame()

while playingGame:
    p1.takeTurn()