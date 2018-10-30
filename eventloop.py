import pygame
import sys


class EventLoop:
    def __init__(self, finished):
        self.finished = finished

    def __str__(self):
        return 'eventLoop, finished=' + str(self.finished) + ')'

    @staticmethod
    def check_events(pacman, play_button, stats):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, pacman)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_buttons(play_button, mouse_x, mouse_y, stats)


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


def check_buttons(play_button, mouse_x, mouse_y, stats):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        pygame.mouse.set_visible(False)
        stats.game_active = True
    elif play_button.hs_image_rect.collidepoint(mouse_x, mouse_y):
        stats.show_hs = True
