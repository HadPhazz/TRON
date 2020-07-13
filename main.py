import pygame, sys, webbrowser
from game import Game

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 102, 0)
blue = (0, 0, 255)

##################################################

window = pygame.display.set_mode((1000, 1000)) # Fenêtre et sa taille
pygame.display.set_caption("TRON Game") # Titre de la fenêtre

background = pygame.image.load("images/grid_1.png").convert() # Fond d'écran de la fenêtre
background_menu = pygame.image.load("images/background.jpg").convert()

icon = pygame.image.load("images/Icon.png") #Icon fenêtre
pygame.display.set_icon(icon)

music_1 = pygame.mixer.Sound("sounds/derezzed.ogg") #Son joué lors du clique sur le bouton Play
music_2 = pygame.mixer.Sound("sounds/rinzler.ogg")

game = Game() #Charger le jeu

banner = pygame.image.load("images/Logo_Title_1.png") # Titre du jeu

rules = pygame.image.load("images/Rules.png") # Règles du jeu

play_button = pygame.image.load("images/Play.png") # Bouton play
play_Area = pygame.Rect((415, 350), (170, 50))

quit_button = pygame.image.load("images/Quit.png") # Bouton quit
quit_Area = pygame.Rect((740, 850), (163, 50))

credits_button = pygame.image.load("images/Credits.png") # Bouton credits
credits_Area = pygame.Rect((100, 850), (295, 50))

################################################## #Boucle pour faire marcher la fenêtre

running = True

while running:

    window.blit(background, (0,0)) # On positionne le background et on le blit tant que le jeu est actif
    
    if game.status == True:
        pygame.mouse.set_visible(False) # Cacher le curseur de la souris pendant le jeu
        game.update_orange(window, background)
        game.update_blue(window, background)
        game.collision_orange(window)
        game.collision_blue(window)
        
    else:
        window.blit(background_menu, (0,0))
        window.blit(banner, (250, 100))
        window.blit(rules, (205, 550))
        window.blit(play_button, (415, 350))
        window.blit(quit_button, (740, 850))
        window.blit(credits_button, (100, 850))
        music_2.play()

    pygame.display.flip() # Actualisation de l'écran

    for event in pygame.event.get(): # Boucle For

        if event.type == pygame.QUIT: # Croix de la fenêtre
            running = False
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN: # On enclenche une touche du clavier

            game.pressed[event.key] = True #Détéction de la pression de la touche, on appuie dessus
            
            if event.key==pygame.K_ESCAPE: # Touche Echap
                running = False
                pygame.quit()
                sys.exit()

        elif event.type == pygame.KEYUP: # On lache une touche du clavier (Keys ou Num KeyPad)

            game.pressed[event.key] = False #On relache la touche, le joueur ne bouge plus
            
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            if play_Area.collidepoint(event.pos):
                game.status = True #Le jeu tourne je reviens au if avant la boucle while
                music_2.stop() #Musique du menu
                music_1.play() #Lance la musique du jeu
             
            elif quit_Area.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

            elif credits_Area.collidepoint(event.pos):
                webbrowser.open("https://forge.info.unicaen.fr/projects/conception-logicielle-bj-ph-fc-sc/repository")

    pygame.display.flip()         
pygame.quit()

##################################################
