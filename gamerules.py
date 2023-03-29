from button import Card, Deck



class GameRules():

    def __init__(self):
        self.delt_cards = []
        self.player_cards = []
        self.dealer_cards = []
        self.aces = 'ace of clubs ace of dimonds ace of hearts ace of spades'
        self.player_total = []
        self.dealer_total = []
        self.current_deck = Deck()
        self.current_card = Card(rank="",suit="")


    def player_hand_start(self):
        start_card = self.current_deck.pop_card()
        self.player_cards.append(start_card)
        self.player_hand_count()
        return start_card
        

    def dealer_hand_start(self):
        start_card = self.current_deck.pop_card()
        self.dealer_cards.append(start_card)
        for card in self.player_cards:   
            if card in self.dealer_cards:
                self.dealer_cards.pop()
                self.dealer_hand_start()
        return start_card
            

    def player_hand_count(self):
        if len(self.player_total) != 0:
            self.player_total.clear()
        total = 0
        for card_total in self.player_cards:
            total += self.current_card.total_count(str(card_total))    
        if total > 21:
            for ace in self.player_cards:
                if total > 21:    
                    if str(ace) in self.aces:
                        total -= 10
                else:
                    break
            self.player_total.append(total)
        if len(self.player_total) == 0:
            self.player_total.append(total)
        if self.player_total[0] > 21:
            return 'you lose'
        

    def dealer_hand_count(self):
        if len(self.dealer_total) != 0:
            self.dealer_total.pop()
        total = 0
        for card_total in self.dealer_cards:
            total += self.current_card.total_count(str(card_total))    
        if total > 21:
            for ace in self.dealer_cards:
                if total > 21:    
                    if str(ace) in self.aces:
                        total -= 10
                else:
                    break
            self.dealer_total.append(total)
        if len(self.dealer_total) == 0:
            self.dealer_total.append(total)  
            
    def player_hit(self):
        hit_card = self.current_deck.pop_card()
        self.player_cards.append(hit_card)
        self.player_hand_count()
        return hit_card

    def player_stand(self):
        self.dealer_hand_count()

    def dealers_play(self):
        dealer_hit_card = self.current_deck.pop_card()
        self.dealer_cards.append(dealer_hit_card)
        self.dealer_hand_count()
        return dealer_hit_card
    
    def remove_cards(self):
        self.delt_cards = []
        self.player_cards = []
        self.dealer_cards = []
        self.player_total = []
        self.dealer_total = []
        self.current_deck.__init__()

# player = GameRules()

# print(player.player_hand_start())
# print(player.player_hand_start())
# print(player.player_total)
# print(player.player_hit())
# print(player.player_total)
# print(player.player_hit())
# print(player.player_total)
# print(player.player_cards)