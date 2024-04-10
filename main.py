import pygame
import random
import sys

pygame.init()

sw = 640
sh = 460
screen = pygame.display.set_mode((sw,sh))

BLACK = (0,0,0)
WHITE = (255,255,255)

clock = pygame.time.Clock()
fps = 10


class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((sw / 2), (sh / 2))]
        self.direction = pygame.Vector2(1,0)
        self.color = (0,128,0)
        self.score = 0
        
    def draw(self, surface):
        for pos in self.positions:
            rect = pygame.Rect((pos[0],pos[1]), (20,20))
            pygame.draw.rect(surface,self.color,rect)
            
    def move(self):
        cur = self.positions[0]
        x,y = self.direction
        new = ((cur[0]+(x*20)) % sw, (cur[1]+(y*20)) % sh)
        if new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()
                
    def reset(self):
        self.length = 1
        self.positions = [((sw / 2),(sh /2))]
        self.direction = pygame.Vector2(1,0)
        self.score = 0

    def key_event(self,event):
        if event.key == pygame.K_UP and self.direction != (0,1):
            self.direction = pygame.Vector2(0,-1)
        elif event.key == pygame.K_DOWN and self.direction != (0,-1):
            self.direction = pygame.Vector2(0,1)
        elif event.key == pygame.K_LEFT and self.direction != (1,0):
            self.direction = pygame.Vector2(-1,0)
        elif event.key == pygame.K_RIGHT and self.direction != (-1,0):
            self.direction = pygame.Vector2(1,0)

class Food:
    def __init__(self):
        self.position = (0,0)
        self.color = (255,0,0)
        self.randomize_position()
        
    def randomize_position(self):
        self.position = (random.randint(0, (sw-20)//20) * 20,random.randint(0, (sh-20)//20) * 20 )
        
    def draw(self,surface):
        rect = pygame.Rect((self.position[0], self.position[1]),(20,20))
        pygame.draw.rect(surface, self.color, rect)

snake = Snake()
food = Food()

while True:
    for event  in  pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            snake.key_event(event)
            
    snake.move()
    head_x, head_y = snake.positions[0]
    food_x, food_y = food.position
    if head_x == food_x and head_y == food_y:
        print('colisao')
        snake.length += 1
        snake.score += 1
        food.randomize_position()
          
    screen.fill(BLACK)
    snake.draw(screen)
    food.draw(screen)
    pygame.display.flip()
    clock.tick(fps)