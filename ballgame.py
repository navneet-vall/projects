import pygame

#main_window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("This is a simple game with no objective. Have fun.")
font = pygame.font.SysFont("Arial", 20)


#ball_specs
ball_radius = 20
ball_pos = [WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2]
ball_color = (0, 0, 0)

#environment
environment_color = (255 ,255, 0)
environment_rect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

#parameters
time_step = 0.01  #seconds
ball_speed = 300  #pix per second
ball_velocity = [0, 0]

#main_game
running = True
while running:
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball_velocity[0] = -ball_speed
            elif event.key == pygame.K_RIGHT:
                ball_velocity[0] = ball_speed
            elif event.key == pygame.K_UP:
                ball_velocity[1] = -ball_speed
            elif event.key == pygame.K_DOWN:
                ball_velocity[1] = ball_speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ball_velocity[0] = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ball_velocity[1] = 0

    #ball_position
    ball_pos[0] += ball_velocity[0] * time_step
    ball_pos[1] += ball_velocity[1] * time_step

    #collisions_boundaries
    if not environment_rect.contains(pygame.Rect(ball_pos[0] - ball_radius, ball_pos[1] - ball_radius, ball_radius * 2, ball_radius * 2)):
        ball_pos[0] = min(max(ball_pos[0], ball_radius), WINDOW_WIDTH - ball_radius)
        ball_pos[1] = min(max(ball_pos[1], ball_radius), WINDOW_HEIGHT - ball_radius)

    #main_environment
    screen.fill(environment_color)
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
    pygame.display.flip()


    #speed_control
    pygame.time.wait(int(time_step * 1000))

#exit
pygame.quit()
