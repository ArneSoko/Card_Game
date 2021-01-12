import pygame

# initialize pygame
pygame.init()

# Create 800x600p window
screen = pygame.display.set_mode((1280, 720))

# Title and icon
pygame.display.set_caption("E-Card")
icon = pygame.image.load('graphics/icon.png')
pygame.display.set_icon(icon)

# All sprite use the same Y axis value
Y = 248

# Emperor card sprite
eCard = pygame.image.load('graphics/emperor.png')
eX = 556

# Citizen card sprite
cCard = pygame.image.load('graphics/citizen.png')
cX = 278

# Slave card sprite
sCard = pygame.image.load('graphics/slave.png')
sX = 834

# Text
font = pygame.font.Font('freesansbold.ttf', 32)
playText = "Please select a card by hovering over it with your mouse."


def card_text(x, y, r, g, b):
    text = font.render(playText, True, (r, g, b))
    screen.blit(text, (x, y))


# Method to render the cards
def card(play, x, y):
    screen.blit(play, (x, y))


running = True
while running:
    # Fill screen with colour
    # screen.fill((0, 100, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.K_q:
                running = False
        if 472 > pygame.mouse.get_pos()[1] > 248:
            if 446 > pygame.mouse.get_pos()[0] > cX:
                screen.fill((0, 0, 255))
                playText = "Citizen"
                card_text(300, 200, 255, 0, 0)
            elif 724 > pygame.mouse.get_pos()[0] > eX:
                screen.fill((255, 255, 0))
                playText = "Emperor"
                card_text(575, 200, 0, 0, 255)
            elif 1002 > pygame.mouse.get_pos()[0] > sX:
                screen.fill((255, 0, 0))
                playText = "Slave"
                card_text(870, 200, 255, 255, 0)
            else:
                screen.fill((0, 100, 255))
                playText = \
                    "Please select a card by hovering over it with your mouse."
                card_text(200, 100, 255, 255, 255)

        else:
            screen.fill((0, 100, 255))
            playText = \
                "Please select a card by hovering over it with your mouse."
            card_text(200, 100, 255, 255, 255)

    # Load in the sprites
    card(eCard, eX, Y)
    card(cCard, cX, Y)
    card(sCard, sX, Y)

    # Update the game screen
    pygame.display.update()
