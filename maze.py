# Imports
import intersects
import math
import pygame
import random

# Initialize game engine
pygame.init()


# Window

scale = 25


WIDTH = 31
HEIGHT = 31 
SIZE = (WIDTH * scale, HEIGHT * scale)
TITLE = "Triwizard Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 80

# Colors
W = (255, 255, 255)
G = (160, 164, 165)
GD = (96, 96, 96)
B = (0, 0, 0)
BR = (91, 59, 0)
R = (198, 0, 0)
Y = (255, 208, 0)
S = (255, 246, 188)
LG = (156, 203, 79)
MG = (97, 144, 16)
DG = (48, 75, 7)
VDG = (37, 61, 25)
LB = (26, 189, 239)

F = None


'''maze = [[MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG],
        [ F, F, F, F, F, F, F, F, F, F, F, F,MG, F,MG, F,MG, F,MG, F, F, F, F, F, F, F, F, F, F, F,MG],
        [MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG, F,MG, F,MG, F,MG, F,MG,MG,MG,MG,MG, F,MG,MG,MG,MG,MG, F,MG],
        [MG, F,MG, F, F, F,MG, F, F, F,MG, F, F, F, F, F,MG, F,MG, F, F, F,MG, F, F, F, F, F,MG, F,MG],
        [MG, F,MG, F,MG, F,MG,MG,MG, F,MG,MG,MG,MG,MG, F,MG, F,MG, F,MG,MG,MG, F,MG,MG,MG,MG,MG,MG,MG],
        [MG, F,MG, F,MG, F, F, F,MG, F, F, F, F, F,MG, F,MG, F,MG, F,MG, F, F, F, F, F,MG, F, F, F,MG],
        [MG, F,MG, F,MG,MG,MG, F,MG, F,MG,MG,MG, F,MG, F,MG, F,MG, F,MG,MG,MG, F,MG, F,MG,MG,MG, F,MG],
        [MG, F,MG, F, F, F,MG, F,MG, F,MG, F, F, F, F, F, F, F, F, F,MG, F, F, F,MG, F,MG, F,MG, F,MG],
        [MG, F,MG, F,MG,MG,MG, F,MG,MG,MG,MG,MG,MG,MG,MG,MG, F,MG,MG,MG,MG,MG, F,MG,MG,MG, F,MG, F,MG],
        [MG, F, F, F,MG, F, F, F, F, F, F, F,MG, F, F, F,MG, F, F, F,MG, F, F, F,MG, F, F, F, F, F,MG],
        [MG,MG,MG,MG,MG, F,MG,MG,MG, F,MG, F,MG,MG,MG, F,MG,MG,MG, F,MG,MG,MG, F,MG, F,MG,MG,MG,MG,MG],
        [MG, F,MG, F, F, F,MG, F, F, F,MG, F, F, F, F, F,MG, F, F, F, F, F,MG, F,MG, F, F, F, F, F,MG],
        [MG, F,MG,MG,MG,MG,MG, F,MG, F,MG,MG,MG, F,MG,MG,MG,MG,MG,MG,MG, F,MG, F,MG,MG,MG, F,MG,MG,MG],
        [MG, F, F, F, F, F,MG, F,MG, F, F, F,MG, F,MG, F, F, F,MG, F, F, F,MG, F, F, F, F, F,MG, F,MG],
        [MG, F,MG,MG,MG, F,MG,MG,MG,MG,MG,MG,MG, F,MG,MG,MG, F,MG,MG,MG, F,MG,MG,MG,MG,MG, F,MG, F,MG],
        [MG, F,MG, F,MG, F, F, F,MG, F, F, F, F, F, F, F,MG, F, F, F, F, F, F, F, F, F,MG, F, F, F,MG],
        [MG,MG,MG, F,MG,MG,MG, F,MG, F,MG,MG,MG,MG,MG, F,MG,MG,MG, F,MG,MG,MG,MG,MG, F,MG, F,MG,MG,MG],
        [MG, F,MG, F, F, F,MG, F,MG, F, F, F,MG, F,MG, F,MG, F, F, F,MG, F, F, F, F, F, F, F,MG, F,MG],
        [MG, F,MG,MG,MG, F,MG, F,MG,MG,MG, F,MG, F,MG, F,MG, F,MG,MG,MG,MG,MG,MG,MG, F,MG,MG,MG, F,MG],
        [MG, F, F, F, F, F, F, F, F, F, F, F,MG, F,MG, F, F, F,MG, F,MG, F, F, F, F, F, F, F, F, F,MG],
        [MG, F,MG,MG,MG,MG,MG,MG,MG,MG,MG, F,MG, F,MG,MG,MG, F,MG, F,MG,MG,MG,MG,MG, F,MG,MG,MG, F,MG],
        [MG, F, F, F,MG, F, F, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F, F,MG, F, F, F,MG, F, F, F,MG],
        [MG, F,MG,MG,MG, F,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG, F,MG,MG,MG, F,MG, F,MG, F,MG],
        [MG, F, F, F,MG, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F, F,MG, F, F, F, F, F,MG, F,MG, F,MG],
        [MG,MG,MG,MG,MG,MG,MG,MG,MG, F,MG,MG,MG,MG,MG, F,MG, F,MG, F,MG,MG,MG,MG,MG, F,MG, F,MG, F,MG],
        [MG, F, F, F, F, F, F, F,MG, F, F, F,MG, F, F, F, F, F,MG, F,MG, F, F, F, F, F,MG, F,MG, F,MG],
        [MG, F,MG,MG,MG,MG,MG, F,MG,MG,MG, F,MG, F,MG,MG,MG,MG,MG, F,MG, F,MG,MG,MG, F,MG,MG,MG,MG,MG],
        [MG, F, F, F,MG, F,MG, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F, F, F, F,MG, F,MG, F, F, F,MG],
        [MG,MG,MG, F,MG, F,MG,MG,MG,MG,MG,MG,MG,MG,MG, F,MG,MG,MG,MG,MG,MG,MG, F,MG,MG,MG, F,MG,MG,MG],
        [MG, F, F, F, F, F,MG, F, F, F, F, F, F, F, F, F, F, F, F, F,MG, F, F, F, F, F, F, F, F, F, F],
        [MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG]]'''

maze = [[MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG],
        [MG, F, F, F, F, F, F, F, F, F, F, F, F, F, F,MG, F, F, F, F, F, F, F, F, F, F, F, F, F, F,MG],
        [MG, F, F, F, F, F, F, F, F, F, F, F, F, F, F,MG, F, F, F, F, F, F, F, F, F, F, F, F, F, F,MG],
        [MG, F, F,MG, F, F,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG, F, F,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG, F, F,MG],
        [MG, F, F,MG, F, F,MG, F, F, F, F, F, F, F, F,MG, F, F, F, F, F, F, F, F,MG, F, F,MG, F, F,MG],
        [MG, F, F,MG, F, F,MG, F, F, F, F, F, F, F, F,MG, F, F, F, F, F, F, F, F,MG, F, F,MG, F, F,MG],
        [MG, F, F,MG,MG,MG,MG, F, F,MG,MG,MG,MG, F, F,MG,MG,MG,MG,MG,MG,MG, F, F,MG, F, F,MG,MG,MG,MG],
        [MG, F, F, F, F, F,MG, F, F,MG, F, F, F, F, F, F, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F,MG],
        [MG, F, F, F, F, F,MG, F, F,MG, F, F, F, F, F, F, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F,MG],
        [MG,MG,MG,MG, F, F,MG, F, F,MG, F, F,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG, F, F,MG, F, F,MG],
        [MG, F, F, F, F, F,MG, F, F,MG, F, F, F, F, F, F, F, F, F, F, F, F, F, F,MG, F, F, F, F, F,MG],
        [MG, F, F, F, F, F,MG, F, F,MG, F, F, F, F, F, F, F, F, F, F, F, F, F, F,MG, F, F, F, F, F,MG],
        [MG, F, F,MG,MG,MG,MG, F, F,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG, F, F,MG, F, F,MG,MG,MG,MG, F, F,MG],
        [MG, F, F, F, F, F, F, F, F,MG, F, F,MG, F, F, F, F, F, F, F, F,MG, F, F,MG, F, F,MG, F, F,MG],
        [MG, F, F, F, F, F, F, F, F,MG, F, F,MG, F, F, F, F, F, F, F, F,MG, F, F,MG, F, F,MG, F, F,MG],
        [MG, F, F,MG,MG,MG,MG,MG,MG,MG, F, F,MG, F, F,MG,MG,MG,MG,MG,MG,MG, F, F,MG, F, F,MG, F, F,MG],
        [MG, F, F,MG, F, F, F, F, F, F, F, F,MG, F, F,MG, F, F, F, F, F,MG, F, F,MG, F, F,MG, F, F,MG],
        [MG, F, F,MG, F, F, F, F, F, F, F, F,MG, F, F,MG, F, F, F, F, F,MG, F, F,MG, F, F,MG, F, F,MG],
        [MG, F, F,MG, F, F,MG,MG,MG,MG, F, F,MG, F, F,MG,MG,MG,MG, F, F,MG, F, F,MG, F, F,MG, F, F,MG],
        [MG, F, F,MG, F, F,MG, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F, F, F, F, F, F, F,MG, F, F,MG],
        [MG, F, F,MG, F, F,MG, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F, F, F, F, F, F, F,MG, F, F,MG],
        [MG, F, F,MG,MG,MG,MG, F, F,MG, F, F,MG,MG,MG,MG, F, F,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG, F, F,MG],
        [MG, F, F, F, F, F,MG, F, F,MG, F, F,MG, F, F,MG, F, F, F, F, F, F, F, F, F, F, F, F, F, F,MG],
        [MG, F, F, F, F, F,MG, F, F,MG, F, F,MG, F, F,MG, F, F, F, F, F, F, F, F, F, F, F, F, F, F,MG],
        [MG,MG,MG,MG, F, F,MG, F, F,MG, F, F,MG, F, F,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG],
        [MG, F, F, F, F, F,MG, F, F,MG, F, F,MG, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F, F, F, F,MG],
        [MG, F, F, F, F, F,MG, F, F,MG, F, F,MG, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F, F, F, F,MG],
        [MG, F, F,MG,MG,MG,MG, F, F,MG, F, F,MG, F, F,MG, F, F,MG, F, F,MG, F, F,MG, F, F,MG, F, F,MG],
        [MG, F, F, F, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F, F],
        [MG, F, F, F, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F, F],
        [MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG]]


cup  = [[F, F, F, G, G, G, G, G, G, G, F, F, F],
        [ G, G, F, G,LB,LB,LB,LB,LB, G, F, G, G],
        [ G, F, G, G,LB,LB,LB,LB,LB, G, G, F, G],
        [ G, G, F, G,LB,LB,LB,LB,LB, G, F, G, G],
        [ F, F, G, G, G,LB,LB,LB, G, G, G, F, F],
        [ F, F, F, F, G, G,LB, G, G, F, F, F, F],
        [ F, F, F, F, F, G, G, G, F, F, F, F, F],
        [ F, F, F, F, F, F, G, F, F, F, F, F, F],
        [ F, F, F, F, F, F, G, F, F, F, F, F, F],
        [ F, F, F, F, F, F, G, F, F, F, F, F, F],
        [ F, F, F, F, F, G,LB, G, F, F, F, F, F],
        [ F, F, F, F, G,LB,LB,LB, G, F, F, F, F],
        [ F, F, F, G, G, G, G, G, G, G, F, F, F]]

harry = [[F, F, F, B, B, B, B, B, B, B, B, F, F, F, F, F],
         [F, F, B, B, B, B, B, B, B, B, B, B, F, F, F, F],
         [F, B, B, B, B, B, B, B, B, B, B, B, B, F, F, F],
         [F, B, B, B, B, S, S, S, S, S, B, B, B, F, F, F],
         [F, B, B, B, S,GD,GD, S, S,GD,GD, B, B, F, F, F],
         [F, B, B,GD,GD, W,DG,GD,GD, W,DG,GD, B, F, F, F],
         [F, S, S, S, S,GD,GD, S, S,GD,GD, S, S, F, F, F],
         [F, F, S, S, S, S, S, S, S, S, S, S, F, F, F, F],
         [F, F, F, S, S, S, S, S, S, S, S, F, F, F, F,BR],
         [F, F, B, R, Y, R, Y, R, Y, R, B, F, F, F, F,BR],
         [F, B, B, Y, Y, R, Y, R, Y, R, B, B, F, F, F,BR],
         [B, B, B, R, R, B, W, W, W, B, B, B, B, F, F,BR],
         [B, B, B, Y, Y, B, B, B, B, B, Y, B, B, B, B, S],
         [B, B, B, R, R, B, B, W, B, B, R, B, B, B, B,BR],
         [B, B, B, Y, Y, B, W, W, W, B, B, B, F, B, B, F],
         [S, S, B, B, B,GD,GD,GD,GD,GD, B, B, F, F, F, F],
         [F, F, B, B,GD,GD,GD, B,GD,GD,GD, B, F, F, F, F],
         [F, F, B, B,GD,GD, B, B, B,GD,GD, B, F, F, F, F],
         [F, F, B, B,GD,GD, F, F, F,GD,GD, B, F, F, F, F]]


# Make a player
player = [2, 1, 1.5, 1.5]
player_vx = 0
player_vy = 0
player_speed = .25

#make exit
end = [28, 28, 2, 2]

def draw_pixel(screen, color, a, b, pixel_size):
    pygame.draw.rect(screen, color, [a, b, pixel_size, pixel_size])


def draw_image(pixel_list, x, y, scale, pixel_size):

    a = x * scale
    b = y * scale
    
    for row in pixel_list:
        for color in row:
            if color != None:   
                draw_pixel(screen, color, a, b, pixel_size)
            a += pixel_size
        b += pixel_size
        a = x * scale
  
def spotlight(pixel_list, x, y, scale, pixel_size, x_center, y_center):
    
    radius = 3 * scale

    a = x * scale
    b = y * scale
    
    a_center = x_center * scale
    b_center = y_center * scale
    
    for row in pixel_list:
        for color in row:
            if color != None and abs(a - a_center) <= radius and abs(b - b_center) <= radius:   
                draw_pixel(screen, color, a, b, pixel_size)
            a += pixel_size
        b += pixel_size
        a = x * scale

# stages
START = 0
PLAYING = 1
END = 2

def setup():
    global player, stage, cups
    
    c_size = 2
    cup1 = [4, 19, c_size, c_size]
    cup2 = [28, 28, c_size, c_size]
    cup3 = [16, 16, c_size, c_size]
    cup4 = [28, 4, c_size, c_size]
    
    cups = [cup1, cup2, cup3, cup4]

    player = [2, 1, 1.5, 1.5]
    stage = START

font = pygame.font.Font(None, scale * 2)
# Game loop
setup()
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                  
            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()

                    
    if stage == PLAYING:        
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
    if stage == PLAYING:
        ''' move the player horizontally'''
        player[0] += player_vx
                
        '''resolve collisions horizontally'''
        for row_index, row in enumerate(maze):
            for col_index, color in enumerate(row):
                
                r = [col_index, row_index, 1, 1]
                
                if intersects.rect_rect(player, r) and color != F:
                    if player_vx > 0:
                        player[0] = r[0] - player[2]      
                    elif player_vx < 0:
                        player[0] = r[0] + r[2]
                            
        ''' move the player in vertical direction '''
        player[1] += player_vy
           
        ''' resolve collisions vertically'''
        for row_index, row in enumerate(maze):
            for col_index, color in enumerate(row):
                
                r = [col_index, row_index, 1, 1]
                
                if intersects.rect_rect(player, r) and color != F:
                    if player_vy > 0:
                        player[1] = r[1] - player[3]       
                    elif player_vy < 0:
                        player[1] = r[1] + r[3]
                              
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

        ''' get the cups '''        
        cups = [c for c in cups if not intersects.rect_rect(player, c)]
        if len(cups) == 0 and intersects.rect_rect(player, end):
            stage = END
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(VDG) 

    if stage == PLAYING:
        draw_image(harry, player[0], player[1], scale, 2)
        draw_image(maze, 0, 0, scale, scale)
        '''spotlight(maze, 0, 0, scale, scale, player[0], player[1])'''
       
        for c in cups:
            draw_image(cup, c[0], c[1], scale, 3)
            
    if stage == END:
        text1 = font.render("You Win!", True, Y)
        text2 = font.render("You Win!", True, Y)
        text_width1 = text1.get_width()
        text_height1 = text1.get_height()
        text_width2 = text2.get_width()
        text_height2 = text2.get_height()
        screen.blit(text1, [WIDTH * scale / 2 - (text_width1 / 2), HEIGHT * scale / 2 - (text_height1 / 2)])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
