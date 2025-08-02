import pygame
import datetime
import random
from sounds import *
from consolelog import *

#Fenster Öffnen
pygame.init()
log("Das Spiel wurde Gestartet")

#Fenster Einstellungen
screen_width = 800
screen_heigth = 500
screen = pygame.display.set_mode((screen_width, screen_heigth))
pygame.display.set_caption('So ein Roter Block')

#Globale Variabeln
points = 0
printed5 = True
printed10 = True
printed20 = True
printedwin = True

#Bilder laden und setzen
icon = pygame.image.load("Textures/Red_Box.png")
pygame.display.set_icon(icon)
player_default = pygame.image.load("Textures/Red_box_default.png").convert()
player_left = pygame.image.load("Textures/Red_box_left.png").convert()
player_right = pygame.image.load("Textures/Red_box_right.png").convert()
player_down = pygame.image.load("Textures/Red_box_down.png").convert()
player_up = pygame.image.load("Textures/Red_box_up.png").convert()

#fonts laden
fonts = pygame.font.get_fonts()

#Texte laden
Punkte_Text = pygame.font.SysFont("impact", 30)
winner_text = pygame.font.SysFont("arial", 40, True)

#Texte rendern
Punkte_Text = Punkte_Text.render(f"Punkte: {points}", True, "white")
Punkte_Text_rect = Punkte_Text.get_rect()
winner_text = winner_text.render("Du hast Gewonnen", True, "white")
winner_text_rect = winner_text.get_rect()

#Postionieren von Texten
Punkte_Text_rect.center = (screen_width//2, 30)
winner_text_rect.center = (screen_width//2, 100)

#Objekte
player = player_default.get_rect()
player.center = (screen_width//2, 250)
food = pygame.Rect((50, 50, 20, 20))

#Timer
clock = pygame.time.Clock()
counter, text = 25, '25'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('arial', 30)

#Game loop
running = True
clock = pygame.time.Clock()
while running:

    #Hintergrund-Farbe
    screen.fill((50, 50, 50))

    #Geschwindigkeit in FPS
    clock.tick(300)

    #Was auf Bildschirm abgebildet wird
    pygame.draw.rect(screen, ("yellow"), food)
    screen.blit(player_default, player)
    screen.blit(Punkte_Text, Punkte_Text_rect)
    screen.blit(font.render(text, True, ("white")), (screen_width-50, 10), )

    #Wenn eine Taste gedrückt wird
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and player.x > 0:
        player.move_ip(-1, 0)
        screen.blit(player_left, player)
    if key[pygame.K_d] and player.x < screen_width - 50:
        player.move_ip(1, 0)
        screen.blit(player_right, player)
    if key[pygame.K_w] and player.y > 0:
        player.move_ip(0, -1)
        screen.blit(player_up, player)
    if key[pygame.K_s] and player.y < screen_heigth - 50:
        player.move_ip(0, 1)
        screen.blit(player_down, player)

    #Wenn "player" mit "food" kollidiert
    if player.colliderect(food):
        food.x = random.randint(0, screen_width - 50)
        food.y = random.randint(0, screen_heigth - 50)
        points += 1
        Punkte_Text = pygame.font.SysFont("impact", 30)
        Punkte_Text = Punkte_Text.render(f"Punkte: {points}", True, "white")
        coinsound()

    #Wenn eine Gewisse Anzahl Punkte erziehlt wird
    if points >= 5:
        if printed5:
            log("Spieler hat 5 Punkte erziehlt")
            printed5 = False
    if points >= 10:
        if printed10:
            log("Spieler hat 10 Punkte erziehlt")
            printed10 = False
    if points >= 20:
        screen.blit(winner_text, winner_text_rect)
        if printed20:
            log("Spieler hat 20 Punkte erziehlt")
            printed20 = False

    #Event-Handler -> Was passiert wenn Bildschirm geschlossen wird
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if key[pygame.K_ESCAPE]:
            running = False
        if event.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3)
            if counter == 0:
                log("Spieler hat verloren")
                points = 0
                log("Das Spiel wurde zurückgesetzt")
                counter = 25
        if points >= 20 and counter > 0 and printedwin == True:
            log("Spieler hat gewonnen")
            printedwin = False

    #Aktualisiert den Frame
    pygame.display.flip()

#Code wird beendet
pygame.quit()
log("<------------------->")
log("|Bro hat Geschlossen|")
log("<------------------->")
