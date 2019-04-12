import random

class Card:
    def __init__(self,suit,face):
        self.suit = suit
        self.face = face
    def __repr__(self):
        return f"Card({self.suit},{self.face})"
    def __str__(self):
        return f"{self.face} of {self.suit}."

class Deck:
    suits  =["Spades","Clubs","Diamonds","Hearts"]
    values = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
    def __init__(self):
        self.deck = []
    
    def get_deck(self):
        for s in self.suits:
            for v in self.values:
                self.deck.append(Card(s,v))
    def shuffle(self):
        newd = []
        if len(self.deck) > 0:
            while len(newd) < 52:
                newc = random.choice(self.deck)
                try:
                    assert newc not in newd
                except AssertionError:
                    while newc in newd:
                        newc = random.choice(self.deck)
                        
                newd.append(newc)
        self.deck = newd
    
    def deal(self,cards,players):
        for i in range(cards):
            for j in players:
                j.hand.append(self.deck[i])
                self.deck.pop(i)

class Player:
    def __init__(self,name,funds):
        self.name = name
        self.hand = []
        self.funds = funds
    def __repr__(self):
        return (f"A Player object: Player({type(self.name)}:{self.name},"+
                f"{type(self.funds)}:{self.funds})")
    def __str__(self):
        return f"I am a player, name: {self.name}. Funds: {self.funds}"
players = [Player("dave",200),Player("bob",400)]

     
d = Deck()

d.get_deck()
d.shuffle()
print(d.deck)
d.deal(5,players)
print(len(d.deck))
for player in players:
    print(player.__repr__())
    
newcard = Card("Hearts","Ace")

print(newcard)