import pygame, os

card = os.path.abspath('sprites/cover.png')
rect = pygame.Rect(0, 0, 49, 71)
image = pygame.transform.scale(pygame.image.load(card), (49, 71))
