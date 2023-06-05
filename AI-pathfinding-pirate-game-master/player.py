from enum import IntEnum

import pygame
from typing import List
from fsm import FSM
from shipcondition import ShipCondition
import math

PLAYER_SPEED = 1


class Player(pygame.sprite.Sprite):
    """Our Player's Pirate Ship!
    """
    #make the script talk to other scripts, match the health ton other self.player.dead vars
    def __init__(self) -> None:
        super().__init__()
        #state machine
        self.health = 10
        filenames = ["data/sprites/ships/ship (2).png",
                     "data/sprites/ships/ship (8).png",
                     "data/sprites/ships/ship (14).png",
                     "data/sprites/ships/ship (20).png"]
        self.fsm = FSM()
        self.fsm.setstate(self.update_healthy)
        # set the initial state
        self.prev_ship_condition = ShipCondition.HEALTHY
        self.ship_condition = ShipCondition.HEALTHY

        self.base_list = [pygame.image.load(filename).convert_alpha() for filename in filenames]
        self.base = self.base_list[0]
        self.image = self.base.copy()
        self.rect = self.image.get_rect()

        # current position and previous
        self._position = [0.0, 0.0]
        self._old_position = self.position
        self.destination = self.position

        self.dx, self.dy = 0, 0
        self.distance = 0

        self.use_AI = False

        # player game data/state
        self.mouse_down = False
        self.score = 0


    @property
    def position(self) -> List[float]:
        return list(self._position)

    @position.setter
    def position(self, value: List[float]) -> None:
        self._position = list(value)

    def update(self, dt: float) -> None:
        """ Updates the player's ship

        This function will attempt to lerp the player to their new
        destination. It will control the speed at which that happens
        using PLAYER_SPEED. Lerping has its issues but is a good start
        to make the game playable. The update function will also redraw
        the ship if it's condition changes.

        Args:
            dt (float): The time elapsed since last tick
        """
        if self.use_AI is not True:
            self._old_position = self._position[:]

            dest_vector = pygame.Vector2(self.destination[0], self.destination[1])
            pos_vector = pygame.Vector2(self._position[0], self._position[1])

            lerped = pos_vector.lerp(dest_vector, min(PLAYER_SPEED * dt, 1))
            self._position[0] = lerped[0]
            self._position[1] = lerped[1]

        else:
            dest_vector = pygame.Vector2(self.destination[0], self.destination[1])
            radians = math.atan2(dest_vector[1] - self._old_position[1], dest_vector[0] - self._old_position[0])

            self.distance = math.hypot(dest_vector[0] - self._old_position[0], dest_vector[1] - self._old_position[1])

            self.distance = int(self.distance)

            self.dx = math.cos(radians)
            self.dy = math.sin(radians)

            self._old_position = self._position[:]

            if self.distance:
                self.distance -= 1
                self._position[0] += self.dx
                self._position[1] += self.dy

            rad = math.atan2(self.dy, self.dx)
            self.rotate(math.degrees(rad))

        self.rect.topleft = self._position


        self.fsm.update()

        if self.ship_condition != self.prev_ship_condition:
            self.prev_ship_condition = self.ship_condition
            self.redraw()





    def move_back(self, dt: float) -> None:
        """If called after an update, the sprite will move back"""
        self._position = self._old_position
        self.destination = self._old_position
        self.rect.topleft = self._position



    def rotate(self, angle: float) -> None:
        """rotates the image so that it always points to direction of travel"""
        self.image = pygame.transform.rotozoom(self.base, 90 - angle, 1)
        x, y = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def redraw(self) -> None:
        """redraws the ship based on its current condition

        There's a bug inside this function, see if you can locate it
        and resolve it. It's easy to replicate by altering your ship's  #look at this after for more marks probably somthing to do with the rotation and when the sprite changes
        condition whilst pointing at a new destination.
        """
        if self.ship_condition < 4:
            self.base = self.base_list[self.ship_condition]
            self.image = self.base.copy()
            self.rect = self.image.get_rect()





    def update_healthy(self):
        self.ship_condition = ShipCondition.HEALTHY
        if self.health <= 6:
            self.fsm.setstate(self.update_damaged)

    def update_damaged(self):
        self.ship_condition = ShipCondition.DAMAGED
        if self.health <= 3:
            self.fsm.setstate(self.update_very_damaged)

    def update_very_damaged(self):
        self.ship_condition = ShipCondition.VERY_DAMAGED
        if self.health == 0:
            self.fsm.setstate(self.deaded)

    def deaded(self):
        self.ship_condition = ShipCondition.SUNK


