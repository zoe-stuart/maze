# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)


# Make a player
player =  [200, 150, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 5

# make walls
wall1 =  [300, 275, 200, 25]
wall2 =  [400, 450, 200, 25]
wall3 =  [100, 100, 25, 200]

walls = [wall1, wall2, wall3]

# Make coins
coin1 = [300, 500, 25, 25]
coin2 = [400, 200, 25, 25]
coin3 = [150, 150, 25, 25]

coins = [coin1, coin2, coin3]


# Game loop
win = False
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    if up:
        player_vy = -player_speed
    elif down:
        player_vy = player_speed
    else:
        player_vy = 0
        
    if left:
        player_vx = -player_speed
    elif right:
        player_vx = player_speed
    else:
        player_vx = 0

        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player[0] += player_vx

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player, w):        
            if player_vx > 0:
                player[0] = w[0] - player[2]
            elif player_vx < 0:
                player[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player[1] += player_vy
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player, w):                    
            if player_vy > 0:
                player[1] = w[1] - player[3]
            if player_vy < 0:
                player[1] = w[1] + w[3]


    ''' here is where you should resolve player collisions with screen edges '''





    ''' get the coins '''
    coins = [c for c in coins if not intersects.rect_rect(player, c)]

    if len(coins) == 0:
        win = True

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player)
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)
        
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, GREEN)
        screen.blit(text, [400, 200])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
