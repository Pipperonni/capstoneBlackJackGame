import json
import pygame, sys, time
from sys import exit
import random
import button
from gamerules import GameRules as gr
import asyncio


pygame.init()
screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('BlackJack')
clock = pygame.time.Clock()
game_active = False
game_round = False
current_time = 0
button_press_time = 0
BLACK = (0, 0, 0)

playing_cards = {"ace of clubs" : "image/aceofclubs.png", "ace of dimonds" : "image/aceofdimonds.png", 
"ace of hearts" : "image/aceofhearts.png", "ace of spades" : "image/aceofspades.png",
"eight of clubs" : "image/eightofclubs.png", "eight of dimonds" : "image/eightofdimonds.png", 
"eight of hearts" : "image/eightofhearts.png", "eight of spades" : "image/eightofspades.png", 
"five of clubs" : "image/fiveofclubs.png", "five of dimonds" : "image/fiveofdimonds.png",
"five of hearts" : "image/fiveofhearts.png", "five of spades" : "image/fiveofspades.png",
"four of clubs" : "image/fourofclubs.png", "four of dimonds" : "image/fourofdimonds.png",
"four of hearts" : "image/fourofhearts.png", "four of spades" : "image/fourofspades.png",
"jack of clubs" : "image/jackofclubs.png", "jack of dimonds" : "image/jackofdimonds.png",
"jack of hearts" : "image/jackofhearts.png", "jack of spades" : "image/jackofspades.png",
"king of clubs" : "image/kingofclubs.png", "king of dimonds" : "image/kingofdimonds.png",
"king of hearts" : "image/kingofhearts.png", "king of spades" : "image/kingofspades.png",
"nine of clubs" : "image/nineofclubs.png", "nine of dimonds" : "image/nineofdimonds.png",
"nine of hearts" : "image/nineofhearts.png", "nine of spades" : "image/nineofspades.png",
"queen of clubs" : "image/queenofclubs.png", "queen of dimonds" : "image/queenofdimonds.png",
"queen of hearts" : "image/queenofhearts.png", "queen of spades" : "image/queenofspades.png",
"seven of clubs" : "image/sevenofclubs.png", "seven of dimonds" : "image/sevenofdimonds.png",
"seven of hearts" : "image/sevenofhearts.png", "seven of spades" : "image/sevenofspades.png",
"six of clubs" : "image/sixofclubs.png", "six of dimonds" : "image/sixofdimonds.png",
"six of hearts" : "image/sixofhearts.png", "six of spades" : "image/sixofspades.png",
"ten of clubs" : "image/tenofclubs.png", "ten of dimonds" : "image/tenofdimonds.png",
"ten of hearts" : "image/tenofhearts.png", "ten of spades" : "image/tenofspades.png",
"three of clubs" : "image/threeofclubs.png", "three of dimonds" : "image/threeofdimonds.png",
"three of hearts" : "image/threeofhearts.png", "three of spades" : "image/threeofspades.png",
"two of clubs" : "image/twoofclubs.png", "two of dimonds" : "image/twoofdimonds.png",
"two of hearts" : "image/twoofhearts.png", "two of spades" : "image/twoofspades.png"}

table_surface = pygame.image.load('image/pokertable.png').convert_alpha()

players_chip_count = []

with open('players_chips.txt') as players_file:
    players_chip_count = json.load(players_file)

bet_counter = 0
card_deck = pygame.image.load("image/backofcards.png").convert_alpha()
# Player hit cards
card_deck_x_position = 40
card_deck_y_position = 70
card_deck_x_position2 = 40
card_deck_y_position2 = 70
card_deck_x_position3 = 40
card_deck_y_position3 = 70
card_deck_x_position4 = 40
card_deck_y_position4 = 70
# Game ends in Draw
card_draw_x_position = 40
card_draw_y_position = 70
card_draw_x_position2 = 40
card_draw_y_position2 = 70
card_draw_x_position3 = 40
card_draw_y_position3 = 70
card_draw_x_position4 = 40
card_draw_y_position4 = 70
# Dealer hit cards
card_dealer_x_position = 40
card_dealer_x_position2 = 40
card_dealer_x_position3 = 40
card_dealer_x_position4 = 40

player = gr()

async def start_game():
    player.player_hand_start()
    player.player_hand_start()
    player.dealer_hand_start()
    player.dealer_hand_start()
    await asyncio.sleep(0.1)
    
def starting_cards_image():   
    player_first_card = playing_cards[f'{player.player_cards[0]}']
    player_second_card = playing_cards[f'{player.player_cards[1]}']
    dealer_first_card = playing_cards[f'{player.dealer_cards[0]}']
    screen.blit(pygame.image.load(player_first_card), (500,296))
    screen.blit(pygame.image.load(player_second_card), (650,296))
    screen.blit(pygame.image.load(dealer_first_card), (500,70))

def start_dealer_second_card():
    dealer_second_card = playing_cards[f'{player.dealer_cards[1]}']
    return dealer_second_card  

def player_score():
    players_score = pygame.font.Font(None, 50)
    ps = players_score.render((f'Player Score: {player.player_total[0]}'), False, 'Black')
    screen.blit((ps), (300,500))

def bet_amount():
    players_bet_amount = pygame.font.Font(None, 32)
    pba = players_bet_amount.render(f'Bet: {bet_counter}', False, '#c12929')
    pba_screen = screen.blit(pba, (807, 530))
    return pba_screen

def players_current_chip_amount():
    players_chip_amount = pygame.font.Font(None, 32)
    pca = players_chip_amount.render(f'Chip Amount: {players_chip_count[0]}', False, 'Black')
    pca_screen = screen.blit(pca, (702, 560))
    return pca_screen

def new_player_chip_count():
    if len(players_chip_count) == 0:
        players_chip_count.append(1000)

def players_bet():
    new_player_chip_amount = players_chip_count[0] - bet_counter
    players_chip_count.pop()
    players_chip_count.append(new_player_chip_amount)

def player_wins():
    win_chip_amount = players_chip_count[0] + (bet_counter * 2)
    players_chip_count.pop()
    players_chip_count.append(win_chip_amount)

def player_draw_bet():
    draw_chip = players_chip_count[0] + bet_counter
    players_chip_count.pop()
    players_chip_count.append(draw_chip)

def players_broke():
    if players_chip_count[0] == 0:
        players_chip_count.pop()
        players_chip_count.append(1000)

def player_stands():
    player.player_stand()

async def dealer_hits():
    hit_card = player.dealers_play()
    await asyncio.sleep(.1)
    return hit_card


def dealer_score():
    dealers_score = pygame.font.Font(None, 50)
    ds = dealers_score.render((f'Dealer Score: {player.dealer_total[0]}'), False, 'Black')
    screen.blit((ds), (300,10))

player_bust = pygame.image.load("image/bustedlogo.png").convert()
player_bust1s = pygame.transform.scale(player_bust, (60,28))
player_bust1r = pygame.transform.rotate(player_bust1s, 45)

canvas = pygame.Surface((1200,600))
end_round = pygame.image.load("image/end_roundb.png").convert_alpha()
rect = end_round.get_rect(center=(1200/2,600/2))
alpha = 255

  
confirm_button = pygame.image.load("image/confirm_btn.png").convert_alpha()   
betting_10 = pygame.image.load("image/bet_10_btn.png").convert_alpha()
betting_50 = pygame.image.load("image/bet_50_btn.png").convert_alpha()
betting_100 = pygame.image.load("image/bet_100_btn.png").convert_alpha()
minus_10 = pygame.image.load("image/minus_bet_10_btn.png").convert_alpha()
minus_50 = pygame.image.load("image/minus_bet_50_btn.png").convert_alpha()
minus_100 = pygame.image.load("image/minus_bet_100_btn.png").convert_alpha()
quit_game = pygame.image.load("image/quitbtn.png").convert_alpha()
start_button = pygame.image.load("image/startbutton.png").convert_alpha()
hit_button = pygame.image.load("image/hitbutton.png").convert_alpha()
deal_button = pygame.image.load("image/dealbutton.png").convert_alpha()
stand_button = pygame.image.load("image/standbutton.png").convert_alpha()


bet_10 = button.Button(1000, 500, betting_10, 1)
bet_50 = button.Button(1050, 500, betting_50, 1)
bet_100 = button.Button(1100, 500, betting_100, 1)

min_10 = button.Button(1000, 530, minus_10, 1)
min_50 = button.Button(1050, 530, minus_50, 1)
min_100 = button.Button(1100, 530, minus_100, 1)

confirm_bet_btn = button.Button(1000, 560, confirm_button, 1)

quit_btn = button.Button(525, 450, quit_game, 1)
stand_btn = button.Button(50, 275, stand_button, 1)
deal_btn = button.Button(525, 375, deal_button, 1)
start_btn = button.Button(525, 275, start_button, 1)
ht_btn = button.Button(50, 375, hit_button, 1)
hb = pygame.USEREVENT + 1
pygame.time.set_timer(hb, 30)



show_image = False
show2_image = False
show3_image = False
show4_image = False
dealer_hide_card = True
hit_button_pressed = False
hit_button_pressed_ani = False
hit_button_pressed_ani2 = False
hit_button_pressed_ani3 = False
hit_button_pressed_ani4 = False
pressed = 0
start = True
stand = True
d_score = False
dealer_under_17 = 0
dealer_hit_ani = False
dealer_hit_ani2 = False
dealer_hit_ani3 = False
dealer_hit_ani4 = False
dealer_hit_card1 = False
dealer_hit_card2 = False
dealer_hit_card3 = False
dealer_hit_card4 = False
card_speed = 5
busted_angle = 0
busted_width = 60
busted_height = 28
busted_ani = False
player_win = False
stand_mes = False
finishhim = False
player_lose = False
plose1 = False
round_draw = False
draw_card = 0
draw_cards = False
draw_cards2 = False
draw_cards3 = False
draw_cards4 = False
draw_image = False
draw_image2 = False
draw_image3 = False
draw_image4 = False
round_done = False
confirm_bet = False


while True:

       
    
    if game_active == False:
        screen.blit(pygame.image.load("image/titlepage.png"), (0, -20))
        if start_btn.draw(screen):
            asyncio.run(start_game())
            new_player_chip_count()
            game_active = True
            game_round = True

    if game_active:

        if game_round == False:
            if quit_btn.draw(screen):
                with open('players_chips.txt', 'w') as players_file:
                    json.dump(players_chip_count, players_file)
                pygame.quit()
                exit()    
            if deal_btn.draw(screen):
                players_broke()
                bet_counter = 0
                confirm_bet = False
                round_done = False
                draw_cards = False
                draw_cards2 = False
                draw_cards3 = False
                draw_cards4 = False
                draw_card = 0
                round_draw = False
                player_lose = False
                stand_mes = False
                finishhim = False
                player_win = False
                busted_angle = 0
                busted_width = 60
                busted_height = 28
                stand = True
                d_score = False
                show_image = False
                show2_image = False
                show3_image = False
                show4_image = False
                draw_image = False
                draw_image2 = False
                draw_image3 = False
                draw_image4 = False
                pressed = 0
                dealer_under_17 = 0
                dealer_hit_card1 = False
                dealer_hit_card2 = False
                dealer_hit_card3 = False
                dealer_hit_card4 = False
                dealer_hide_card = True
                card_deck_x_position = 40
                card_deck_y_position = 70
                card_deck_x_position2 = 40
                card_deck_y_position2 = 70
                card_deck_x_position3 = 40
                card_deck_y_position3 = 70
                card_deck_x_position4 = 40
                card_deck_y_position4 = 70
                card_draw_x_position = 40
                card_draw_y_position = 70
                card_draw_x_position2 = 40
                card_draw_y_position2 = 70
                card_draw_x_position3 = 40
                card_draw_y_position3 = 70
                card_draw_x_position4 = 40
                card_draw_y_position4 = 70
                card_dealer_x_position = 40
                card_dealer_x_position2 = 40
                card_dealer_x_position3 = 40
                card_dealer_x_position4 = 40
                player.remove_cards()
                asyncio.run(start_game())
                game_round = True

        if game_round:

            for event in pygame.event.get():
                screen.blit(table_surface,(0,0))
                screen.blit(card_deck,(40,70))

                starting_cards_image()
                if dealer_hide_card:
                    screen.blit(pygame.image.load("image/backofcards.png"), (650,70))
                else:
                    screen.blit(pygame.image.load(start_dealer_second_card()), (650,70))
                
                bet_amount()
                players_current_chip_amount()

                if confirm_bet == False:
                    if bet_10.draw(screen):
                        if bet_counter + 10 <= players_chip_count[0]:
                            bet_counter += 10
                    if bet_50.draw(screen):
                        if bet_counter + 50 <= players_chip_count[0]:
                            bet_counter += 50
                    if bet_100.draw(screen):
                        if bet_counter + 100 <= players_chip_count[0]:
                            bet_counter += 100
                    if min_10.draw(screen):
                        if bet_counter - 10 >= 0:
                            bet_counter -= 10
                    if min_50.draw(screen):
                        if bet_counter - 50 >= 0:
                            bet_counter -= 50
                    if min_100.draw(screen):
                        if bet_counter - 100 >= 0:
                            bet_counter -= 100
                    if confirm_bet_btn.draw(screen):
                        players_bet()
                        confirm_bet = True                        
                
                if confirm_bet:
                    if stand_btn.draw(screen):
                        stand_mes = True

                if stand == False:
                    if player.dealer_total[0] < 17:
                        if dealer_under_17 == 0:
                            dealer_hit_ani = True
                        elif dealer_under_17 == 1:
                            dealer_hit_ani2 = True
                        elif dealer_under_17 == 2:
                            dealer_hit_ani3 = True
                        elif dealer_under_17 == 3:
                            dealer_hit_ani4 = True
                    else: 
                        if player.dealer_total[0] < player.player_total[0]:
                            player_win = True
                            
                        elif player.dealer_total[0] > 21:
                            player_win = True
                            
                        elif player.dealer_total[0] > player.player_total[0]:
                            player_lose = True
                            
                        elif player.dealer_total[0] == player.player_total[0]:
                            round_draw = True
                    
                if dealer_hit_ani:
                    if card_dealer_x_position <= 200:
                        card_dealer_x_position += 11
                    else:
                        if dealer_under_17 == 0:
                            dhit1 = asyncio.run(dealer_hits())
                            dealer_hit_card1 = True
                            dealer_under_17 += 1
                        dealer_hit_ani = False
                
                if dealer_hit_card1 == False:
                    screen.blit(card_deck,(card_dealer_x_position, 70))
                if dealer_hit_card1:
                    screen.blit(pygame.image.load(playing_cards[f'{dhit1}']), (200,70))
                
                if dealer_hit_ani2:
                    if card_dealer_x_position2 <= 350:
                        card_dealer_x_position2 += 17
                    else:
                        if dealer_under_17 == 1:
                            dhit2 = asyncio.run(dealer_hits())
                            dealer_hit_card2 = True
                            dealer_under_17 += 1
                        dealer_hit_ani2 = False
                
                if dealer_hit_card2 == False:
                    screen.blit(card_deck,(card_dealer_x_position2, 70))
                if dealer_hit_card2:
                    screen.blit(pygame.image.load(playing_cards[f'{dhit2}']), (350,70))
                
                if dealer_hit_ani3:
                    if card_dealer_x_position3 <= 800:
                        card_dealer_x_position3 += 50
                    else:
                        if dealer_under_17 == 2:
                            dhit3 = asyncio.run(dealer_hits())
                            dealer_hit_card3 = True
                            dealer_under_17 += 1
                        dealer_hit_ani3 = False
                
                if dealer_hit_card3 == False:
                    screen.blit(card_deck,(card_dealer_x_position3, 70))
                if dealer_hit_card3:
                    screen.blit(pygame.image.load(playing_cards[f'{dhit3}']), (800,70))
                
                if dealer_hit_ani4:
                    if card_dealer_x_position4 <= 950:
                        card_dealer_x_position4 += 60
                    else:
                        if dealer_under_17 == 3:
                            dhit4 = asyncio.run(dealer_hits())
                            dealer_hit_card4 = True
                            dealer_under_17 += 1
                        dealer_hit_ani4 = False
                
                if dealer_hit_card4 == False:
                    screen.blit(card_deck,(card_dealer_x_position4, 70))
                if dealer_hit_card4:
                    screen.blit(pygame.image.load(playing_cards[f'{dhit4}']), (950,70))

                if d_score:
                    dealer_score()
                
                if confirm_bet: 
                    if ht_btn.draw(screen):
                        hit_button_pressed = True
                        if pressed == 0:
                            hit_button_pressed_ani = True
                        elif pressed == 1:
                            hit_button_pressed_ani2 = True
                        elif pressed == 2:
                            hit_button_pressed_ani3 = True
                        elif pressed == 3:
                            hit_button_pressed_ani4 = True
                    
                if hit_button_pressed_ani:    
                    if card_deck_x_position <= 190 or card_deck_y_position <= 294:
                        if card_deck_x_position <= 190:
                            card_deck_x_position += 11
                        if card_deck_y_position <= 294:
                            card_deck_y_position += 15
                    else:
                        if pressed == 0:
                            hit1 = player.player_hit()
                            show_image = True
                            pressed += 1
                        hit_button_pressed_ani = False
                
                if hit_button_pressed_ani2:    
                    if card_deck_x_position2 <= 340 or card_deck_y_position2 <= 294:
                        if card_deck_x_position2 <= 340:
                            card_deck_x_position2 += 13
                        if card_deck_y_position2 <= 294:
                            card_deck_y_position2 += 10
                    else:
                        if pressed == 1:
                            hit2 = player.player_hit()
                            show2_image = True
                            pressed += 1
                        hit_button_pressed_ani2 = False
                
                if hit_button_pressed_ani3:    
                    if card_deck_x_position3 <= 790 or card_deck_y_position3 <= 294:
                        if card_deck_x_position3 <= 790:
                            card_deck_x_position3 += 16
                        if card_deck_y_position3 <= 294:
                            card_deck_y_position3 += 5
                    else:
                        if pressed == 2:
                            hit3 = player.player_hit()
                            show3_image = True
                            pressed += 1
                        hit_button_pressed_ani3 = False
                
                if hit_button_pressed_ani4:    
                    if card_deck_x_position4 <= 940 or card_deck_y_position4 <= 294:
                        if card_deck_x_position4 <= 940:
                            card_deck_x_position4 += 20
                        if card_deck_y_position4 <= 294:
                            card_deck_y_position4 += 5
                    else:
                        if pressed == 3:
                            hit4 = player.player_hit()
                            show4_image = True
                            pressed += 1
                        hit_button_pressed_ani4 = False
                
                if show_image == False:
                    screen.blit(card_deck,(card_deck_x_position,card_deck_y_position))
                if show_image:        
                    screen.blit(pygame.image.load(playing_cards[f'{hit1}']), (200,296))
                
                if show2_image == False:
                    screen.blit(card_deck,(card_deck_x_position2,card_deck_y_position2))
                if show2_image:
                    screen.blit(pygame.image.load(playing_cards[f'{hit2}']), (350,296))
                
                if show3_image == False:
                    screen.blit(card_deck,(card_deck_x_position3,card_deck_y_position3))
                if show3_image:
                    screen.blit(pygame.image.load(playing_cards[f'{hit3}']), (800,296))
                
                if show4_image == False:
                    screen.blit(card_deck,(card_deck_x_position4,card_deck_y_position4))
                if show4_image:
                    screen.blit(pygame.image.load(playing_cards[f'{hit4}']), (950,296))

                player_score()
                
                if stand_mes:   
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        finishhim = True
                        button_press_time = pygame.time.get_ticks()      
                current_time = pygame.time.get_ticks()
                if finishhim:    
                    if current_time - button_press_time > 1500:
                        finishhim = False
                        if finishhim == False:
                            player_stands()
                            d_score = True
                            dealer_hide_card = False
                            stand = False  
                
                if finishhim:
                    finish = pygame.image.load("image/finishhim.png").convert()
                    finishc = finish.set_colorkey(BLACK)
                    screen.blit(finish, (600 - (finish.get_width()/2), 200 - (finish.get_height() / 2)))

                if round_draw:
                    if draw_card == 0:
                        draw_cards = True
                    elif draw_card == 1:
                        draw_cards2 = True
                    elif draw_card == 2:
                        draw_cards3 = True
                    elif draw_card == 3:
                        draw_cards4 = True

                        # card_draw_x_position = 40
                        # card_draw_y_position = 70
                    
                if draw_cards:    
                    if card_draw_x_position <= 350 or card_draw_y_position <= 175:
                        if card_draw_x_position <= 350:
                            card_draw_x_position += 11
                        if card_draw_y_position <= 175:
                            card_draw_y_position += 3
                    else:
                        if draw_card == 0:    
                            draw_image = True
                            draw_card += 1
                        draw_cards = False

                if draw_image == False:
                    screen.blit(card_deck,(card_draw_x_position,card_draw_y_position))
                if draw_image:        
                    screen.blit(pygame.image.load("image/draw_d.png"), (350,175))
                
                if draw_cards2:    
                    if card_draw_x_position2 <= 500 or card_draw_y_position2 <= 175:
                        if card_draw_x_position2 <= 500:
                            card_draw_x_position2 += 15
                        if card_draw_y_position2 <= 175:
                            card_draw_y_position2 += 3
                    else:
                        if draw_card == 1:    
                            draw_image2 = True
                            draw_card += 1
                        draw_cards2 = False

                if draw_image2 == False:
                    screen.blit(card_deck,(card_draw_x_position2,card_draw_y_position2))
                if draw_image2:        
                    screen.blit(pygame.image.load("image/draw_r.png"), (500,175))
                
                if draw_cards3:    
                    if card_draw_x_position3 <= 650 or card_draw_y_position3 <= 175:
                        if card_draw_x_position3 <= 650:
                            card_draw_x_position3 += 15
                        if card_draw_y_position3 <= 175:
                            card_draw_y_position3 += 3
                    else:
                        if draw_card == 2:    
                            draw_image3 = True
                            draw_card += 1
                        draw_cards3 = False
                        

                if draw_image3 == False:
                    screen.blit(card_deck,(card_draw_x_position3,card_draw_y_position3))
                if draw_image3:        
                    screen.blit(pygame.image.load("image/draw_a.png"), (650,175))
                
                if draw_cards4:    
                    if card_draw_x_position4 <= 800 or card_draw_y_position4 <= 175:
                        if card_draw_x_position4 <= 800:
                            card_draw_x_position4 += 25
                        if card_draw_y_position4 <= 175:
                            card_draw_y_position4 += 5
                    else:
                        if draw_card == 3:    
                            draw_image4 = True
                            draw_card += 1
                        draw_cards4 = False

                if draw_image4 == False:
                    screen.blit(card_deck,(card_draw_x_position4,card_draw_y_position4))
                if draw_image4:        
                    screen.blit(pygame.image.load("image/draw_w.png"), (800,175))
                    player_draw_bet()
                    round_done = True

                if player_lose:
                    player_loses = pygame.image.load("image/youlose.png").convert()
                    player_losess = pygame.transform.scale(player_loses, (214, 179))
                    player_losesr = pygame.transform.rotate(player_losess, -25)
                    player_losesc = player_losesr.set_colorkey(BLACK)
                    screen.blit(player_losesr, (600 - (player_loses.get_width()/2), 200 - (player_loses.get_height() / 2)))
                    round_done = True
                
                if player_win:
                    player_winner = pygame.image.load("image/winnerlogo.png").convert()
                    player_winsc = player_winner.set_colorkey(BLACK)
                    screen.blit(player_winner, (600 - (player_winner.get_width()/2), 250 - (player_winner.get_height() / 2)))
                    player_wins()
                    round_done = True

                if player.player_hand_count() == 'you lose':
                    player_bust = pygame.image.load("image/bustedlogo.png").convert()
                    player_bust1s = pygame.transform.scale(player_bust, (busted_width, busted_height))
                    player_bust1r = pygame.transform.rotate(player_bust1s, busted_angle)
                    player_bust1c = player_bust1r.set_colorkey(BLACK)
                    screen.blit(player_bust1r, (600 - (player_bust.get_width()/2), 250 - (player_bust.get_height() / 2)))
                    busted_ani = True
                    
                if busted_ani:
                    if busted_angle < 720 or busted_width < 600 or busted_height < 280:
                        if busted_angle < 720:
                            busted_angle += 30
                        if busted_width < 600:
                            busted_width += 20
                        if busted_height < 280:
                            busted_height += 20
                    else:
                        round_done = True
                        busted_ani = False
                
                if round_done:
                    game_round = False
                                                
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('players_chips.txt', 'w') as players_file:
                json.dump(players_chip_count, players_file)
            pygame.quit()   
            exit() 
    
            

    pygame.display.update()
    clock.tick(30)


