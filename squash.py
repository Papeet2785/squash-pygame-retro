import os
import sys
import pygame
#script I cp pasted from gpt for better path thingy idk bruh
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)

#fun variables to edit :)
screen_x = 1024
screen_y = 768
velocity_x_init = -1000
velocity_y_init = 0
ball_size = 30
paddle_size_x = 18
paddle_size_y = 80
fps = 60
paddle_movement = 1000
paddle_bounce = 400


#window init + decorations
pygame.init()
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Squash")
icon = pygame.image.load(resource_path('Assets/icon.ico'))
pygame.display.set_icon(icon)

#Sprites
#floor
floor = pygame.image.load(resource_path('Assets/floor.png'))
floor = pygame.transform.scale(floor, (screen_x, screen_y))

#ball
ball = pygame.image.load(resource_path(('Assets/ball.png'))).convert_alpha()
ball = pygame.transform.scale(ball, (ball_size,ball_size))
ball_x = screen_x/2
ball_y =screen_y/2

#human paddle
paddle = pygame.image.load(resource_path(('Assets/paddle.png'))).convert_alpha()
paddle = pygame.transform.scale(paddle, (paddle_size_x, paddle_size_y))
paddle_x = 5
paddle_y = ((screen_y/2) - (paddle_size_y/2))

#game over
game_over = pygame.image.load(resource_path(('Assets/gameover.png'))).convert_alpha()
game_over = pygame.transform.scale(game_over, (screen_x, screen_y))

#restart message, cp pasted gemini
font = pygame.font.Font(None, 48)
res_surface = font.render("Press r to restart!", True, 'black')
res_rect = res_surface.get_rect(center=(screen_x // 2, screen_y // 4))

#speed variables init
ball_x_vel = velocity_x_init
ball_y_vel = velocity_y_init

#screen stuff I copy/pasted
clock = pygame.time.Clock()
delta_time = 0.1
running = True
while running:
    #spawning stuff
    screen.blit(floor, (0,0))
    screen.blit(ball, (ball_x,ball_y))
    if ball_x < 0:
        screen.blit(game_over, (0,0))
        screen.blit(res_surface, res_rect)
    else:
        screen.blit(paddle, (paddle_x,paddle_y))
        
    #hitboxes
    b_hbox = pygame.Rect(ball_x, ball_y, ball_size, ball_size)
    #elite paddle
    p1_hbox_top = pygame.Rect(paddle_x, paddle_y, paddle_size_x, paddle_size_y/3)
    p1_hbox_mid = pygame.Rect(paddle_x, paddle_y + paddle_size_y/3, paddle_size_x, paddle_size_y/3)
    p1_hbox_bot = pygame.Rect(paddle_x, paddle_y + paddle_size_y * 2/3, paddle_size_x, paddle_size_y/3)

    #ball vx
    #paddle collisions
    if b_hbox.colliderect(p1_hbox_mid) or b_hbox.colliderect(p1_hbox_top) or b_hbox.colliderect(p1_hbox_bot):
        ball_x_vel *= -1
    #wall collisions
    if ball_x > screen_x - ball_size:
        ball_x = screen_x - ball_size
        ball_x_vel *= -1
    ball_x += ball_x_vel * delta_time

    #ball vy
    #paddle collisions
    if b_hbox.colliderect(p1_hbox_top):
        ball_y_vel -= paddle_bounce
    if b_hbox.colliderect(p1_hbox_bot):
        ball_y_vel += paddle_bounce
    #wall collisions
    if ball_y < 0:
        ball_y = 0
        ball_y_vel *= -1
    if ball_y > screen_y - ball_size:
        ball_y = screen_y - ball_size
        ball_y_vel *= -1  
    ball_y += ball_y_vel * delta_time

    #keys
    keys = pygame.key.get_pressed()
    #up
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and paddle_y>10:
        paddle_y -= paddle_movement*delta_time
    #down
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and paddle_y<(screen_y - paddle_size_y):
        paddle_y += paddle_movement*delta_time
    #restart
    if (keys[pygame.K_r]):
        paddle_y = ((screen_y/2) - (paddle_size_y/2))
        ball_x_vel = velocity_x_init
        ball_y_vel = velocity_y_init
        ball_x = screen_x/2
        ball_y = screen_y/2

    #stuff I cp pasted from youtube for better window/fps stuff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    delta_time = clock.tick(fps) / 1000
    delta_time = max(0.001, min(0.1, delta_time))
    clock.tick(fps)
pygame.quit()
