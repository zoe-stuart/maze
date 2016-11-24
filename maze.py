# Imports
import intersects
import math
import pygame
import random

# Initialize game engine
pygame.init()


# Window

scale = 16

WIDTH = 51 
HEIGHT = 36 
SIZE = (WIDTH * scale, HEIGHT * scale)
TITLE = "Triwizard Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 80

# Colors
T = (255, 255, 255)
B = (0, 0, 0)
Y = (255, 255, 0)
LG = (156, 203, 79)
MG = (97, 144, 16)
DG = (48, 75, 7)
VDG = (37, 61, 25)

F = None


maze = [[F, F, F, F, F, F, F, F, F],
        [T, T, T, F, T, T, T, T, T],
        [T, F, F, F, F, F, F, F, T],
        [T, T, T, T, T, T, T, F, F]]



# Make a player
player =  [10, 10, .5, .5]
player_vx = 0
player_vy = 0
player_speed = .25

# Make coins
coin1 = [25, 19, 2, 2]
coin2 = [3, 6, 2, 2]
coin3 = [39, 3, 2, 2]
coin4 = [32, 3, 2, 2]

coins = [coin1, coin2, coin3, coin4]


def draw_pixel(screen, color, a, b, scale):
    pygame.draw.rect(screen, color, [a, b, scale, scale])


def draw_image(pixel_list, x, y, scale):

    a = x * scale
    b = y * scale
    
    for row in pixel_list:
        for color in row:
            if color != None:   
                draw_pixel(screen, color, a, b, scale)
            a += scale
        b += scale
        a = x * scale
        
def debug(msg):
    font = pygame.font.Font(None, scale * 2)
    text = font.render(msg, 1, Y)
    text_width = text.get_width()
    text_height = text.get_height()
    screen.blit(text, [WIDTH*scale - text_width, HEIGHT*scale - text_height])
        
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

        
    # debug message:
    message = ""
    
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player horizontally'''
    player[0] += player_vx

            
    '''resolve collisions horizontally'''
    for row_index, row in enumerate(maze):
        for col_index, color in enumerate(row):
            
            r = [col_index, row_index, 1, 1]
            
            if intersects.rect_rect(player, r) and color == T:
                if player_vx > 0:
                    player[0] = r[0] - player[2]
                    message = "OUCH! " + str(r[0]) + " " + str(r[1])
                elif player_vx < 0:
                    player[0] = r[0] + r[2]
                    message = "OUCH! " + str(r[0]) + " " + str(r[1])
               
             
    ''' move the player in vertical direction '''
    player[1] += player_vy
    
    
    ''' resolve collisions vertically'''
    for row_index, row in enumerate(maze):
        for col_index, color in enumerate(row):
            
            r = [col_index, row_index, 1, 1]
            
            if intersects.rect_rect(player, r) and color == T:
                if player_vy > 0:
                    player[1] = r[1] - player[3]
                    message = "OUCH! " + str(r[0]) + " " + str(r[1])
                elif player_vy < 0:
                    player[1] = r[1] + r[3]
                    message = "OUCH! " + str(r[0]) + " " + str(r[1])
               
               
               
    ''' here is where you should resolve player collisions with screen edges '''
    top = player[1]
    bottom = player[1] + player[3]
    left = player[0]
    right = player[0] + player[2]


   
    if left < 0:
        player[0] = 0
    elif right > WIDTH:
        player[0] = WIDTH - player[2]

    if top < 0:
        player[1] = 0
    elif bottom > HEIGHT:
        player[1] = HEIGHT - player[3]



    ''' get the coins '''
    coins = [c for c in coins if not intersects.rect_rect(player, c)]

    if len(coins) == 0:
        win = True

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(VDG)

    debug(message)

    pygame.draw.rect(screen, Y, (player[0] * scale, player[1] * scale, player[2] * scale, player[3] * scale))
    
    font = pygame.font.Font(None, scale * 2)
    text = font.render("("+str(player[0])+","+str(player[1])+")", 1, Y)
    text_width = text.get_width()
    text_height = text.get_height()
    screen.blit(text, [WIDTH * scale / 2 - (text_width / 2), HEIGHT * scale / 2 - (text_height / 2)])
    
    draw_image(maze, 0, 0, scale)
   
    for c in coins:
        pygame.draw.rect(screen, Y, (c[0] * scale, c[1] * scale, c[2] * scale, c[3] * scale))
      
      
      
      
      
      
      
      
      
      
        
    if win:
        font = pygame.font.Font(None, scale * 2)
        text = font.render("You Win!", 1, Y)
        text_width = text.get_width()
        text_height = text.get_height()
        screen.blit(text, [WIDTH * scale / 2 - (text_width / 2), HEIGHT * scale / 2 - (text_height / 2)])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
