import pygame

from gamestate import GameState
from gamestate import GameStateID
from gamedata import GameData


class GameOver(GameState):

    def __init__(self, data: GameData) -> None:
        super().__init__(data)
        self.id = GameStateID.GAME_OVER
        self.user_clicked = False
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.bg = pygame.image.load("data\sprites\\background_image_loss.jpg")

    def update(self, dt: float) -> GameStateID:
        """ If user_clicked go to game menu else return GAME_OVER"""
        if self.user_clicked:
            return GameStateID.START_MENU

        return GameStateID.GAME_OVER

    def render(self, screen: pygame.Surface) -> None:
        """ Renders the game lost message / assets """

        screen.blit(self.bg, [0, 0])

        rect_background = pygame.Rect(700, 500, 700, 150)
        pygame.draw.rect(screen, (0, 0, 0), rect_background)

        screen.blit(self.font.render('Oh no you died. Press the "Enter" key to go back to the start menu', True, (255, 255, 0)), (rect_background.topleft[0] + 30, rect_background.topleft[1] + 60))


    def input(self, event: pygame.event) -> None:
        """ Checks to see if user clicks button and set user_clicked """
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.user_clicked = True

        print("processing input")
