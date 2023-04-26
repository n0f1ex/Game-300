import pygame
import os


class Masti(pygame.sprite.Sprite):
    def __init__(self, w, h, m):
        # 480x360
        # 71x49
        self.resize = 2
        pygame.sprite.Sprite.__init__(self)
        c = {'P': [-50 * self.resize, -50 * self.resize], 'C': [0, -50 * self.resize],
             'B': [-50 * self.resize, 0], 'K': [0, 0]}
        c = c[m]
        self.resize = 2
        self.rect = pygame.Rect(w//2 + c[0], h//2 + c[1], 50 * self.resize, 50 * self.resize)
        self.image = pygame.transform.scale(pygame.image.load(os.path.abspath('sprites/' + m + '.png')),
                                            (50 * self.resize, 50 * self.resize))

    def destroy(self):
        self.kill()
