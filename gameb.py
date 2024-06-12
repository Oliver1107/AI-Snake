import pygame
import random
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

# --- Pygame Setup ---
pygame.init()
font = pygame.font.SysFont(None, 25)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

# Display
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake with Neural Network')
clock = pygame.time.Clock()

# Snake Properties
block_size = 10
snake_speed = 15


# --- Neural Network ---
class SnakeNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# --- Game Functions ---
def generate_food():
    foodx = round(random.randrange(0, dis_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - block_size) / 10.0) * 10.0
    return foodx, foody


def game_loop():
    game_over = False
    game_close = False

    # Snake Initial Position
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    snake_length = 1

    # Food
    foodx, foody = generate_food()

    # Neural Network
    input_size = 11  # Input features (direction, distances to food, walls, body)
    hidden_size = 256
    output_size = 3  # Output actions (left, straight, right)
    net = SnakeNet(input_size, hidden_size, output_size)
    optimizer = optim.Adam(net.parameters(), lr=0.01)

    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            # ... (Event handling for quitting or playing again) 

        # ... (Event handling for key presses to control the snake)

        # Input for Neural Network
        input_data = ... # Construct input data based on game state

        # Neural Network Decision
        output = net(torch.FloatTensor(input_data))
        action = torch.argmax(output).item()  # 0: left, 1: straight, 2: right

        # ... (Update snake movement based on the neural network's action)

        dis.fill(white)
        pygame.draw.rect(dis, green, [foodx, foody, block_size, block_size])
        for x, y in snake_list:
            pygame.draw.rect(dis, black, [x, y, block_size, block_size])
        
        # ... (Score display, collision checks, game over logic)

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()