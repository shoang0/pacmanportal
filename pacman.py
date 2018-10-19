import pygame
from pygame.sprite import Sprite


class Pacman(Sprite):
    def __init__(self, screen):
        """Initialize pacman and his starting position"""
        super(Pacman, self).__init__()
        self.screen = screen

        # load image and get its rect
        self.image = pygame.image.load('images/pacman.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx - 255
        self.rect.bottom = self.screen_rect.bottom - 200

        # store decimal value for pacman's center
        self.center = float(self.rect.centerx)

        # movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update pacman's position based on movement flags"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
        if self.moving_up:
            self.rect.bottom -= 1
        if self.moving_down:
            self.rect.bottom += 1

    def blitme(self):
        # draw pacman at current location
        self.screen.blit(self.image, self.rect)
