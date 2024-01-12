'''
lambda arguments: expression

add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8
'''

MAX_PLAYER_HAND = 7

#Creation of Data
class Card:
    def __init__(self, name, text, effect):
        self.name = name
        self.text = text
        self.effect = effect

    def __str__(self):
        return "\t" + self.name + ": " + self.effect
    
    def doEffect(self):
        self.effect()

class Potion:
    def __init__(self):
        self.potions = []

    def addPotion(self, potion):
        self.potions.append(potion)

class Player:
    def __init__(self):
        self.hand = []

    def gainCard(self, card):
        self.hand.append(card)

    def playCard(self, ):


    def takeTurn():
        pass

class Game:
    pass