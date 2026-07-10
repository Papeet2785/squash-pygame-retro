import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))

#Sprites
#floor
floor = pygame.image.load('Assets/floor.png')
floor = pygame.transform.scale(floor, (600, 600))

#ball
ball = pygame.image.load('Assets/ball.png').convert_alpha()
ball = pygame.transform.scale(ball, (25,25))
x_ball = 300
y_ball =300

#human paddle
paddle1 = pygame.image.load('Assets/paddle.png').convert_alpha()
x_paddle1 = 5
y_paddle1 = 280

#game over
game_over = pygame.image.load('Assets/gameover.png').convert_alpha()
game_over = pygame.transform.scale(game_over, (600, 600))

#initializing velocity
x_ball_vel = -1000
y_ball_vel = 0

#screen stuff I copy/pasted
clock = pygame.time.Clock()
delta_time = 0.1
running = True
while running:
    #spawning stuff
    screen.blit(floor, (0,0))
    screen.blit(ball, (x_ball,y_ball))
    if x_ball < 0:
        screen.blit(game_over, (0,0))
    else:
        screen.blit(paddle1, (x_paddle1,y_paddle1))
        
    #hitboxes
    b_hbox = pygame.Rect(x_ball, y_ball, ball.get_width(), ball.get_height())
    #elite paddle hitboxes
    p1_hbox_top = pygame.Rect(x_paddle1, y_paddle1, paddle1.get_width(), 20)
    p1_hbox_mid = pygame.Rect(x_paddle1, y_paddle1+20, paddle1.get_width(), paddle1.get_height()-20)
    p1_hbox_bot = pygame.Rect(x_paddle1, y_paddle1 + paddle1.get_height() -20, paddle1.get_width(), 20)
    #screen edge hitboxes
    wall_top = pygame.Rect(0, -20, 600, 20)
    wall_bot = pygame.Rect(0, 600, 600, 20)
    wall_right = pygame.Rect(600, 0, 20, 600)

    #ball vx
    if b_hbox.colliderect(p1_hbox_mid) or b_hbox.colliderect(p1_hbox_top) or b_hbox.colliderect(p1_hbox_bot) or b_hbox.colliderect(wall_right):
        x_ball_vel *= -1
    x_ball += x_ball_vel * delta_time

    #ball vy
    if b_hbox.colliderect(wall_top) or b_hbox.colliderect(wall_bot):
        y_ball_vel *= -1
    if b_hbox.colliderect(p1_hbox_top):
        y_ball_vel -= 300
    if b_hbox.colliderect(p1_hbox_bot):
        y_ball_vel += 300    
    y_ball += y_ball_vel * delta_time

    #keys
    keys = pygame.key.get_pressed()
    #up
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and y_paddle1>10:
        y_paddle1 -= 800*delta_time
    #down
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and y_paddle1<520:
        y_paddle1 += 800*delta_time
    
    #display stuff I copy/pasted
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    delta_time = clock.tick(60) / 1000
    delta_time = max(0.001, min(0.1, delta_time))
    clock.tick(60)
pygame.quit()
