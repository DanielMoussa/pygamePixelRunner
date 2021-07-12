# import necessary modules
import pygame
from sys import exit

# launches pygame
pygame.init()

# display an 800 pixel by 400 pixel screen
screen = pygame.display.set_mode((800, 400))

# change display name
pygame.display.set_caption('Pixel Runner')

# set time to specify fps later
clock = pygame.time.Clock()

# speicify the font (font file, font size)
test_font = pygame.font.Font('font/Pixeltype.ttf', 60)

# Load Textures
# load sky texture
sky_surface = pygame.image.load('graphics/Sky.png')
# load ground texture
ground_surface = pygame.image.load('graphics/ground.png')
# create a text surface, text(text, anti aliasing, color)
text_surface = test_font.render('Pixel Runner', False, 'Green')

# load snail texture & display it near the end of the screen (600 pixels)
snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_x_pos = 600

# True is never false, which is an infinite loop, to keep updating the displayed informations
while True:

    # loop to check for input to close the display window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # display textures & positions

    # display the sky texture
    screen.blit(sky_surface, (0, 0))

    # display the ground texture
    screen.blit(ground_surface, (0, 300))

    # display the created text surface
    screen.blit(text_surface, (300, 50))

    # move the snail 4 pixels every tick
    snail_x_pos -= 4
    # teleport the snail to the end of the screen
    if snail_x_pos < -100:
        snail_x_pos = 800
    # display the snail texture
    screen.blit(snail_surface, (snail_x_pos, 275))

    # keep updating the display info 60 times a second
    pygame.display.update()
    clock.tick(60)
