import pygame, os
from karts import LustCard


def display():
    screen.fill((0, 255, 0))

    clock.tick(FPS)

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()

W, H = 720, 480
FPS = 20  # частота кадров в секунду

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((W, H))

pygame.display.set_caption("Game 300")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
card = LustCard(W, H)
card.init('cover', 50, 100)
x0, y0 = card.rect.x, card.rect.y
x, y = 500, 300
all_sprites.add(card)

v = 50
a = -1
v_all = (v*2 + (v-1)*a)/2 * v
len_x, len_y = (x - x0) / v_all, (y - y0) / v_all
for t in range(v):
    card.rect.x += len_x * (v - t)
    card.rect.y += len_y * (v - t)
    display()
while True:
    eve = pygame.event.get()
    for events in eve:
        if events.type == pygame.QUIT:
            exit()
