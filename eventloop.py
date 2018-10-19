import pygame
import sys


class EventLoop:
    def __init__(self, finished):
        self.finished = finished

    def __str__(self):
        return 'eventLoop, finished=' + str(self.finished) + ')'

    @staticmethod
    def check_events(pacman, play_button):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, pacman)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(play_button, mouse_x, mouse_y)


def check_keydown_events(event, pacman):
    """Respond to keypresses."""
    if event.key == pygame.K_w:
        pacman.moving_up = True
        pacman.moving_left = False
        pacman.moving_down = False
        pacman.moving_right = False
    elif event.key == pygame.K_a:
        pacman.moving_up = False
        pacman.moving_left = True
        pacman.moving_down = False
        pacman.moving_right = False
    elif event.key == pygame.K_s:
        pacman.moving_up = False
        pacman.moving_left = False
        pacman.moving_down = True
        pacman.moving_right = False
    elif event.key == pygame.K_d:
        pacman.moving_up = False
        pacman.moving_left = False
        pacman.moving_down = False
        pacman.moving_right = True
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_play_button(play_button, mouse_x, mouse_y):
    """Start a new game when the player clicks Play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        # Hide cursor
        pygame.mouse.set_visible(False)
