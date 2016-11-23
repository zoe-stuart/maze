# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
scale = 15

WIDTH = 50 
HEIGHT = 37 
SIZE = (WIDTH * scale, HEIGHT * scale)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
LG = (156, 203, 79)
MG = (97, 144, 16)
DG = (48, 75, 7)
VDG = (37, 61, 25)


# Make a player
player =  [1, 1, 1, 1]
player_vx = 0
player_vy = 0
player_speed = .25

# make walls
wall1 =  [0, 2, 8, 1]
wall2 =  [11, 2, 16, 1]
wall3 =  [8, 2, 8, 1]
wall4 =  [11, 2, 1, 8]
wall5 =  [0, 37, 48, 1]
wall6 =  [2, 9, 7, 1]
wall7 =  [29, 2, 8, 1]
wall8 =  [0, 12, 18, 1]
wall9 =  [2, 5, 4, 1]
wall10 = [2, 5, 1, 4]

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10]



# Make coins
coin1 = [12, 20, .5, .5]
coin2 = [16, 8, .5, .5]
coin3 = [6, 6, .5, .5]

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
    top = player[1]
    bottom = player[1] + player[3]
    left = player[0]
    right = player[0] + player[2]


   
    if left < 0:
        player[0] = 0
    elif right >= WIDTH:
        player[0] = WIDTH - player[2]

    if top < 0:
        player[1] = 0
    elif bottom >= HEIGHT:
        player[1] = HEIGHT - player[3]



    ''' get the coins '''
    coins = [c for c in coins if not intersects.rect_rect(player, c)]

    if len(coins) == 0:
        win = True

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(VDG)

    pygame.draw.rect(screen, WHITE, (player[0] * scale, player[1] * scale, player[2] * scale, player[3] * scale))
    
    for w in walls:
        pygame.draw.rect(screen, LG, (w[0] * scale, w[1] * scale, w[2] * scale, w[3] * scale))

    for c in coins:
        pygame.draw.rect(screen, YELLOW, (c[0] * scale, c[1] * scale, c[2] * scale, c[3] * scale))
        
    if win:
        font = pygame.font.Font(None, scale * 2)
        text = font.render("You Win!", 1, YELLOW)
        text_width = text.get_width()
        text_height = text.get_height()
        screen.blit(text, [WIDTH * scale / 2 - (text_width / 2), HEIGHT * scale / 2 - (text_height / 2)])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
