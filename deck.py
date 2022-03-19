import os
from PIL import Image
from arcade import SpriteList, Sprite, Texture

VALORES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
NAIPES = ['H', 'S', 'D', 'C']

class Deck_base(SpriteList):
    def __init__(self, position = None):
        super().__init__()
        self.pos = position
        self._width = None
        self._height = None
        self._x = None
        self._y = None
    
    def append_card(self, card, remove):
        card.set_position(self.pos[0], self.pos[1])
        if remove: card.remove_from_sprite_lists()
        self.append(card)
        
    def get_cards_info(self):
        if (len(self) > 0):
            self._width = self[0].width
            self._height = self[0].height
            self._x = self[0].center_x
            self._y = self[0].center_y
            
    def set_cards_info(self, width, height, x, y):
        self._width = width
        self._height = height
        self._x = x
        self._y = y
        
class Card(Sprite):
    def __init__(self, back_img, valor, naipe, scale, center_x, center_y):
        super().__init__(scale = scale, center_x = center_x, center_y = center_y)
        self.valor = valor
        self.naipe = naipe
        self.back_img = back_img
        self.turned = True
        self.getImg()
        
    def getImg(self):
        card_name = "{}{}.png".format(self.valor, self.naipe)
        card_image = Image.open(os.path.join(os.getcwd(), "resources", "images", "cards", card_name ))
        back_texture = Texture(name="card_back", image = self.back_img)
        front_texture = Texture(name=card_name, image = card_image )
        self.textures = [front_texture, back_texture]
        self.set_texture(1)
        
    def turn_card(self):
        if (self.turned):
            self.turned = False
            self.set_texture(0)
        else:
            self.turned = True
            self.set_texture(1)

class Bpos(Deck_base):
    def __init__(self, hit_box, position = None):
        super().__init__(position)
        self.naipes = NAIPES
        self.next_card = 'K'
        self.red = ['H', 'D']
        self.black = ['S', 'C']
        self.original_hitBox = hit_box
        
    def get_next_valor(self):
        valores_rev = VALORES[::-1]
        if (len(self) > 0):
            self.next_card = valores_rev[valores_rev.index(self[-1].valor)+1] if valores_rev.index(self[-1].valor)+1 < len(valores_rev) else 'N'
            if self[-1].naipe in self.red:
                self.naipes = self.black
            else:
                self.naipes = self.red
        else:
            self.next_card = 'K'
            self.naipes = NAIPES
    
    def ajusta_pos(self):
        if len(self) > 0:
            self.get_cards_info()
            soma_x = 0
            for card in self:
                if not card.turned:
                    if (self.index(card) > 0) and self[self.index(card)-1].turned:
                        soma_x += self._height/8
                    elif (self.index(card) > 0):
                        soma_x += self._height/5
                    card.set_position(
                        self.pos[0],
                        self.pos[1] - (soma_x) 
                    )
                else:
                    if (self.index(card) > 0):
                        soma_x += self._height/8
                    card.set_position (
                        self.pos[0],
                        self.pos[1] - (soma_x)
                    )
    
    def ajusta_collision(self):
        if len(self) > 0:
            for card in self:
                if card != self[-1] and not card.turned:
                    points = list(card.get_hit_box())
                    points[0] = (points[0][0], (self._height)*1.7)
                    points[1] = (points[1][0], (self._height)*1.7)
                    points[2] = (points[2][0], (self._height)*1.7)
                    points[3] = (points[3][0], (self._height)*1.7)
                    self[self.index(card)].set_hit_box(points)
                elif card == self[-1] and not card.turned:
                    self[-1].set_hit_box(self.original_hitBox)
    
    def check_next(self, cards):
        returno = False
        if cards[0].valor == self.next_card and cards[0].naipe in self.naipes:
            for card in cards:
                self.append_card(card, False)
            self.get_next_valor()
            self.ajusta_pos()
            self.ajusta_collision()
            returno = True
        return returno
        
    def extend_pos(self, cards):
        for card in cards:
                self.append_card(card, False)
        self.get_next_valor()
        self.ajusta_pos()
        self.ajusta_collision()
        
    def remove_last(self):
        self.remove(self[-1])
        self.get_next_valor()
        self.ajusta_pos()
        self.ajusta_collision()

class Apos(Deck_base):
    def __init__(self, naipe, position = None):  
        super().__init__(position)
        self.naipe = naipe
        self.next_card = 'A'
        self.background = Image.open(os.path.join(os.getcwd(), "resources", "images", "cards", "{}.png".format(self.naipe) ))
    
    def get_next_valor(self):
        if (len(self) > 0):
            self.next_card = VALORES[VALORES.index(self[-1].valor)+1] if len(self) < len(VALORES) else 'N'
        else:
            self.next_card = 'A'
            
    def check_next(self, card):
        returno = False
        if card.valor == self.next_card and card.naipe == self.naipe:
            self.append_card(card, False)
            self.get_next_valor()
            returno = True
        return returno
    
class Drag(Deck_base):
    def __init__(self):
        super().__init__()
        self.drag_from = ''
        self.drag = False
    
    def clear_drag(self):
        self.clear()
        self.pos = []
        self.drag_from = ''
        self.drag = False
    
    def append_drags(self, cards, drag_from, pos):
        self.pos = pos
        self.drag_from = drag_from
        for card in cards:
            card.remove_from_sprite_lists()
            self.append(card)
        self.drag = True
        self.get_cards_info()
        
    def update_position(self, x , y):
        for card in self:
            card.set_position(
                self.pos[0] + x,
                self.pos[1] + y - ( self._height/5 * self.index(card))
            )
            
class Compra(Deck_base):
    def __init__(self, position = None):
        super().__init__(position)
    
    def compra_carta(self, carta):
        carta.turn_card()
        self.append_card(carta, True)

class Deck(Deck_base):
    def __init__(self, position = None, scale = None):
        super().__init__(position = None)
        self.pos = (72.5, 504.5) if position == None else position
        self.scale = 0.2 if scale == None else scale
        self.get_cards()
        
    def get_cards(self):
        card_back = Image.open(os.path.join(os.getcwd(), "resources","images","cards","red_back.png"))
        for naipe in NAIPES:
            for valor in VALORES:
                self.append(Card( card_back, valor, naipe, self.scale, self.pos[0], self.pos[1]))
        self.get_cards_info()
        
    def extend_deck(self, sprite_list):
        self.extend(sprite_list)
        for card in self:
            card.set_position(self.pos[0], self.pos[1])
            card.turn_card()
        self.reverse()
