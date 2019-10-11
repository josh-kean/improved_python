import sys, pygame
import random as rand
import os
import time
from pi import pi

pygame.init()

#keeps all game constants for the game

class Assets:
    def __init__(self):
        self.colors = {'black': (0, 0, 0), 'white': (255, 255, 255), 'red': (255, 0, 0)}
        self.width = 1000
        self.height = 1000
        self.display = pygame.display.set_mode((self.width, self.height))
        self.body_width = 50
        self.key_down = ''
        self.images = {
                0: 'zero.png',
                1: 'one.png',
                2: 'two.png',
                3: 'three.png',
                4: 'four.png',
                5: 'five.png',
                6: 'six.png',
                7: 'seven.png',
                8: 'eight.png',
                9: 'nine.png'
        }
        self.pi = pi

    def num_images(self, num):
        self.num = num
        return self.images[self.num]

#maintains the state of the game, including current digit, score, etc.
class State(Assets):
    def __init__(self):
        Assets.__init__(self)
        self.dir_change = [-50, 0] #changes direction of the snake
        self.keys = {
                pygame.K_UP: [0, -50],
                pygame.K_DOWN: [0, 50],
                pygame.K_LEFT: [-50, 0],
                pygame.K_RIGHT: [50, 0]
        }

#contains functions to draw snake //todo add function to move snake
class Snake(State):
    def __init__(self):
        State.__init__(self)
        self.snake_positions = [[500, 50], [550, 50], [600, 50], [650, 50]]
        self.head = [self.snake_positions[0]] #head is the new head of the snake
        self.length = 4

#displays an image file onto the screen
    def display_number(self, pos):
        image = pygame.image.load(os.path.join('images', self.images[pi[pos]]))
        self.display.blit(image, (self.snake_positions[pos][0], self.snake_positions[pos][1]))

#goes through all items in digits list
    def draw_snake(self):
        for x in range(self.length):
            self.display_number(x)

    def move_snake(self, event):
        if event.key in self.keys:
            if abs(self.dir_change[0]) == abs(self.keys[event.key][0]):
                return True
            if abs(self.dir_change[1]) == abs(self.keys[event.key][1]):
                return True
            self.key_down = event.key
            self.dir_change = self.keys[event.key]

    def detect_death(self):
        if self.snake_positions[0] in self.snake_positions[1:]:
            return False
        if self.snake_positions[0][0] < 0 or self.snake_positions[0][0] > self.width:
            return False
        if self.snake_positions[0][1] < 0 or self.snake_positions[0][1] > self.height:
            return False
        else:
            return True

    def update_snake(self):
        self.head = list(self.snake_positions[0])
        self.head[0] += self.dir_change[0]
        self.head[1] += self.dir_change[1]
        self.snake_positions = [self.head] + self.snake_positions[:self.length]
        self.draw_snake()


#functions to display food
class Food(Snake):
    def __init__(self):
        Snake.__init__(self)
        self.foodx = rand.randrange( 50, 500, 50)
        self.foody = rand.randrange( 50, 500, 50)
        self.food_position = [self.foodx, self.foody]

#displays the food square onto the screen
    def make_food(self, length):
        image = pygame.image.load(os.path.join('images', self.images[pi[length]]))
        self.display.blit(image, (self.foodx, self.foody))

#creates a random x, y coordinate for the food
    def make_x_y(self, excluded_points):
        self.foodx = rand.randrange( 50, 500, 50)
        self.foody = rand.randrange( 50, 500, 50)
        if [self.foodx, self.foody] in excluded_points:
            self.foodx = rand.randrange( 50, 500, 50)
            self.foody = rand.randrange( 50, 500, 50)
            
        self.food_position = [self.foodx, self.foody]

def detect_collision(snake_body, food_position):
    if snake_body[0] == food_position:
        snake.length+=1
        food.make_x_y(snake_body[1:])

assets = Assets()
snake = Snake()
food = Food()
state = State()

def start_screen():
    game = True
    while game:
        assets.display.fill(assets.colors['white'])
        food.make_food(snake.length)
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif action.type == pygame.KEYDOWN:
                snake.move_snake(action)
                continue
        snake.update_snake()
        detect_collision(snake.snake_positions, food.food_position)
        time.sleep(.1)
        game = snake.detect_death()
        pygame.display.update()

start_screen()
pygame.quit()
quit()
