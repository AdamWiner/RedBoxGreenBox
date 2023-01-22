import pygame
import random
import os

score = 0
lives = 3
bullet_list = []
alien_bullet_list = []


def increment_score(points):
    global score
    score += points


def decrement_lives():
    global lives
    lives -= 1


def fire_bullet():
    global bullet_list
    bullet_list.append((player_x_pos, player_y_pos))


def fire_alien_bullet():
    global alien_bullet_list
    alien_bullet_list.append((alien_x_pos, alien_y_pos))


# Set the working directory
directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(directory)

# Initialize pygame
pygame.init()

# Load the music file
pygame.mixer.music.load("music.mp3")

# Set screen size
size = (800, 600)
screen = pygame.display.set_mode(size)

# Set title
pygame.display.set_caption("Red Box Green Box ")

# Set colors
black = (0, 0, 0)
white = (255, 255, 255)

# Load the music file
pygame.mixer.music.load("music.mp3")

# Load player and alien images
player_image = pygame.Surface((50, 50))
player_image.fill((0, 255, 0))
alien_image = pygame.Surface((50, 50))
alien_image.fill((255, 0, 0))

# Set initial positions
player_x_pos = 350
player_y_pos = 450
alien_x_pos = random.randint(50, 650)
alien_y_pos = 50

# Set speed
alien_speed = 6

# Set font
font = pygame.font.Font(None, 30)

# Play the music
pygame.mixer.music.play(-1)

# Set game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_pos -= 100
            elif event.key == pygame.K_RIGHT:
                player_x_pos += 100
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            fire_bullet()
            if event.key == pygame.K_m:
                if pygame.mixer.music.get_volume() > 0:
                    pygame.mixer.music.set_volume(0)
                else:
                    pygame.mixer.music.set_volume(1)

       # Move and draw bullets
    if bullet_list:
        for i, bullet in enumerate(bullet_list):
            if player_x_pos > 0 and player_x_pos < 700:
                pygame.draw.rect(screen, white, (bullet[0], bullet[1], 10, 20))
                bullet_y_pos = bullet[1]
                bullet_x_pos = bullet[0]
                bullet_y_pos -= 10
                bullet = (bullet_x_pos, bullet_y_pos)
                if bullet[0] > alien_x_pos and bullet[0] < alien_x_pos + 50 and bullet[1] > alien_y_pos and bullet[1] < alien_y_pos + 50:
                    alien_x_pos = -50
                    alien_y_pos = -50
                    bullet_list.pop(i)
                    increment_score(10)
                elif bullet[1] < 0:
                    bullet_list.pop(i)
                else:
                    bullet_list[i] = bullet

    # Move alien down
    alien_y_pos += alien_speed

    # Fire alien bullet
    if random.randint(0, 100) == 0:
        fire_alien_bullet()

    # Clear screen
    screen.fill(black)

    # Draw player
    screen.blit(player_image, (player_x_pos, player_y_pos))

    # Draw alien
    screen.blit(alien_image, (alien_x_pos, alien_y_pos))

    # Check for collision with bottom of screen
    if alien_y_pos > 450:
        alien_y_pos = 50
        alien_x_pos = random.randint(50, 650)
        increment_score(1)
        # Check for collision with player
    if alien_y_pos > 400 and alien_x_pos > player_x_pos and alien_x_pos < player_x_pos + 50:
        lives -= 1
        alien_x_pos = -50
        alien_y_pos = -50

    if lives <= 0:
        running = False
    score_text = font.render("Score: " + str(score) +
                             " Lives: " + str(lives), True, white)
    screen.blit(score_text, (20, 20))
    # Update display
    pygame.display.flip()

    # Wait
    pygame.time.wait(11)

# Stop Music
pygame.mixer.music.stop()

# Wait
pygame.time.wait(11)

# Quit pygame
pygame.quit()
