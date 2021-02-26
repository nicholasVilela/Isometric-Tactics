import pygame, sys, state, constants
from game import Game


def start():
    clock = pygame.time.Clock()
    game = Game(state.screen)

    def quit_game():
        pygame.quit()
        sys.exit()

    while game.running:
        game.layers['background'].fill(constants.SCREEN_FILL)
        game.layers['midground'].fill(constants.COLORS['black'])
        game.layers['foreground'].fill(constants.COLORS['black'])

        game.update()

        state.screen.blit(game.layers['background'], (0, 0))
        state.screen.blit(game.layers['midground'], (0, 0))
        state.screen.blit(game.layers['foreground'], (0, 0))

        pygame.display.update()
        clock.tick(constants.FRAMERATE)

    quit_game()


pygame.init()
pygame.display.set_caption('Isometric Tactics')
start()