import pygame
import datetime
import random

#Fenster Öffnen
pygame.init()
now = datetime.datetime.now()
print(f"[{now.strftime("%H:%M:%S")} INFO]: Spiel wurde gestartet")

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

#Bilder laden und setzen
icon = pygame.image.load("Textures/Red_Box.png")
pygame.display.set_icon(icon)
Prank = pygame.image.load("Textures/Du_Opfer_Text.png")
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
Punkte_Text = Punkte_Text.render(f"Punkte: {points}", True, "black")
Punkte_Text_rect = Punkte_Text.get_rect()
winner_text = winner_text.render("Du hast gewonnen!", True, "black", "yellow")
winner_text_rect = winner_text.get_rect()

#Postionieren von Texten
Punkte_Text_rect.center = (screen_width//2, 30)
winner_text_rect.center = (screen_width//2, 100)

#Objekte
player = player_default.get_rect()
player.center = (screen_width//2, 250)
food = pygame.Rect((50, 50, 20, 20))

#Game loop
running = True
clock = pygame.time.Clock()
while running:

    #Hintergrund-Farbe
    screen.fill(("silver"))

    #Geschwindigkeit in FPS
    clock.tick(300)

    #Was auf Bildschirm abgebildet wird
    pygame.draw.rect(screen, ("yellow"), food)
    screen.blit(player_default, player)
    screen.blit(Punkte_Text, Punkte_Text_rect)

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
    if key[pygame.K_p]:
        screen.blit(Prank, Prank.get_rect(center = screen.get_rect().center))

    #Wenn "player" mit "food" kollidiert
    if player.colliderect(food):
        food.x = random.randint(0, screen_width - 50)
        food.y = random.randint(0, screen_heigth - 50)
        points += 1
        Punkte_Text = pygame.font.SysFont("impact", 30)
        Punkte_Text = Punkte_Text.render(f"Punkte: {points}", True, "black")

    #Wenn eine Gewisse Anzahl Punkte erziehlt wird
    if points >= 5:
        screen.blit(winner_text, winner_text_rect)
        now = datetime.datetime.now()
        if printed5:
            print(f"[{now.strftime("%H:%M:%S")} INFO]: Spieler hat 5 Punkte erziehlt")
            printed5 = False
    if points >= 10:
        winner_text = pygame.font.SysFont("arial", 40, True)
        winner_text = winner_text.render(f"Bro spielt noch\nweiter als hätte er noch\nnicht gewonnen!", True, "black", "yellow")
        now = datetime.datetime.now()
        if printed10:
            print(f"[{now.strftime("%H:%M:%S")} INFO]: Spieler hat 10 Punkte erziehlt")
            printed10 = False
    if points == 20:
        winner_text = pygame.font.SysFont("arial", 40, True)
        winner_text = winner_text.render(f"Du kannst von vorne anfangen\nwenn du noch\nein Punkt holst!", True, "black", "yellow")
        now = datetime.datetime.now()
        if printed20:
            print(f"[{now.strftime("%H:%M:%S")} INFO]: Spieler hat 20 Punkte erziehlt")
            printed20 = False
    if points == 21:
        points = 0
        now = datetime.datetime.now()
        print(f"[{now.strftime("%H:%M:%S")} INFO]: Spieler hat 21 Punkte erziehlt")
        print(f"[{now.strftime("%H:%M:%S")} INFO]: Das Spiel wurde zurückgesetzt")


    #Event-Handler -> Was passiert wenn Bildschirm geschlossen wird
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Aktualisiert den Frame
    pygame.display.update()

#Wenn Fenster Geschlossen wird
now = datetime.datetime.now()
print(f"[{now.strftime("%H:%M:%S")} INFO]: <------------------->")
print(f"[{now.strftime("%H:%M:%S")} INFO]: |Bro hat Geschlossen|")
print(f"[{now.strftime("%H:%M:%S")} INFO]: <------------------->")

#Code wird beendet
pygame.quit()