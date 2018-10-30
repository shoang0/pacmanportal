import pygame.font


class Button:
    def __init__(self, screen, msg):
        """Initialize button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.msg_image = None
        self.msg_image_rect = None
        self.title_image = None
        self.title_image_rect = None
        self.hs_image = None
        self.hs_image_rect = None

        # Set dimensions and properties of buttons
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build play button's rect obj and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.top = self.screen_rect.bottom - 100

        # prep button once
        self.prep_msg(msg)
        self.prep_title()
        self.prep_hs()
        # self.targetvalues()

    def prep_msg(self, msg):
        """Turn msg into rendered image and center text on button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.msg_image_rect.top = self.screen_rect.bottom - 100

    def prep_title(self):
        """Turn game title display into image and place on screen"""
        self.font = pygame.font.SysFont(None, 120)
        title = "PACMAN"
        self.title_image = self.font.render(title, True, self.text_color, self.button_color)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.center = self.rect.center
        self.title_image_rect.top = self.screen_rect.top + 50

    def prep_hs(self):
        self.font = pygame.font.SysFont(None, 48)
        hs = "High Scores"
        self.hs_image = self.font.render(hs, True, self.text_color, self.button_color)
        self.hs_image_rect = self.hs_image.get_rect()
        self.hs_image_rect.center = self.rect.center
        self.hs_image_rect.top = self.screen_rect.bottom - 50

    def draw_button(self):
        # Draw button and title
        self.screen.fill((0, 0, 0))
        self.screen.fill(self.button_color, self.screen_rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.title_image, self.title_image_rect)
        self.screen.blit(self.hs_image, self.hs_image_rect)
        pygame.display.flip()
