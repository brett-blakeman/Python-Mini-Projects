import pygame
import random 

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (50, 120, 50)
RED = (255, 0, 0)
DARK_GREEN = (0, 155, 0)
BLUE = (0, 0, 255)
WALL_COLOR = (120, 70, 15)

pygame.init()

#Screen Size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

block = 20

#starting position of the snake
x = WIDTH // 2
y = HEIGHT // 2

#User-defined number of food spawned
food_count = 25
foods = []

#movement speed
x_change = 0
y_change = 0

body = []
length = 1

wall_thickness = block

#Top Wall
pygame.draw.rect(screen, WALL_COLOR, (0, 0, WIDTH, wall_thickness))
#Bottom Wall
pygame.draw.rect(screen, WALL_COLOR, (0, HEIGHT - wall_thickness, WIDTH, wall_thickness))
#Left Wall
pygame.draw.rect(screen, WALL_COLOR, (0, 0, wall_thickness, HEIGHT))
#Right Wall
pygame.draw.rect(screen, WALL_COLOR, (WIDTH - wall_thickness, 0, wall_thickness, HEIGHT))

#Food Position
for i in range(food_count):
    food_x = random.randrange(0, WIDTH, block)
    food_y = random.randrange(0, HEIGHT, block)
    foods.append([food_x, food_y])

score = 0

clock = pygame.time.Clock()

#Game Loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        
        #Movement Controls
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                x_change = -block
                y_change = 0
            elif event.key ==pygame.K_RIGHT:
                x_change = block
                y_change = 0
            elif event.key ==pygame.K_UP:
                x_change = 0
                y_change = -block
            elif event.key ==pygame.K_DOWN:
                x_change = 0
                y_change = block

    #Update the position of the snake
    x += x_change
    y += y_change

    #Wall Collision
    if ( x < block or x >= WIDTH - block or y < block or y >= HEIGHT - block):
        running = False

    #new head position
    head = [x, y]
    #Add the new head to the body
    body.append(head)

    #keep the length correct by removing the tail if necessary
    if len(body) > length:
        del body[0]

    #self collision
    for segment in body[:-1]:
        if segment == head:
            running = False

    #Check for collision with food
    for food in foods:
        if x == food[0] and y == food[1]:
            length += 1
            score += 1
            food[0] = random.randrange(0, WIDTH, block)
            food[1] = random.randrange(0, HEIGHT, block)

    #Spawn new food if the current food is eaten
    if x == food_x and y == food_y:
        food_x = random.randrange(0, WIDTH, block)
        food_y = random.randrange(0, HEIGHT, block)
    
    #Fills background with light green and dark green checkered pattern
    for row in range(HEIGHT // block):
        for col in range(WIDTH // block):
                #Alternate colors for a checkered pattern
            if (row + col) % 2 == 0:
                    color = LIGHT_GREEN
            else:
                    color = DARK_GREEN
            pygame.draw.rect(screen, color, (col * block, row * block, block, block))

    #Draw the food
    for food in foods:
        pygame.draw.rect(screen, RED, (food[0], food[1], block, block))

    #Draw the body
    for segment in body:
            pygame.draw.rect(screen, BLUE, (segment[0] + 2, segment[1] + 2, block - 4, block - 4))

    #Score Display
    font = pygame.font.SysFont(None, 35)
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

    #Updates the screen
    pygame.display.update()

    clock.tick(10) #FPS

pygame.quit()

print("Game Over! Your final score is: " + str(score))