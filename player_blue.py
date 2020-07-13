import pygame, sys

class Player_Blue(pygame.sprite.Sprite):
    
    def __init__(self, game): #jeu pour la fonction de collision
        super().__init__()
        self.game = game
        self.velocity = 1 # Nb de pixels quand le joueur bouge
        self.image = pygame.image.load("images/Moto_Blue_Left.png")
        self.rect = self.image.get_rect() # Rectangle du joueur
        self.rect.x = 900 # Position x de base
        self.rect.y = 473 # Position y de base

    def right(self): #Deplacement à droite
        self.rect.x += self.velocity
        
    def left(self): #Deplacement à gauche
        self.rect.x -= self.velocity

    def up(self): #Deplacement en haut
        self.rect.y -= self.velocity

    def down(self): #Deplacement en bas
        self.rect.y += self.velocity





