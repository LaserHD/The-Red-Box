import pygame

pygame.mixer.init()
coin_sound = pygame.mixer.music.load('sounds/coinsound.mp3')

def coinsound():
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(0, 0,5)