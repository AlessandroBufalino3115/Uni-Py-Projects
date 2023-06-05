import math
import random

import pygame.mixer

pygame.init()
pygame.font.init()
screen_height = 1000
screen_width = 2000

number_asteroids = 100
G_const = 6.67428e-11

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Physics sim")

font = pygame.font.Font('freesansbold.ttf', 20)
white = (255, 255, 255)


class Asteroid:
    def __init__(self, Velocity_x, Velocity_y, Position_x, Position_y, Mass):
        self.velocity_x = Velocity_x
        self.velocity_y = Velocity_y
        self.position_x = Position_x
        self.position_y = Position_y
        self.mass = Mass

    def normalise(self, influ_pos_x, influ_pos_y): # direction calculation
        magnitude = math.sqrt(pow((influ_pos_x - self.position_x), 2) + pow((influ_pos_y - self.position_y), 2))

        if magnitude == 0:
            return 0, 0

        ret_x = (self.position_x - influ_pos_x) / magnitude
        ret_y = (self.position_y - influ_pos_y) / magnitude

        return -ret_x, -ret_y

        # unit vector from above

    def gravitational_equation(self, other_ast_mass, other_ast_pos_x, other_ast_pos_y):  # for x and for y alone

        unit_array = self.normalise(other_ast_pos_x, other_ast_pos_y)  # gets the direction of the force

        distance_x = other_ast_pos_x - self.position_x
        distance_y = other_ast_pos_y - self.position_y
        distance_hypo = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if self.position_x != other_ast_pos_x:
            force_x = unit_array[0] * G_const * (self.mass * other_ast_mass) / pow(distance_hypo, 2)  # on the same axis it gives issues
        else:
            force_x = 0

        if self.position_y != other_ast_pos_y:
            force_y = unit_array[1] * G_const * (self.mass * other_ast_mass) / pow(distance_hypo, 2)  # force per axis
        else:
            force_y = 0

        return force_x, force_y


if __name__ == '__main__':

    asteroid_arr_physics = [None] * number_asteroids
    asteroid_arr_rects = [None] * number_asteroids  # starting the arrays

    for i in range(number_asteroids):
        asteroid_arr_physics[i] = Asteroid(0, 0, random.randint((screen_width // 2) - 300, (screen_width // 2) + 300), random.randint((screen_height // 2) - 300, (screen_height // 2) + 300), 800000000)
        asteroid_arr_rects[i] = pygame.Rect(asteroid_arr_physics[i].position_x, asteroid_arr_physics[i].position_y, 5, 5)  # setting the arrays

    asteroid_arr_physics[0].mass = 80000000000
    asteroid_arr_physics[0].position_x = screen_width // 2
    asteroid_arr_physics[0].position_y = screen_height // 2  # middle point asteroid creation

    asteroid_arr_rects[0] = pygame.Rect(asteroid_arr_physics[0].position_x, asteroid_arr_physics[0].position_y, 10, 10)

    while True:
        dt = clock.tick(60)
        screen.fill((0, 0, 0))

        for s in range(number_asteroids):  # loop to draw the rects
            if s == 0:
                pygame.draw.rect(screen, (255, 0, 0), asteroid_arr_rects[s])  # the first one we want to be drawn as red to show the middle point
            else:
                pygame.draw.rect(screen, white, asteroid_arr_rects[s])

        for i in range(1, number_asteroids):  # for each asteroid in the array, skip the first one because that is the main one and that doesnt move

            force_x = 0
            force_y = 0  #reset the resultnat force counter to get the total force on each axis acted on the asteroid

            for x in range(number_asteroids):  # we loop through all the other asteroid to get the resultant force

                if x != i:
                    force_arr = asteroid_arr_physics[i].gravitational_equation(asteroid_arr_physics[x].mass, asteroid_arr_physics[x].position_x, asteroid_arr_physics[x].position_y)

                    force_x += force_arr[0]
                    force_y += force_arr[1]

            acc_x = force_x / asteroid_arr_physics[i].mass  # calculate the acceleration for each axis
            acc_y = force_y / asteroid_arr_physics[i].mass

            vel_x = (asteroid_arr_physics[i].velocity_x + (acc_x * dt)) # calculate the velocity for each axis
            vel_y = (asteroid_arr_physics[i].velocity_y + (acc_y * dt))

            asteroid_arr_physics[i].velocity_x = vel_x  # saving the speed
            asteroid_arr_physics[i].velocity_y = vel_y

            new_pos_x = (asteroid_arr_physics[i].position_x + (asteroid_arr_physics[i].velocity_x * dt))
            new_pos_y = (asteroid_arr_physics[i].position_y + (asteroid_arr_physics[i].velocity_y * dt))  # calculate the new position

            asteroid_arr_rects[i] = pygame.Rect(round(new_pos_x), round(new_pos_y), 5, 5)  # creating a new rect with the new positions

            asteroid_arr_physics[i].position_x = new_pos_x
            asteroid_arr_physics[i].position_y = new_pos_y    # saving the old position

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
