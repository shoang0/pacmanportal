import pygame
from pygame.sprite import Sprite


class Ghosts(Sprite):
    def __init__(self, screen):
        super(Ghosts, self).__init__()
        self.screen = screen

        # Load the ghost and set its rect attr
        self.image = pygame.image.load('images/blinky1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Spawn ghosts in cage
        self.rect.centerx = self.screen_rect.centerx - 255
        self.rect.bottom = self.screen_rect.bottom - 400

    def blitme(self):
        self.screen.blit(self.image, self.rect)
