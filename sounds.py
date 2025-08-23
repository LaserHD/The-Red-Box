import pygame

pygame.mixer.init()

def coinsound():
    coin_sound = pygame.mixer.music.load('sounds/coinsound.mp3')
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(0, 0,5)

def gamestartsound():
    gamestart = pygame.mixer.music.load('sounds/gamestartsound.mp3')
    pygame.mixer.music.set_volume(0.12)
    pygame.mixer.music.play(0,0,5)