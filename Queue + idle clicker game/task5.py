import sys
import math
from time import time
import pygame.mixer
from pygame.locals import *
import random
from enum import Enum

pygame.init()
pygame.font.init()
screen_height = 800
screen_width = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Clicker game")

font = pygame.font.Font('freesansbold.ttf', 20)
white = (255, 255, 255)


class type_of_missions(Enum): # types of missions
    TC = 1   # accumulate a total of clicks
    CPS = 2   # clicks per second


class game_screen(Enum):   # different scenes used in the game
    game_screen = 1
    shop_screen = 2
    Missions_screen = 3


class Missions(object):
    def __init__(self):
        self.type = None
        self.amount = None
        self.clickps = None
        self.reward = None
        n = random.randint(0, 1)
        if n == 0:
            self.type = type_of_missions.TC
            Missions.tc(self)
        if n == 1:
            self.type = type_of_missions.CPS
            Missions.cps(self)

    def cps(self):
        self.amount = 1
        n = random.randint(3, 10)
        self.clickps = n
        n = random.randint(60, 300)
        self.reward = n

    def tc(self):
        n = random.randint(30, 100)
        self.amount = n
        n = random.randint(60, 300)
        self.reward = n


class Queue:
    def __init__(self):
        self.queue = []

    def createMission(self):

        if Queue.getSize(self) < 3:
            miss = Missions()
            self.queue.append(miss)
        else:
            print("you already have enough missions")

    def dequeue(self, index):
        self.queue.pop(index)

    def returnData(self, index):
        data_mission = self.queue[index]
        if data_mission.type == type_of_missions.TC:
            return data_mission.type, data_mission.amount, data_mission.reward
        else:
            return data_mission.type, data_mission.amount, data_mission.reward, data_mission.clickps

    def getSize(self):
        size = 0
        for x in self.queue:
            size += 1
        return size


def mouseInputs(event):
    if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
            return 1


if __name__ == '__main__':
    start = 0
    money = 0
    clicks_per_sec = 0
    total_clicks = 0

    cost_cm = 200
    cost_psi = 100
    click_multiplier = 1
    passive_score_increase = 0

    mission_queue = Queue()
    mission_queue.createMission()

    scene = game_screen.game_screen

    while True:
        m_x, m_y = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))

        if scene == game_screen.game_screen:

            # rect and text setting
            Clicker_Button = pygame.Rect(50, 100, 200, 50)
            pygame.draw.rect(screen, (255, 255, 0), Clicker_Button)

            to_shop_button = pygame.Rect(300, 100, 200, 50)
            pygame.draw.rect(screen, (255, 37, 0), to_shop_button)

            to_missions_button = pygame.Rect(500, 100, 200, 50)
            pygame.draw.rect(screen, (255, 122, 0), to_missions_button)

            screen.blit(font.render("Shop", True, (255, 255, 0)), (to_shop_button.topleft[0], to_shop_button.topleft[1]))
            screen.blit(font.render("Missions", True, (255, 255, 0)), (to_missions_button.topleft[0], to_missions_button.topleft[1]))

            current_mission = pygame.Rect(50, 200, 200, 100)


            if Clicker_Button.collidepoint((m_x, m_y)):
                if click:
                    total_clicks += 1
                    money += 1 * click_multiplier
                    clicks_per_sec += 1
            if to_missions_button.collidepoint((m_x, m_y)):
                if click:
                    scene = game_screen.Missions_screen
            if to_shop_button.collidepoint((m_x, m_y)):
                if click:
                    scene = game_screen.shop_screen


            # writes the info of the current mission
            if mission_queue.getSize() >= 1:
                if mission_queue.returnData(0)[0] == type_of_missions.TC:
                    screen.blit(font.render(str(mission_queue.returnData(0)[0]), True, (255, 255, 0)), (50, current_mission.topleft[1] + 20))
                    screen.blit(font.render("this is the amount of clicks to reach: " + str(mission_queue.returnData(0)[1]) + ". Right now your click count is " + str(total_clicks), True, (255, 255, 0)), (50, current_mission.topleft[1] + 50))
                    screen.blit(font.render("If you complete the task, as a reward you will get " + str(mission_queue.returnData(0)[2]), True, (255, 255, 0)), (50, current_mission.topleft[1] + 80))
                else:
                    screen.blit(font.render(str(mission_queue.returnData(0)[0]), True, (255, 255, 0)), (50, current_mission.topleft[1] + 20))
                    screen.blit(font.render("Click the clicker this amount of times in one second: " + str(mission_queue.returnData(0)[3]), True, (255, 255, 0)), (50, current_mission.topleft[1] + 50))
                    screen.blit(font.render("If you complete the task, as a reward you will get " + str(mission_queue.returnData(0)[2]), True, (255, 255, 0)), (50, current_mission.topleft[1] + 80))

                # checking the mission and if statements to give the winning scenarios
                if total_clicks == mission_queue.returnData(0)[1] and mission_queue.returnData(0)[0] == type_of_missions.TC:
                    total_clicks = 0
                    money += mission_queue.returnData(0)[2]
                    mission_queue.dequeue(0)
                elif mission_queue.returnData(0)[0] == type_of_missions.CPS and clicks_per_sec >= mission_queue.returnData(0)[3]:
                    total_clicks = 0
                    money += mission_queue.returnData(0)[2]
                    mission_queue.dequeue(0)

            screen.blit(font.render(str(money) + " score", True, (255, 255, 0)), (50, current_mission.centery + 150))



            # 1 second timer
            if time() > start:
                clicks_per_sec = 0
                money += passive_score_increase
                start = time() + 1

        ####################################################################################################
        elif scene == game_screen.shop_screen:

            # rect and text setting
            exit_button = pygame.Rect(screen.get_width() - 50, 0, 50, 50)
            Upgrade_click_button = pygame.Rect(200, 150, 600, 50)
            Upgrade_psi_button = pygame.Rect(200, 250, 600, 50)

            pygame.draw.rect(screen, (255, 0, 0), exit_button)
            pygame.draw.rect(screen, (255, 0, 0), Upgrade_click_button)
            pygame.draw.rect(screen, (255, 0, 0), Upgrade_psi_button)

            screen.blit(font.render('X', True, (255, 88, 0)), (exit_button.topleft[0], exit_button.topleft[1]))
            screen.blit(font.render('To upgrade the passive income is going to cost you ' + str(cost_psi), True, (255, 213, 0)), (Upgrade_psi_button.topleft[0], Upgrade_psi_button.topleft[1]))
            screen.blit(font.render('To upgrade the click multiplier is going to cost you ' + str(cost_cm), True, (255, 213, 0)), (Upgrade_click_button.topleft[0], Upgrade_click_button.topleft[1]))
            screen.blit(font.render('you have this amount of money right now ' + str(money), True, (255, 213, 0)), (Upgrade_click_button.topleft[0], Upgrade_click_button.topleft[1] + 250))


            #event checking
            if exit_button.collidepoint((m_x, m_y)):
                if click:
                    scene = game_screen.game_screen
            if Upgrade_click_button.collidepoint((m_x, m_y)):
                if click:
                    if money >= cost_cm:
                        money -= cost_cm
                        cost_cm = (math.log2(cost_cm) * cost_cm) // 2
                        cost_cm = round(cost_cm)
                        click_multiplier += 1

            if Upgrade_psi_button.collidepoint((m_x, m_y)):
                if click:
                    if money >= cost_psi:
                        money -= cost_psi
                        cost_psi = (math.log2(cost_psi) * cost_psi) // 2
                        cost_psi = round(cost_psi)
                        passive_score_increase += 5

        ####################################################################################################
        elif scene == game_screen.Missions_screen:

            # rect and text setting
            exit_button = pygame.Rect(screen.get_width() - 50, 0, 50, 50)
            Mission1 = pygame.Rect(50, 100, 700, 150)
            Mission2 = pygame.Rect(50, 300, 700, 150)
            Mission3 = pygame.Rect(50, 500, 700, 150)
            Buy_task_button = pygame.Rect(50, 750, 250, 50)
            skip_task_button = pygame.Rect(50, 50, 300, 50)
            title = pygame.Rect((screen_width // 2) - 100, 0, 250, 25)

            pygame.draw.rect(screen, (255, 0, 0), exit_button)
            pygame.draw.rect(screen, (255, 0, 0), Mission1)
            pygame.draw.rect(screen, (255, 0, 0), Mission2)
            pygame.draw.rect(screen, (255, 0, 0), Mission3)
            pygame.draw.rect(screen, (0, 255, 0), Buy_task_button)
            pygame.draw.rect(screen, (255, 123, 0), skip_task_button)
            pygame.draw.rect(screen, (255, 0, 0), title)

            screen.blit(font.render('X', True, (255, 88, 0)), (exit_button.topleft[0], exit_button.topleft[1]))
            screen.blit(font.render('missions', True, (255, 213, 0)), (title.topleft[0], title.topleft[1]))
            screen.blit(font.render('buy a mission for 40!', True, (255, 213, 0)), (Buy_task_button.topleft[0], Buy_task_button.topleft[1]))
            screen.blit(font.render('want to skip this mission?', True, (255, 213, 0)), (skip_task_button.topleft[0], skip_task_button.topleft[1]))


            # collision setting
            if exit_button.collidepoint((m_x, m_y)):
                if click:
                    scene = game_screen.game_screen

            if Buy_task_button.collidepoint((m_x, m_y)):
                if click:
                    if mission_queue.getSize() < 4 and money > 40:
                        money -= 40
                        mission_queue.createMission()
            if skip_task_button.collidepoint((m_x, m_y)):
                if click:
                    if mission_queue.getSize() >= 1:
                        total_clicks = 0
                        mission_queue.dequeue(0)


            if mission_queue.getSize() >= 1:
                if mission_queue.returnData(0)[0] == type_of_missions.TC:
                    screen.blit(font.render("Click the counter a total of this times", True, white), (Mission1.topleft[0], Mission1.topleft[1] + 30))
                    screen.blit(font.render(str(mission_queue.returnData(0)[1]), True, white), (Mission1.topleft[0], Mission1.topleft[1] + 60))
                    screen.blit(font.render(str(mission_queue.returnData(0)[2]) + " this will be our reward", True, white), (Mission1.topleft[0], Mission1.topleft[1] + 90))
                else:
                    screen.blit(font.render("click the counter this amount of times per second mission,", True, white), (Mission1.topleft[0], Mission1.topleft[1] + 30))
                    screen.blit(font.render(str(mission_queue.returnData(0)[2]) + " this will be our reward", True, white), (Mission1.topleft[0], Mission1.topleft[1] + 60))
                    screen.blit(font.render("Achieve " + str(mission_queue.returnData(0)[3]) + " clicks in 1 second", True, white), (Mission1.topleft[0], Mission1.topleft[1] + 90))
            else:
                screen.blit(font.render("looks like there are no missions here, why don't you buy a mission?", True, white), (Mission1.topleft[0], Mission1.topleft[1] + 20))

            if mission_queue.getSize() >= 2:
                if mission_queue.returnData(1)[0] == type_of_missions.TC:
                    screen.blit(font.render("Click the counter a total of this times", True, white),(Mission2.topleft[0], Mission2.topleft[1] + 30))
                    screen.blit(font.render(str(mission_queue.returnData(1)[1]), True, white), (Mission2.topleft[0], Mission2.topleft[1] + 60))
                    screen.blit(font.render(str(mission_queue.returnData(1)[2]) + " this will be our reward", True, white), (Mission2.topleft[0], Mission2.topleft[1] + 90))
                else:
                    screen.blit(font.render("click the counter this amount of times per second mission,", True, white), (Mission2.topleft[0], Mission2.topleft[1] + 30))
                    screen.blit(font.render(str(mission_queue.returnData(1)[2]) + " this will be our reward", True, white), (Mission2.topleft[0], Mission2.topleft[1] + 60))
                    screen.blit(font.render("Achieve " + str(mission_queue.returnData(1)[3]) + " clicks in 1 second", True, white), (Mission2.topleft[0], Mission2.topleft[1] + 90))
            else:
                screen.blit(font.render("looks like there are no missions here, why don't you buy a mission?", True, white), (Mission2.topleft[0], Mission2.topleft[1] + 20))

            if mission_queue.getSize() >= 3:
                if mission_queue.returnData(2)[0] == type_of_missions.TC:
                    screen.blit(font.render("Click the counter a total of this times", True, white),(Mission3.topleft[0], Mission3.topleft[1] + 30))
                    screen.blit(font.render(str(mission_queue.returnData(2)[1]) + " amount", True, white), (Mission3.topleft[0], Mission3.topleft[1] + 60))
                    screen.blit(font.render(str(mission_queue.returnData(2)[2]) + " this will be our reward", True, white), (Mission3.topleft[0], Mission3.topleft[1] + 90))
                else:
                    screen.blit(font.render("click the counter this amount of times per second mission,", True, white), (Mission3.topleft[0], Mission3.topleft[1] + 30))
                    screen.blit(font.render(str(mission_queue.returnData(2)[2]) + " this will be our reward", True, white), (Mission3.topleft[0], Mission3.topleft[1] + 60))
                    screen.blit(font.render("Achieve " + str(mission_queue.returnData(2)[3]) + " clicks in 1 second", True, white), (Mission3.topleft[0], Mission3.topleft[1] + 90))
            else:
                screen.blit(font.render("looks like there are no missions here, why don't you buy a mission?", True, white), (Mission3.topleft[0], Mission3.topleft[1] + 20))


        # event checking
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if mouseInputs(event) == 1:
                click = True
        pygame.display.update()

sys.exit(0)
