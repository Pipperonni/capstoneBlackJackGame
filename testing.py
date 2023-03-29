
if stand:
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
                            
                        if hit_button_pressed_ani == False:    
                            if pressed == 0:
                                hit1 = player.player_hit()
                                show_image = True
                                pressed += 1
                        if hit_button_pressed_ani2 == False:
                            if pressed == 1:
                                hit2 = player.player_hit()
                                show2_image = True
                                pressed += 1
                        if hit_button_pressed_ani3 == False:
                            if pressed == 2:
                                hit3 = player.player_hit()
                                show3_image = True
                                pressed += 1
                        if hit_button_pressed_ani4 == False:
                            if pressed == 3:
                                hit4 = player.player_hit()
                                show4_image = True
                                pressed += 1
                        
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


