import arcade
from deck import Deck, Compra, Drag, Apos, Bpos
from datetime import timedelta

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Paciencia 2.0 by Marcos Walker"
CARD_WIDTH = 550
CARD_HEIGHT = 841
CARD_SCALE = SCREEN_HEIGHT / CARD_HEIGHT / 4.5
SPACER = (SCREEN_WIDTH - (CARD_WIDTH * CARD_SCALE * 7)) / 8
FULLSCREEN = False

class Paciencia(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, vsync = True, fullscreen = FULLSCREEN)
        arcade.set_background_color(arcade.color.AUBURN)
    
    def setup(self):
        self.deck = Deck(position = [((CARD_WIDTH * CARD_SCALE)/2)+SPACER ,SCREEN_HEIGHT - ((CARD_HEIGHT * CARD_SCALE)/2) - SPACER/2] ,scale = CARD_SCALE)
        self.compra = Compra(position = [(self.deck._width*1.5)+SPACER*2, SCREEN_HEIGHT - ((CARD_HEIGHT * CARD_SCALE)/2) - SPACER/2])
        self.compra.set_cards_info(self.deck._width, self.deck._height, self.deck._x, self.deck._y)
        self.H = Apos('H', [((CARD_WIDTH * CARD_SCALE)*3.5)+SPACER*4, SCREEN_HEIGHT - ((CARD_HEIGHT * CARD_SCALE)/2) - SPACER/2])
        self.S = Apos('S', [((CARD_WIDTH * CARD_SCALE)*4.5)+SPACER*5, SCREEN_HEIGHT - ((CARD_HEIGHT * CARD_SCALE)/2) - SPACER/2])
        self.D = Apos('D', [((CARD_WIDTH * CARD_SCALE)*5.5)+SPACER*6, SCREEN_HEIGHT - ((CARD_HEIGHT * CARD_SCALE)/2) - SPACER/2])
        self.C = Apos('C', [((CARD_WIDTH * CARD_SCALE)*6.5)+SPACER*7, SCREEN_HEIGHT - ((CARD_HEIGHT * CARD_SCALE)/2) - SPACER/2])
        self.pos0 = Bpos(self.deck[-1].hit_box, [((CARD_WIDTH * CARD_SCALE)/2)+SPACER, SCREEN_HEIGHT - ((CARD_HEIGHT * CARD_SCALE)*1.5) - SPACER])
        self.pos1 = Bpos(self.deck[-1].hit_box, [((CARD_WIDTH * CARD_SCALE)*1.5)+SPACER*2, SCREEN_HEIGHT - ((CARD_HEIGHT * CARD_SCALE)*1.5) - SPACER])
        self.pos2 = Bpos(self.deck[-1].hit_box, [((CARD_WIDTH * CARD_SCALE)*2.5)+SPACER*3, SCREEN_HEIGHT - ((CARD_HEIGHT * CARD_SCALE)*1.5) - SPACER])
        self.pos3 = Bpos(self.deck[-1].hit_box, [((CARD_WIDTH * CARD_SCALE)*3.5)+SPACER*4, SCREEN_HEIGHT - ((CARD_HEIGHT * CARD_SCALE)*1.5) - SPACER])
        self.pos4 = Bpos(self.deck[-1].hit_box, [((CARD_WIDTH * CARD_SCALE)*4.5)+SPACER*5, SCREEN_HEIGHT - ((CARD_HEIGHT * CARD_SCALE)*1.5) - SPACER])
        self.pos5 = Bpos(self.deck[-1].hit_box, [((CARD_WIDTH * CARD_SCALE)*5.5)+SPACER*6, SCREEN_HEIGHT - ((CARD_HEIGHT * CARD_SCALE)*1.5) - SPACER])
        self.pos6 = Bpos(self.deck[-1].hit_box, [((CARD_WIDTH * CARD_SCALE)*6.5)+SPACER*7, SCREEN_HEIGHT - ((CARD_HEIGHT * CARD_SCALE)*1.5) - SPACER])
        
        self.drag = Drag()
        
        self.naipes = arcade.SpriteList()
        self.naipes.append(
            arcade.Sprite(scale=0.2, center_x = self.H.pos[0], center_y = self.H.pos[1], texture = arcade.Texture(name="H_back", image = self.H.background))
        )
        self.naipes.append(
            arcade.Sprite(scale=0.2, center_x = self.S.pos[0], center_y = self.S.pos[1], texture = arcade.Texture(name="S_back", image = self.S.background))
        )
        self.naipes.append(
            arcade.Sprite(scale=0.2, center_x = self.D.pos[0], center_y = self.D.pos[1], texture = arcade.Texture(name="D_back", image = self.D.background))
        )
        self.naipes.append(
            arcade.Sprite(scale=0.2, center_x = self.C.pos[0], center_y = self.C.pos[1], texture = arcade.Texture(name="C_back", image = self.C.background))
        )
        
        self.deck_left = self.deck._x - self.deck._width/2
        self.deck_right = self.deck._x + self.deck._width/2
        self.deck_top = self.deck._y + self.deck._height/2
        self.deck_bottom = self.deck._y - self.deck._height/2
        self.compra_left = self.compra.pos[0] - (CARD_WIDTH*CARD_SCALE)/2
        self.compra_right = self.compra_left + (CARD_WIDTH*CARD_SCALE)
        self.H_left = self.H.pos[0] - (CARD_WIDTH*CARD_SCALE)/2
        self.H_right = self.H_left + (CARD_WIDTH*CARD_SCALE)
        self.S_left = self.S.pos[0] - (CARD_WIDTH*CARD_SCALE)/2
        self.S_right = self.S_left + (CARD_WIDTH*CARD_SCALE)
        self.D_left = self.D.pos[0] - (CARD_WIDTH*CARD_SCALE)/2
        self.D_right = self.D_left + (CARD_WIDTH*CARD_SCALE)
        self.C_left = self.C.pos[0] - (CARD_WIDTH*CARD_SCALE)/2
        self.C_right = self.C_left + (CARD_WIDTH*CARD_SCALE)
        self.pos0_top = self.pos0.pos[1] + (CARD_HEIGHT*CARD_SCALE)/2
        self.pos0_bottom = self.pos0.pos[1] - (CARD_HEIGHT*CARD_SCALE)/2
        self.pos0_left = self.pos0.pos[0] - (CARD_WIDTH*CARD_SCALE)/2
        self.pos0_right = self.pos0_left + (CARD_WIDTH*CARD_SCALE)
        self.pos1_left = self.pos1.pos[0] - (CARD_WIDTH*CARD_SCALE)/2
        self.pos1_right = self.pos1_left + (CARD_WIDTH*CARD_SCALE)
        self.pos2_left = self.pos2.pos[0] - (CARD_WIDTH*CARD_SCALE)/2
        self.pos2_right = self.pos2_left + (CARD_WIDTH*CARD_SCALE)
        self.pos3_left = self.pos3.pos[0] - (CARD_WIDTH*CARD_SCALE)/2
        self.pos3_right = self.pos3_left + (CARD_WIDTH*CARD_SCALE)
        self.pos4_left = self.pos4.pos[0] - (CARD_WIDTH*CARD_SCALE)/2
        self.pos4_right = self.pos4_left + (CARD_WIDTH*CARD_SCALE)
        self.pos5_left = self.pos5.pos[0] - (CARD_WIDTH*CARD_SCALE)/2
        self.pos5_right = self.pos5_left + (CARD_WIDTH*CARD_SCALE)
        self.pos6_left = self.pos6.pos[0] - (CARD_WIDTH*CARD_SCALE)/2
        self.pos6_right = self.pos6_left + (CARD_WIDTH*CARD_SCALE)
        
        self.drawCards()
        self.foi = False
        self.tempo = 0
        
    def drawMarcas(self):
        arcade.draw_lrtb_rectangle_outline(self.deck_left, self.deck_right, self.deck_top, self.deck_bottom, arcade.color.WINE, 5) # deck
        arcade.draw_lrtb_rectangle_outline(self.compra_left, self.compra_right, self.deck_top, self.deck_bottom, arcade.color.WINE, 5) # compra
        arcade.draw_lrtb_rectangle_outline(self.H_left, self.H_right, self.deck_top, self.deck_bottom, arcade.color.WINE, 5) # H
        arcade.draw_lrtb_rectangle_outline(self.S_left, self.S_right, self.deck_top, self.deck_bottom, arcade.color.WINE, 5) # S
        arcade.draw_lrtb_rectangle_outline(self.D_left, self.D_right, self.deck_top, self.deck_bottom, arcade.color.WINE, 5) # D
        arcade.draw_lrtb_rectangle_outline(self.C_left, self.C_right, self.deck_top, self.deck_bottom, arcade.color.WINE, 5) # C
        arcade.draw_lrtb_rectangle_outline(self.pos0_left, self.pos0_right, self.pos0_top, self.pos0_bottom, arcade.color.WINE, 5) # pos0
        arcade.draw_lrtb_rectangle_outline(self.pos1_left, self.pos1_right, self.pos0_top, self.pos0_bottom, arcade.color.WINE, 5) # pos1
        arcade.draw_lrtb_rectangle_outline(self.pos2_left, self.pos2_right, self.pos0_top, self.pos0_bottom, arcade.color.WINE, 5) # pos2
        arcade.draw_lrtb_rectangle_outline(self.pos3_left, self.pos3_right, self.pos0_top, self.pos0_bottom, arcade.color.WINE, 5) # pos3
        arcade.draw_lrtb_rectangle_outline(self.pos4_left, self.pos4_right, self.pos0_top, self.pos0_bottom, arcade.color.WINE, 5) # pos4
        arcade.draw_lrtb_rectangle_outline(self.pos5_left, self.pos5_right, self.pos0_top, self.pos0_bottom, arcade.color.WINE, 5) # pos5
        arcade.draw_lrtb_rectangle_outline(self.pos6_left, self.pos6_right, self.pos0_top, self.pos0_bottom, arcade.color.WINE, 5) # pos6
        tempo = str(timedelta(seconds=self.tempo)).split(":")
        texto = "{:02d}:{:02d}:{:02d}".format(int(tempo[0]), int(tempo[1]), int(tempo[2].split('.')[0]))
        arcade.draw_text(text = texto, start_x = self.pos6_left, start_y = 10, color = arcade.color.BLACK, font_name = ('arial'), bold = True)
        arcade.draw_text(text = 'Novo', start_x = self.deck_left, start_y = 10, color = arcade.color.BLACK, font_name = ('arial'), bold = True)
        arcade.draw_lrtb_rectangle_outline(self.deck_left-10, self.deck_left + 50, 25, 5, arcade.color.BLACK, 5)
        
    def drawCards(self):
        self.deck.shuffle()
        self.pos0.extend_pos([self.deck.pop()])
        self.pos0[-1].turn_card()
        lista = []
        for i in range(0,2):
            lista.append(self.deck.pop())
        self.pos1.extend_pos(lista)
        self.pos1[-1].turn_card()
        lista = []
        for i in range(0,3):
            lista.append(self.deck.pop())
        self.pos2.extend_pos(lista)
        self.pos2[-1].turn_card()
        lista = []
        for i in range(0,4):
            lista.append(self.deck.pop())
        self.pos3.extend_pos(lista)
        self.pos3[-1].turn_card()
        lista = []
        for i in range(0,5):
            lista.append(self.deck.pop())
        self.pos4.extend_pos(lista)
        self.pos4[-1].turn_card()
        lista = []
        for i in range(0,6):
            lista.append(self.deck.pop())
        self.pos5.extend_pos(lista)
        self.pos5[-1].turn_card()
        lista = []
        for i in range(0,7):
            lista.append(self.deck.pop())
        self.pos6.extend_pos(lista)
        self.pos6[-1].turn_card()
    
    def on_update(self, deltatime):
        if self.foi:
            self.tempo += deltatime
        if self.H.next_card == 'N' and self.S.next_card == 'N' and self.D.next_card == 'N' and self.C.next_card == 'N' and self.foi:
            self.foi = False
    
    def on_draw(self):
        self.clear()
        self.drawMarcas()
        self.naipes.draw()
        self.deck.draw()
        self.compra.draw()
        self.H.draw()
        self.S.draw()
        self.D.draw()
        self.C.draw()
        self.pos0.draw()
        self.pos1.draw()
        self.pos2.draw()
        self.pos3.draw()
        self.pos4.draw()
        self.pos5.draw()
        self.pos6.draw()
        
        self.drag.draw()
        
    def on_mouse_press(self, x, y, button, modifiers):
        if button == 1:
            if not self.drag.drag:
                if len(self.compra) > 0 and self.compra[-1].collides_with_point((x, y)): # Arrastar de COMPRA
                    self.drag.append_drags([self.compra[-1]], 'compra', [self.compra[-1].center_x - x, self.compra[-1].center_y - y])
                elif len(self.H) > 0 and self.H[-1].collides_with_point((x, y)): # Arrastar de H
                    self.drag.append_drags([self.H[-1]], 'H', [self.H[-1].center_x - x, self.H[-1].center_y - y])
                    self.H.get_next_valor()
                elif len(self.S) > 0 and self.S[-1].collides_with_point((x, y)): # Arrastar de H
                    self.drag.append_drags([self.S[-1]], 'S', [self.S[-1].center_x - x, self.S[-1].center_y - y])
                    self.S.get_next_valor()
                elif len(self.D) > 0 and self.D[-1].collides_with_point((x, y)): # Arrastar de H
                    self.drag.append_drags([self.D[-1]], 'D', [self.D[-1].center_x - x, self.D[-1].center_y - y])
                    self.D.get_next_valor()
                elif len(self.C) > 0 and self.C[-1].collides_with_point((x, y)): # Arrastar de H
                    self.drag.append_drags([self.C[-1]], 'C', [self.C[-1].center_x - x, self.C[-1].center_y - y])
                    self.C.get_next_valor()
                else:
                    found = False
                    if not found:
                        for card in self.pos0:
                            if not card.turned:
                                if card.collides_with_point((x, y)):
                                    card_index = self.pos0.index(card)
                                    self.drag.append_drags(self.pos0[card_index:], 'pos0', [card.center_x - x, card.center_y - y])
                                    self.pos0.get_next_valor()
                                    self.pos0.ajusta_pos()
                                    self.pos0.ajusta_collision()
                                    found = True
                                    break
                    if not found:
                        for card in self.pos1:
                            if not card.turned:
                                if card.collides_with_point((x, y)):
                                    card_index = self.pos1.index(card)
                                    self.drag.append_drags(self.pos1[card_index:], 'pos1', [card.center_x - x, card.center_y - y])
                                    self.pos1.get_next_valor()
                                    self.pos1.ajusta_pos()
                                    self.pos1.ajusta_collision()
                                    found = True
                                    break
                    if not found:
                        for card in self.pos2:
                            if not card.turned:
                                if card.collides_with_point((x, y)):
                                    card_index = self.pos2.index(card)
                                    self.drag.append_drags(self.pos2[card_index:], 'pos2', [card.center_x - x, card.center_y - y])
                                    self.pos2.get_next_valor()
                                    self.pos2.ajusta_pos()
                                    self.pos2.ajusta_collision()
                                    found = True
                                    break
                    if not found:
                        for card in self.pos3:
                            if not card.turned:
                                if card.collides_with_point((x, y)):
                                    card_index = self.pos3.index(card)
                                    self.drag.append_drags(self.pos3[card_index:], 'pos3', [card.center_x - x, card.center_y - y])
                                    self.pos3.get_next_valor()
                                    self.pos3.ajusta_pos()
                                    self.pos3.ajusta_collision()
                                    found = True
                                    break
                    if not found:
                        for card in self.pos4:
                            if not card.turned:
                                if card.collides_with_point((x, y)):
                                    card_index = self.pos4.index(card)
                                    self.drag.append_drags(self.pos4[card_index:], 'pos4', [card.center_x - x, card.center_y - y])
                                    self.pos4.get_next_valor()
                                    self.pos4.ajusta_pos()
                                    self.pos4.ajusta_collision()
                                    found = True
                                    break
                    if not found:
                        for card in self.pos5:
                            if not card.turned:
                                if card.collides_with_point((x, y)):
                                    card_index = self.pos5.index(card)
                                    self.drag.append_drags(self.pos5[card_index:], 'pos5', [card.center_x - x, card.center_y - y])
                                    self.pos5.get_next_valor()
                                    self.pos5.ajusta_pos()
                                    self.pos5.ajusta_collision()
                                    found = True
                                    break
                    if not found:
                        for card in self.pos6:
                            if not card.turned:
                                if card.collides_with_point((x, y)):
                                    card_index = self.pos6.index(card)
                                    self.drag.append_drags(self.pos6[card_index:], 'pos6', [card.center_x - x, card.center_y - y])
                                    self.pos6.get_next_valor()
                                    self.pos6.ajusta_pos()
                                    self.pos6.ajusta_collision()
                                    found = True
                                    break
        elif button == 4:
            if not self.drag.drag:
                teste = self.verificaPosB()
                while teste:
                    teste = self.verificaPosB()
           
    def verificaPosB(self):
        retorno = False
        if len(self.compra) > 0:
            if self.H.check_next(self.compra[-1]) or self.S.check_next(self.compra[-1]) or self.D.check_next(self.compra[-1]) or self.C.check_next(self.compra[-1]):
                self.compra.remove(self.compra[-1])
                retorno = True
        if len(self.pos0) > 0:
            if self.H.check_next(self.pos0[-1]) or self.S.check_next(self.pos0[-1]) or self.D.check_next(self.pos0[-1]) or self.C.check_next(self.pos0[-1]):
                self.pos0.remove_last()
                retorno = True
                self.turnCard()
        if len(self.pos1) > 0:
            if self.H.check_next(self.pos1[-1]) or self.S.check_next(self.pos1[-1]) or self.D.check_next(self.pos1[-1]) or self.C.check_next(self.pos1[-1]):
                self.pos1.remove_last()
                retorno = True
                self.turnCard()
        if len(self.pos2) > 0:
            if self.H.check_next(self.pos2[-1]) or self.S.check_next(self.pos2[-1]) or self.D.check_next(self.pos2[-1]) or self.C.check_next(self.pos2[-1]):
                self.pos2.remove_last()
                retorno = True
                self.turnCard()
        if len(self.pos3) > 0:
            if self.H.check_next(self.pos3[-1]) or self.S.check_next(self.pos3[-1]) or self.D.check_next(self.pos3[-1]) or self.C.check_next(self.pos3[-1]):
                self.pos3.remove_last()
                retorno = True
                self.turnCard()
        if len(self.pos4) > 0:
            if self.H.check_next(self.pos4[-1]) or self.S.check_next(self.pos4[-1]) or self.D.check_next(self.pos4[-1]) or self.C.check_next(self.pos4[-1]):
                self.pos4.remove_last()
                retorno = True
                self.turnCard()
        if len(self.pos5) > 0:
            if self.H.check_next(self.pos5[-1]) or self.S.check_next(self.pos5[-1]) or self.D.check_next(self.pos5[-1]) or self.C.check_next(self.pos5[-1]):
                self.pos5.remove_last()
                retorno = True
                self.turnCard()
        if len(self.pos6) > 0:
            if self.H.check_next(self.pos6[-1]) or self.S.check_next(self.pos6[-1]) or self.D.check_next(self.pos6[-1]) or self.C.check_next(self.pos6[-1]):
                self.pos6.remove_last()
                retorno = True
                self.turnCard()
        return retorno
        
    def on_mouse_motion(self, x, y, dx, dy):
        if self.drag.drag:
            self.drag.update_position(x, y)
            
    def turnCard(self):
        if len(self.pos0) > 0:
            if self.pos0[-1].turned: self.pos0[-1].turn_card()
            
        if len(self.pos1) > 0:
            if self.pos1[-1].turned: self.pos1[-1].turn_card()
            
        if len(self.pos2) > 0:
            if self.pos2[-1].turned: self.pos2[-1].turn_card()
            
        if len(self.pos3) > 0:
            if self.pos3[-1].turned: self.pos3[-1].turn_card()
            
        if len(self.pos4) > 0:
            if self.pos4[-1].turned: self.pos4[-1].turn_card()
            
        if len(self.pos5) > 0:
            if self.pos5[-1].turned: self.pos5[-1].turn_card()
            
        if len(self.pos6) > 0:
            if self.pos6[-1].turned: self.pos6[-1].turn_card()
        
    def on_mouse_release(self, x, y, button, modifiers):
        if not self.foi:
            self.foi = True
        if button == 1: 
            if not self.drag.drag:    
                if (x >= self.deck_left and x <= self.deck_right) and (y >= self.deck_bottom and y <= self.deck_top): # COMPRAR DO DECK
                    if (len(self.deck) > 0):  
                        carta = self.deck[-1]
                        self.compra.compra_carta(carta)
                    else:
                        self.deck.extend_deck(self.compra)
                        self.compra.clear()
                elif (x >= self.deck_left-10 and x<= self.deck_left+50) and (y >= 5 and y <= 25):
                    self.setup()
            else: # Draging
                find = False
                if (self.drag[0].center_x >= self.H_left and self.drag[0].center_x <= self.H_right) and (self.drag[0].center_y >= self.deck_bottom and self.drag[0].center_y <= self.deck_top): # H
                    if len(self.drag) == 1 and self.H.check_next(self.drag[0]):
                        self.drag.clear_drag()
                        self.turnCard()
                        find = True
                elif (self.drag[0].center_x >= self.S_left and self.drag[0].center_x <= self.S_right) and (self.drag[0].center_y >= self.deck_bottom and self.drag[0].center_y <= self.deck_top): # S
                    if len(self.drag) == 1 and self.S.check_next(self.drag[0]):
                        self.drag.clear_drag()
                        self.turnCard()
                        find = True
                elif (self.drag[0].center_x >= self.D_left and self.drag[0].center_x <= self.D_right) and (self.drag[0].center_y >= self.deck_bottom and self.drag[0].center_y <= self.deck_top): # D
                    if len(self.drag) == 1 and self.D.check_next(self.drag[0]):
                        self.drag.clear_drag()
                        self.turnCard()
                        find = True
                elif (self.drag[0].center_x >= self.C_left and self.drag[0].center_x <= self.C_right) and (self.drag[0].center_y >= self.deck_bottom and self.drag[0].center_y <= self.deck_top): # C
                    if len(self.drag) == 1 and self.C.check_next(self.drag[0]):
                        self.drag.clear_drag()
                        self.turnCard()
                        find = True
                elif (self.drag[0].center_x >= self.pos0_left and self.drag[0].center_x <= self.pos0_right) and (self.drag[0].center_y >= self.pos0_bottom and self.drag[0].center_y <= self.pos0_top) or self.drag[0].collides_with_list(self.pos0): # pos0
                    if self.pos0.check_next(self.drag):
                        self.drag.clear_drag()
                        self.turnCard()
                        find = True
                elif (self.drag[0].center_x >= self.pos1_left and self.drag[0].center_x <= self.pos1_right) and (self.drag[0].center_y >= self.pos0_bottom and self.drag[0].center_y <= self.pos0_top) or self.drag[0].collides_with_list(self.pos1): # pos1
                    if self.pos1.check_next(self.drag):
                        self.drag.clear_drag()
                        self.turnCard()
                        find = True
                elif (self.drag[0].center_x >= self.pos2_left and self.drag[0].center_x <= self.pos2_right) and (self.drag[0].center_y >= self.pos0_bottom and self.drag[0].center_y <= self.pos0_top) or self.drag[0].collides_with_list(self.pos2): # pos2
                    if self.pos2.check_next(self.drag):
                        self.drag.clear_drag()
                        self.turnCard()
                        find = True
                elif (self.drag[0].center_x >= self.pos3_left and self.drag[0].center_x <= self.pos3_right) and (self.drag[0].center_y >= self.pos0_bottom and self.drag[0].center_y <= self.pos0_top) or self.drag[0].collides_with_list(self.pos3): # pos3
                    if self.pos3.check_next(self.drag):
                        self.drag.clear_drag()
                        self.turnCard()
                        find = True
                elif (self.drag[0].center_x >= self.pos4_left and self.drag[0].center_x <= self.pos4_right) and (self.drag[0].center_y >= self.pos0_bottom and self.drag[0].center_y <= self.pos0_top) or self.drag[0].collides_with_list(self.pos4): # pos4
                    if self.pos4.check_next(self.drag):
                        self.drag.clear_drag()
                        self.turnCard()
                        find = True
                elif (self.drag[0].center_x >= self.pos5_left and self.drag[0].center_x <= self.pos5_right) and (self.drag[0].center_y >= self.pos0_bottom and self.drag[0].center_y <= self.pos0_top) or self.drag[0].collides_with_list(self.pos5): # pos5
                    if self.pos5.check_next(self.drag):
                        self.drag.clear_drag()
                        self.turnCard()
                        find = True
                elif (self.drag[0].center_x >= self.pos6_left and self.drag[0].center_x <= self.pos6_right) and (self.drag[0].center_y >= self.pos0_bottom and self.drag[0].center_y <= self.pos0_top) or self.drag[0].collides_with_list(self.pos6): # pos6
                    if self.pos6.check_next(self.drag):
                        self.drag.clear_drag()
                        self.turnCard()
                        find = True
                if not find:
                    if self.drag.drag_from == 'compra':
                        self.compra.append_card(self.drag[-1], False)
                        self.drag.clear_drag()
                    elif self.drag.drag_from == 'H':
                        self.H.append_card(self.drag[-1], False)
                        self.H.get_next_valor()
                        self.drag.clear_drag()
                    elif self.drag.drag_from == 'S':
                        self.S.append_card(self.drag[-1], False)
                        self.S.get_next_valor()
                        self.drag.clear_drag()
                    elif self.drag.drag_from == 'D':
                        self.D.append_card(self.drag[-1], False)
                        self.D.get_next_valor()
                        self.drag.clear_drag()
                    elif self.drag.drag_from == 'C':
                        self.C.append_card(self.drag[-1], False)
                        self.C.get_next_valor()
                        self.drag.clear_drag()
                    elif self.drag.drag_from == 'pos0':
                        self.pos0.extend_pos(self.drag)
                        self.drag.clear_drag()
                    elif self.drag.drag_from == 'pos1':
                        self.pos1.extend_pos(self.drag)
                        self.drag.clear_drag()
                    elif self.drag.drag_from == 'pos2':
                        self.pos2.extend_pos(self.drag)
                        self.drag.clear_drag()
                    elif self.drag.drag_from == 'pos3':
                        self.pos3.extend_pos(self.drag)
                        self.drag.clear_drag()
                    elif self.drag.drag_from == 'pos4':
                        self.pos4.extend_pos(self.drag)
                        self.drag.clear_drag()
                    elif self.drag.drag_from == 'pos5':
                        self.pos5.extend_pos(self.drag)
                        self.drag.clear_drag()
                    elif self.drag.drag_from == 'pos6':
                        self.pos6.extend_pos(self.drag)
                        self.drag.clear_drag()
                
def main():
    window = Paciencia()
    window.setup()
    arcade.run()
    
if __name__ == "__main__":
    main()