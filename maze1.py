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
wall1 =  [0, 2, 11, 1]
wall2 =  [13, 2, 1, 7]
wall3 =  [13, 2, 29, 1]
wall4 =  [10, 2, 1, 7]
wall5 =  [16, 12, 1, 19]
wall6 =  [2, 8, 9, 1]
wall7 =  [34, 2, 1, 9]
wall8 =  [0, 11, 45, 1]
wall9 =  [2, 5, 5, 1]
wall10 = [2, 5, 1, 3]
wall11 = [0, 37, 46, 1]
wall12 = [16, 5, 18, 1]
wall13 = [13, 8, 18, 1]
wall14 = [44, 2, 4, 1]
wall15 = [44, 2, 1, 7]
wall16 = [47, 2, 1, 21]
wall17 = [37, 5, 4, 1]
wall18 = [34, 8, 10, 1]
wall19 = [41, 2, 1, 4]
wall20 = [19, 14, 25, 1]
wall21 = [19, 14, 1, 14]
wall22 = [5, 31, 40, 1]
wall23 = [2, 34, 48, 1]
wall24 = [47, 25, 1, 9]
wall25 = [44, 14, 1, 11]
wall26 = [44, 25, 4, 1]
wall27 = [19, 28, 8, 1]
wall28 = [29, 28, 16, 1]
wall29 = [41, 17, 1, 9]
wall30 = [29, 22, 1, 7]
wall31 = [22, 25, 8, 1]
wall32 = [22, 22, 8, 1]
wall33 = [22, 17, 1, 5]
wall34 = [22, 17, 11, 1]
wall35 = [32, 18, 1, 8]
wall36 = [35, 15, 1, 14]
wall37 = [38, 17, 1, 9]
wall38 = [2, 14, 1, 20]
wall39 = [2, 14, 8, 1]
wall40 = [10, 14, 1, 15]
wall41 = [5, 17, 1, 15]
wall42 = [10, 28, 3, 1]
wall43 = [13, 14, 1, 15]
wall44 = [5, 17, 3, 1]
wall45 = [5, 20, 3, 1]
wall46 = [5, 23, 3, 1]
wall47 = [5, 26, 3, 1]

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20, wall21, wall22, wall23, wall24, wall25, wall26, wall27, wall28, wall29, wall30, wall31, wall32, wall33, wall34, wall35, wall36, wall37, wall38, wall39, wall40, wall41, wall42, wall43, wall44, wall45, wall46, wall47]



# Make coins
coin1 = [25, 19, 2, 2]
coin2 = [3, 6, 2, 2]
coin3 = [39, 3, 2, 2]
coin4 = [32, 3, 2, 2]

coins = [coin1, coin2, coin3, coin4]


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
