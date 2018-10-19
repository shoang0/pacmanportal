import pygame
from maze import Maze
from eventloop import EventLoop
from pacman import Pacman
from ghosts import Ghosts
from button import Button
# from expandfile import ExpandFile


class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Pacman Portal")
        # self.expandfile = ExpandFile('images/pacman_maze.txt', expandBy=3)
        self.maze = Maze(self.screen, mazefile='images/pacman_maze_expanded.txt', brickfile='brick')
        self.pacman = Pacman(self.screen)
        self.ghosts = Ghosts(self.screen)
        self.play_button = Button(self.screen, "Play")

    def __str__(self): return 'Game(Pacman Portal), maze=' + str(self.maze) + ')'

    def play(self):
        eloop = EventLoop(finished=False)
        while not eloop.finished:
            eloop.check_events(self.pacman, self.play_button)
            self.pacman.update()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(Game.BLACK)
        self.maze.blitme()
        self.pacman.blitme()
        self.ghosts.blitme()
        pygame.display.flip()


game = Game()
game.play()
