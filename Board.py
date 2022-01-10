import pygame
from Snake import Snake
import random

class Board:
    def __init__(self):
        self.colors = {
            'black' : pygame.Color(0,0,0),
            'white' : pygame.Color(255,255,255),
            'red' : pygame.Color(255,0,0),
            'green' : pygame.Color(0,255,0),
            'blue' : pygame.Color(0,0,255),
            'purple' : pygame.Color(128,0,128)
        }
        #display = pygame.display.set_mode((720,480))

        #display.fill(black)

        self.display = pygame.display.set_mode((720,480))
        self.display.fill(self.colors['black'])

    # def getDisplay(self):
    #     #display = pygame.display.set_mode((720,480))
    #     self.display.fill(self.colors['black'])
    #     return display

#snake = Snake().linkedlist


    #pygame.init()
class Food:

    def __init__(self):
        self.food = None
        self.x = None
        self.y = None

    def generateFood(self):
        #pygame.draw.rect(self.display, self.colors['green'], pygame.Rect(random.randint(1,720), random.randint(1,480), 10, 10))
        self.x = random.randint(1, (710 // 10)) * 10
        self.y = random.randint(1, (470 // 10)) * 10

        self.food = pygame.Rect(self.x, self.y, 10, 10)
        return self.food
