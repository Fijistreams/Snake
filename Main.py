from Snake import Snake
import pygame
from Board import Board, Food
from Node import Node

snake = Snake()
snakelist = snake.linkedlist
black = pygame.Color(0,0,0)
board = Board()
foodobject = Food()
display = board.display
#display = board.getDisplay()
pygame.init()

fps = pygame.time.Clock()
direction = 'RIGHT'
INBOUNDS = True

food = foodobject.generateFood()

#tempnode = snakelist.head
#print(tempnode.data)

def checkInbounds(x,y):
    global INBOUNDS
    if(x > 720 or x < 0):
        INBOUNDS = False

    if(y > 480 or y < 0):
        INBOUNDS = False  

while True:
    tempnode = snakelist.head
    change_to = None

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    
    if(change_to == 'UP' and direction != 'DOWN'):
        direction = 'UP'

    if(change_to == 'DOWN' and direction != 'UP'):
        direction = 'DOWN'

    if(change_to == 'LEFT' and direction != 'RIGHT'):
        direction = 'LEFT'

    if(change_to == 'RIGHT' and direction != 'LEFT'):
        direction = 'RIGHT'

    snake.Move(direction)

    snakelist = snake.linkedlist
    display.fill(black)
    pygame.display.update()
       #snakelist.head.data[1] += 10
       #snakelist.printList()

    while(tempnode is not None):
        #print('trying')
        pygame.draw.rect(display, board.colors['purple'], pygame.Rect(tempnode.data[0], tempnode.data[1], 10, 10))
        pygame.draw.rect(display, board.colors['green'], food)
        tempnode = tempnode.nextnode

    #if head touches food
    if(snakelist.head.data[0] in range(foodobject.x - 5, foodobject.x + 5) and snakelist.head.data[1] in range(foodobject.y - 5, foodobject.y + 5) ):
        food = foodobject.generateFood()

        snake.addSegment('direction')

    if(snake.TOUCHING == True):
        pygame.quit()
        quit()

    checkInbounds(snakelist.head.data[0], snakelist.head.data[1])
    if(INBOUNDS == False):
        pygame.quit()
        quit()

    

    pygame.display.update()
    fps.tick(15)


