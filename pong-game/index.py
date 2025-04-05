import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Ball properties
ball = pygame.Rect(WIDTH//2, HEIGHT//2, 20, 20)
ball_dx, ball_dy = 5, 5

# Paddle properties
paddle1 = pygame.Rect(30, HEIGHT//2 - 60, 10, 120)
paddle2 = pygame.Rect(WIDTH-40, HEIGHT//2 - 60, 10, 120)
paddle_speed = 10

def move_paddles(keys):
    if keys[pygame.K_w] and paddle1.y > 0: paddle1.y -= paddle_speed
    if keys[pygame.K_s] and paddle1.y < HEIGHT - 120: paddle1.y += paddle_speed
    if keys[pygame.K_UP] and paddle2.y > 0: paddle2.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2.y < HEIGHT - 120: paddle2.y += paddle_speed

running = True
while running:
    clock.tick(60)
    win.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    move_paddles(keys)

    # Ball Movement
    ball.x += ball_dx
    ball.y += ball_dy

    if ball.y <= 0 or ball.y >= HEIGHT - 20: ball_dy *= -1
    if ball.colliderect(paddle1) or ball.colliderect(paddle2): ball_dx *= -1

    pygame.draw.rect(win, (255, 255, 255), paddle1)
    pygame.draw.rect(win, (255, 255, 255), paddle2)
    pygame.draw.ellipse(win, (255, 255, 255), ball)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
