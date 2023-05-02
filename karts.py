import pygame
import os


class Card(pygame.sprite.Sprite):
    def __init__(self):
        # 480x360
        # 71x49
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = None
        self.h = None
        self.card = ''
        self.resize = 2
        self.margin = 0
        self.hover = False

    def init(self, card, pos, h):
        # значение карты позиция карты высота экрана
        self.h = h
        self.rect = pygame.Rect(pos*49*self.resize, h - 71*self.resize - self.margin, 49*self.resize, 71*self.resize)
        self.image = pygame.transform.scale(pygame.image.load(os.path.abspath('sprites/' + card + '.png')), (49*self.resize, 71*self.resize))
        self.card = card

    def reposition(self, pos):
        self.rect = pygame.Rect(pos*49*self.resize, self.h - 71*self.resize - self.margin, 49*self.resize, 71*self.resize)
        self.image = pygame.transform.scale(pygame.image.load('sprites/' + self.card + '.png'), (49*self.resize, 71*self.resize))

    def on_hover(self, last, mouse, start=False):
        if (start or (self.rect.collidepoint(mouse) and (list(last)[0] == list(self.card)[0] or list(last)[1] == list(self.card)[1] or list(self.card)[1] == 'Q'))) and not self.hover:
            self.rect[1] -= 10*self.resize
            self.hover = True

    def not_hover(self, mouse):
        if not self.rect.collidepoint(mouse) and self.hover:
            self.rect[1] += 10 * self.resize
            self.hover = False

    def on_click(self, last, mouse, start=False):
        if start or (self.rect.collidepoint(mouse) and (list(last)[0] == list(self.card)[0] or list(last)[1] == list(self.card)[1] or list(self.card)[1] == 'Q')):
            return self.card
        return -1

    def played(self):
        self.kill()


class LustCard(pygame.sprite.Sprite):
    def __init__(self, w, h):
        # 480x360
        # 71x49
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = None
        self.w = w
        self.h = h
        self.card = ''
        self.resize = 2
        self.margin = 0
        self.hover = False

    def init(self, card, x=-1, y=-1):
        if x == -1 and y == -1:
            x = self.w // 2 - 49 * self.resize // 2
            y = self.h // 2 - 71 * self.resize // 2
        # значение карты позиция карты высота экрана
        self.rect = pygame.Rect(x, y, 49*self.resize, 71*self.resize)
        self.image = pygame.transform.scale(pygame.image.load(os.path.abspath('sprites/' + card + '.png')), (49*self.resize, 71*self.resize))
        self.card = card


class Cover(Card):
    def init(self, w, h):
        # значение карты позиция карты высота экрана
        self.card = os.path.abspath('sprites/cover.png')
        self.rect = pygame.Rect(w//36*21, h // 2 - 71*self.resize//2, 49*self.resize, 71*self.resize)
        self.image = pygame.transform.scale(pygame.image.load(self.card), (49*self.resize, 71*self.resize))


class CoverCard(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # 480x360
        # 71x49
        pygame.sprite.Sprite.__init__(self)
        self.resize = 2
        self.card = os.path.abspath('sprites/cover.png')
        self.rect = pygame.Rect(x, y, 49 * self.resize, 71 * self.resize)
        self.image = pygame.transform.scale(pygame.image.load(self.card), (49 * self.resize, 71 * self.resize))
