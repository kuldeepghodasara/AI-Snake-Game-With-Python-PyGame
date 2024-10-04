import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set screen width and height
width = 800
height = 600

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
dark_green = (0, 155, 0)

# Create the screen
screen = pygame.display.set_mode((width, height))

# Set the clock for controlling the game's frame rate
clock = pygame.time.Clock()

# Set block size and speed
block_size = 20
speed = 15

# Set fonts for displaying score
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, blue)
    screen.blit(value, [0, 0])

def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.ellipse(screen, dark_green, [x[0], x[1], block_size, block_size])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def get_next_direction(snake_head, food_pos, snake_list):
    # Simple AI to move towards the food while avoiding collisions
    directions = [
        (block_size, 0),  # Right
        (-block_size, 0),  # Left
        (0, block_size),  # Down
        (0, -block_size)  # Up
    ]
    best_direction = directions[0]
    min_distance = float('inf')

    for direction in directions:
        new_head = [snake_head[0] + direction[0], snake_head[1] + direction[1]]
        distance = ((new_head[0] - food_pos[0]) ** 2 + (new_head[1] - food_pos[1]) ** 2) ** 0.5

        if distance < min_distance and new_head not in snake_list and 0 <= new_head[0] < width and 0 <= new_head[1] < height:
            min_distance = distance
            best_direction = direction

    return best_direction

def gameLoop():  # Main function for the game
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Get AI direction
        x1_change, y1_change = get_next_direction([x1, y1], [foodx, foody], snake_List)

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.ellipse(screen, red, [foodx, foody, block_size, block_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(block_size, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(speed)

    pygame.quit()
    quit()

gameLoop()