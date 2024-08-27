import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Shooter")

# Load images
player_img = pygame.image.load('player.png')
player_img = pygame.transform.scale(player_img, (80, 80))
enemy_img = pygame.image.load('enemy.png')
enemy_img = pygame.transform.scale(enemy_img, (80, 80))

# Game variables
player_x = 370
player_y = 480
player_x_change = 0

enemy_x = random.randint(0, screen_width - 50)
enemy_y = random.randint(50, 150)
enemy_y_change = 40
enemy_x_change = 4

# Define functions
def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y):
    screen.blit(enemy_img, (x, y))

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Check if a keystroke is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_LEFT:
                player_x_change = 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_LEFT:
                player_x_change = 0
    
    # Update player position
    player_x += player_x_change

    # Boundary checking for player
    if player_x <= 10:
        player_x = 10
    elif player_x >= screen_width -100:
        player_x = screen_width -100

    # Update enemy position
    enemy_x += enemy_x_change

    if enemy_x <= 0:
        enemy_x_change = 3
        enemy_y += enemy_y_change
    elif enemy_x >= screen_width - 50:
        enemy_x_change = -4
        enemy_y += enemy_y_change

    # Collision detection
    collision = False
    if (enemy_y + 50 >= player_y and enemy_y <= player_y + 50):
        if (enemy_x + 50 >= player_x and enemy_x <= player_x + 50):
            collision = True

    if collision:
        running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw player and enemy
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()
