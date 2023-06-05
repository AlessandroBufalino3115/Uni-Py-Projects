import pygame

from gamestate import GameState
from gamestate import GameStateID
from gamedata import GameData


class GameMenu(GameState):

    def __init__(self, gamedata: GameData) -> None:
        super().__init__(gamedata)
        self.id = GameStateID.START_MENU
        self.start = False

        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.bg = pygame.image.load("data\sprites\\background image.jpg")

    def input(self, event: pygame.event) -> None:
        """ Handles the user input to select menu items """

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.start = True


    def update(self, dt: float) -> GameStateID:
        """ If menu item is selected transition to appropriate state else return START_MENU """

        if self.start is True:
            return GameStateID.GAMEPLAY

        return GameStateID.START_MENU

    def render(self, screen: pygame.Surface) -> None:
        """ Use pygame to draw the menu """

        screen.blit(self.bg, [0, 0])

        rect_background = pygame.Rect(700, 500, 700, 150)
        pygame.draw.rect(screen, (0, 255, 255), rect_background)

        screen.blit(self.font.render('Welcome to the start menu. Press the "Enter" key to begin', True, (255, 255, 0)), (rect_background.topleft[0] + 30, rect_background.topleft[1] + 60))
