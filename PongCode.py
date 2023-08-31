#Remember to install the python library 'pygame' for this to work
import pygame
import random

# Initialize Pygame
pygame.init()

# Game settings
width, height = 800, 600
ball_speed = [5, 5]
paddle_speed = 5

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Create the display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Create the paddles and ball
player_paddle = pygame.Rect(50, height // 2 - 50, 10, 100)
opponent_paddle = pygame.Rect(width - 60, height // 2 - 50, 10, 100)
ball = pygame.Rect(width // 2 - 15, height // 2 - 15, 30, 30)

# Set initial ball direction
ball_direction = [random.choice([-1, 1]), random.choice([-1, 1])]

# Initialize scores
player_score = 0
opponent_score = 0

# Load font
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and player_paddle.bottom < height:
        player_paddle.top += paddle_speed
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.top -= paddle_speed

    # AI logic for opponent's paddle
    if opponent_paddle.centery < ball.centery:
        opponent_paddle.y += paddle_speed
    elif opponent_paddle.centery > ball.centery:
        opponent_paddle.y -= paddle_speed

    # Update ball position
    ball.x += ball_speed[0] * ball_direction[0]
    ball.y += ball_speed[1] * ball_direction[1]

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= height:
        ball_direction[1] *= -1

    # Ball collision with paddles
    if ball.colliderect(player_paddle):
        ball_direction[0] = abs(ball_direction[0])  # Change x-direction
    elif ball.colliderect(opponent_paddle):
        ball_direction[0] = -abs(ball_direction[0])  # Change x-direction

    # Reset ball position and update scores
    if ball.left <= 0:
        ball_direction[0] *= -1
        ball.x = width // 2 - ball.width // 2
        ball.y = height // 2 - ball.height // 2
        opponent_score += 1
    elif ball.right >= width:
        ball_direction[0] *= -1
        ball.x = width // 2 - ball.width // 2
        ball.y = height // 2 - ball.height // 2
        player_score += 1

    # Draw everything
    screen.fill(black)
    pygame.draw.rect(screen, white, player_paddle)
    pygame.draw.rect(screen, white, opponent_paddle)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (width // 2, 0), (width // 2, height))

    # Draw scores
    player_text = font.render(f"Player: {player_score}", True, white)
    opponent_text = font.render(f"Opponent: {opponent_score}", True, white)
    screen.blit(player_text, (20, 20))
    screen.blit(opponent_text, (width - opponent_text.get_width() - 20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

