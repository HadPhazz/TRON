import pygame, sys, math
from player_orange import Player_Orange
from player_blue import Player_Blue

white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 102, 0)
blue = (0, 0, 255)

class Game:

    def __init__(self):
        
        self.status = False
        self.all_players = pygame.sprite.Group()
        self.player_orange = Player_Orange(self)
        self.player_blue = Player_Blue(self)
        self.all_players.add(self.player_orange)
        self.all_players.add(self.player_blue)
        self.pressed = {}

################################################## # Actions réalisés pour déplacer le joueur Orange

    def update_orange(self, window, background):
        
        window.blit(self.player_orange.image, self.player_orange.rect) # On affiche le joueur orange sur l'écran en enlevant les trainées derrière lui

        if self.pressed.get(pygame.K_RIGHT) and self.player_orange.rect.x + self.player_orange.rect.width < window.get_width():
            self.player_orange.image = pygame.image.load("images/Moto_Orange_Right.png")
            self.player_orange.right() #Méthode de mouvement à droite
            pygame.draw.aaline(background, orange, (self.player_orange.rect.centerx, self.player_orange.rect.centery),(self.player_orange.rect.centerx, self.player_orange.rect.centery), 5)
            
        elif self.pressed.get(pygame.K_LEFT) and self.player_orange.rect.x > 0:
            self.player_orange.image = pygame.image.load("images/Moto_Orange_Left.png")
            self.player_orange.left() #Méthode de mouvement à gauche
            pygame.draw.aaline(background, orange, (self.player_orange.rect.centerx, self.player_orange.rect.centery),(self.player_orange.rect.centerx, self.player_orange.rect.centery), 5)
                
        elif self.pressed.get(pygame.K_UP)and self.player_orange.rect.y > 0:
            self.player_orange.image = pygame.image.load("images/Moto_Orange_Up.png")
            self.player_orange.up() #Méthode de mouvement en haut
            pygame.draw.aaline(background, orange, (self.player_orange.rect.centerx, self.player_orange.rect.centery),(self.player_orange.rect.centerx, self.player_orange.rect.centery), 5)

        elif self.pressed.get(pygame.K_DOWN) and self.player_orange.rect.y + self.player_orange.rect.height < window.get_height():
            self.player_orange.image = pygame.image.load("images/Moto_Orange_Down.png")
            self.player_orange.down() #Méthode de mouvement en bas
            pygame.draw.aaline(background, orange, (self.player_orange.rect.centerx, self.player_orange.rect.centery),(self.player_orange.rect.centerx, self.player_orange.rect.centery), 5)

################################################## # Actions réalisés pour déplacer le joueur Bleu

    def update_blue(self, window, background):

        window.blit(self.player_blue.image, self.player_blue.rect) # On affiche le joueur bleu sur l'écran en enlevant les trainées derrière lui

        if self.pressed.get(pygame.K_KP4) and self.player_blue.rect.x > 0:
            self.player_blue.image = pygame.image.load("images/Moto_Blue_Left.png")
            self.player_blue.left() #Méthode de mouvement à gauche
            pygame.draw.aaline(background, blue, (self.player_blue.rect.centerx, self.player_blue.rect.centery),(self.player_blue.rect.centerx, self.player_blue.rect.centery), 5)

        elif self.pressed.get(pygame.K_KP6) and self.player_blue.rect.x + self.player_blue.rect.width < window.get_width():
            self.player_blue.image = pygame.image.load("images/Moto_Blue_Right.png")
            self.player_blue.right() #Méthode de mouvement à droite
            pygame.draw.aaline(background, blue, (self.player_blue.rect.centerx, self.player_blue.rect.centery),(self.player_blue.rect.centerx, self.player_blue.rect.centery), 5)
            
        elif self.pressed.get(pygame.K_KP8) and self.player_blue.rect.y > 0:
            self.player_blue.image = pygame.image.load("images/Moto_Blue_Up.png")
            self.player_blue.up() #Méthode de mouvement en haut
            pygame.draw.aaline(background, blue, (self.player_blue.rect.centerx, self.player_blue.rect.centery),(self.player_blue.rect.centerx, self.player_blue.rect.centery), 5)
            
        elif self.pressed.get(pygame.K_KP5) and self.player_blue.rect.y + self.player_blue.rect.height < window.get_height():
            self.player_blue.image = pygame.image.load("images/Moto_Blue_Down.png")
            self.player_blue.down() #Méthode de mouvement en bas
            pygame.draw.aaline(background, blue, (self.player_blue.rect.centerx, self.player_blue.rect.centery),(self.player_blue.rect.centerx, self.player_blue.rect.centery), 5)
            
##################################################

    def collision_orange(self, window):
        
        self.Pixel_Color_Orange_Right = window.get_at((self.player_orange.rect.centerx+27, self.player_orange.rect.centery))
        self.Pixel_Color_Orange_Left = window.get_at((self.player_orange.rect.centerx-27, self.player_orange.rect.centery))
        self.Pixel_Color_Orange_Up = window.get_at((self.player_orange.rect.centerx, self.player_orange.rect.centery-27))
        self.Pixel_Color_Orange_Down = window.get_at((self.player_orange.rect.centerx, self.player_orange.rect.centery+27))

        if self.pressed.get(pygame.K_RIGHT) and self.player_orange.rect.x + self.player_orange.rect.width < window.get_width() and self.Pixel_Color_Orange_Right == (255, 102, 0, 255) or self.pressed.get(pygame.K_RIGHT) and self.player_orange.rect.x + self.player_orange.rect.width < window.get_width() and self.Pixel_Color_Orange_Right == (0, 0, 255, 255):
            self.win_state_orange(window)

        elif self.pressed.get(pygame.K_LEFT) and self.player_orange.rect.x > 0 and self.Pixel_Color_Orange_Left == (255, 102, 0, 255) or self.pressed.get(pygame.K_LEFT) and self.player_orange.rect.x > 0 and self.Pixel_Color_Orange_Left == (0, 0, 255, 255):
            self.win_state_orange(window)

        elif self.pressed.get(pygame.K_UP)and self.player_orange.rect.y > 0 and self.Pixel_Color_Orange_Up == (255, 102, 0, 255) or self.pressed.get(pygame.K_UP)and self.player_orange.rect.y > 0 and self.Pixel_Color_Orange_Up == (0, 0, 255, 255):
            self.win_state_orange(window)

        elif self.pressed.get(pygame.K_DOWN) and self.player_orange.rect.y + self.player_orange.rect.height < window.get_height() and self.Pixel_Color_Orange_Down == (255, 102, 0, 255) or self.pressed.get(pygame.K_DOWN) and self.player_orange.rect.y + self.player_orange.rect.height < window.get_height() and self.Pixel_Color_Orange_Down == (0, 0, 255, 255):
            self.win_state_orange(window)
            
##################################################

    def collision_blue(self, window):

        self.Pixel_Color_Blue_Left = window.get_at((self.player_blue.rect.centerx-27, self.player_blue.rect.centery))
        self.Pixel_Color_Blue_Right = window.get_at((self.player_blue.rect.centerx+27, self.player_blue.rect.centery))
        self.Pixel_Color_Blue_Up = window.get_at((self.player_blue.rect.centerx, self.player_blue.rect.centery-27))
        self.Pixel_Color_Blue_Down = window.get_at((self.player_blue.rect.centerx, self.player_blue.rect.centery+27))

        if self.pressed.get(pygame.K_KP4) and self.player_blue.rect.x > 0 and self.Pixel_Color_Blue_Left == (255, 102, 0, 255) or self.pressed.get(pygame.K_KP4) and self.player_blue.rect.x > 0 and self.Pixel_Color_Blue_Left == (0, 0, 255, 255):
            self.win_state_blue(window)

        elif self.pressed.get(pygame.K_KP6) and self.player_blue.rect.x + self.player_blue.rect.width < window.get_width() and self.Pixel_Color_Blue_Right == (255, 102, 0, 255) or self.pressed.get(pygame.K_KP6) and self.player_blue.rect.x + self.player_blue.rect.width < window.get_width() and self.Pixel_Color_Blue_Right == (0, 0, 255, 255):
            self.win_state_blue(window)

        elif self.pressed.get(pygame.K_KP8) and self.player_blue.rect.y > 0 and self.Pixel_Color_Blue_Up == (255, 102, 0, 255) or self.pressed.get(pygame.K_KP8) and self.player_blue.rect.y > 0 and self.Pixel_Color_Blue_Up == (0, 0, 255, 255):
            self.win_state_blue(window)

        elif self.pressed.get(pygame.K_KP5) and self.player_blue.rect.y + self.player_blue.rect.height < window.get_height() and self.Pixel_Color_Blue_Down == (255, 102, 0, 255) or self.pressed.get(pygame.K_KP5) and self.player_blue.rect.y + self.player_blue.rect.height < window.get_height() and self.Pixel_Color_Blue_Down == (0, 0, 255, 255):
            self.win_state_blue(window)
            
##################################################

    def win_state_orange(self, window):

        Player_Blue_Win = pygame.image.load("images/Player_Blue_Win.png")
        self.player_orange.velocity = 0 #Joueur orange ne bouge plus
        self.player_blue.velocity = 0 #Joueur bleu ne bouge plus
        window.blit(Player_Blue_Win, (240, 300)) # On affiche qui à gagné à l'écran

##################################################

    def win_state_blue(self, window):
        
        Player_Orange_Win = pygame.image.load("images/Player_Orange_Win.png")
        self.player_orange.velocity = 0 #Joueur orange ne bouge plus
        self.player_blue.velocity = 0 #Joueur bleu ne bouge plus
        window.blit(Player_Orange_Win, (265, 300)) # On affiche qui à gagné à l'écran

##################################################
