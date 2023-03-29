import random
import pygame, sys

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and click conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
        
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action


class Card:
    rank = ["two","three","four","five","six","seven","eight","nine","ten","jack","queen","king","ace"]
    suit = ["clubs", "dimonds", "hearts", "spades"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.cards = {"ace of clubs" : 11, "ace of dimonds" : 11, "ace of hearts" : 11, "ace of spades" : 11,
"eight of clubs" : 8, "eight of dimonds" : 8, "eight of hearts" : 8, "eight of spades" : 8, 
"five of clubs" : 5, "five of dimonds" : 5,"five of hearts" : 5, "five of spades" : 5,
"four of clubs" : 4, "four of dimonds" : 4,"four of hearts" : 4, "four of spades" : 4,
"jack of clubs" : 10, "jack of dimonds" : 10,"jack of hearts" : 10, "jack of spades" : 10,
"king of clubs" : 10, "king of dimonds" : 10,"king of hearts" : 10, "king of spades" : 10,
"nine of clubs" : 9, "nine of dimonds" : 9,"nine of hearts" : 9, "nine of spades" : 9,
"queen of clubs" : 10, "queen of dimonds" : 10,"queen of hearts" : 10, "queen of spades" : 10,
"seven of clubs" : 7, "seven of dimonds" : 7,"seven of hearts" : 7, "seven of spades" : 7,
"six of clubs" : 6, "six of dimonds" : 6,"six of hearts" : 6, "six of spades" : 6,
"ten of clubs" : 10, "ten of dimonds" : 10,"ten of hearts" : 10, "ten of spades" : 10,
"three of clubs" : 3, "three of dimonds" : 3,"three of hearts" : 3, "three of spades" : 3,
"two of clubs" : 2, "two of dimonds" : 2,"two of hearts" : 2, "two of spades" : 2}
    
    def __repr__(self):
        return f"{Card.rank[self.rank]} of {Card.suit[self.suit]}"
    
    def total_count(self, card): 
        return self.cards.get(card)
        

class Deck:
    def __init__(self):
        self.deck = []
        for suit in range(4):
            for rank in range(13):
                self.deck.append(Card(rank, suit))
        self.shuffle()

    def __len__(self):
        return len(self.deck)
    
    def add_card(self, card):
        self.deck.append(card)

    def pop_card(self):
        return self.deck.pop()

    def shuffle(self):
        random.shuffle(self.deck)

# card = Card(rank="",suit="")
# deck = Deck()
# card.total_count(deck.pop_card())
