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
GL = (219, 219, 219)
G = (160, 164, 165)
GD = (96, 96, 96)
B = (0, 0, 0)
BR = (91, 59, 0)
R = (198, 0, 0)
Y = (255, 208, 0)
S = (255, 246, 188)
LH = (254, 255, 204)
LG = (156, 203, 79)
MG = (97, 144, 16)
DG = (48, 75, 7)
SG = (10, 99, 2)
VDG = (37, 61, 25)
CF = (26, 189, 239)

F = None


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
        [MG, F, F, F, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F,MG],
        [MG, F, F, F, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F, F, F, F,MG, F, F,MG],
        [MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG]]


cup  = [[ F, F, F, G, G, G, G, G, G, G, F, F, F],
        [ G, G, F, G,CF,CF,CF,CF,CF, G, F, G, G],
        [ G, F, G, G,CF,CF,CF,CF,CF, G, G, F, G],
        [ G, G, F, G,CF,CF,CF,CF,CF, G, F, G, G],
        [ F, F, G, G, G,CF,CF,CF, G, G, G, F, F],
        [ F, F, F, F, G, G,CF, G, G, F, F, F, F],
        [ F, F, F, F, F, G, G, G, F, F, F, F, F],
        [ F, F, F, F, F, F, G, F, F, F, F, F, F],
        [ F, F, F, F, F, F, G, F, F, F, F, F, F],
        [ F, F, F, F, F, F, G, F, F, F, F, F, F],
        [ F, F, F, F, F, G,CF, G, F, F, F, F, F],
        [ F, F, F, F, G,CF,CF,CF, G, F, F, F, F],
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

draco = [[F, F, F,LH,LH,LH,LH,LH,LH,LH,LH, F, F, F, F, F],
         [F, F,LH,LH,LH,LH,LH,LH,LH,LH,LH,LH, F, F, F, F],
         [F,LH,LH,LH,LH,LH,LH,LH,LH,LH,LH,LH,LH, F, F, F],
         [F,LH,LH,LH,LH, S, S, S, S, S,LH,LH,LH, F, F, F],
         [F,LH,LH,LH, S, S, S, S, S, S, S,LH,LH, F, F, F],
         [F,LH,LH, S, S, W,GD, S, S, W,GD, S,LH, F, F, F],
         [F, S, S, S, S, S, S, S, S, S, S, S, S, F, F, F],
         [F, F, S, S, S, S, S, S, S, S, S, S, F, F, F, F],
         [F, F, F, S, S, S, S, S, S, S, S, F, F, F, F,BR],
         [F, F, B,SG,GL,SG,GL,SG,GL,SG, B, F, F, F, F,BR],
         [F, B, B,GL,GL,SG,GL,SG,GL,SG, B, B, F, F, F,BR],
         [B, B, B,SG,SG, B, W, W, W, B, B, B, B, F, F,BR],
         [B, B, B,GL,GL, B, B, B, B, B,GL, B, B, B, B, S],
         [B, B, B,SG,SG, B, B, W, B, B,SG, B, B, B, B,BR],
         [B, B, B,GL,GL, B, W, W, W, B, B, B, F, B, B, F],
         [S, S, B, B, B,GD,GD,GD,GD,GD, B, B, F, F, F, F],
         [F, F, B, B,GD,GD,GD, B,GD,GD,GD, B, F, F, F, F],
         [F, F, B, B,GD,GD, B, B, B,GD,GD, B, F, F, F, F],
         [F, F, B, B,GD,GD, F, F, F,GD,GD, B, F, F, F, F]]


# Make a player
player1_size = 2
player1 = [1, 1, 1.5, 1.5]
player1_vx = 0
player1_vy = 0
player1_speed = .20

player2_size = 1
player2 = [0, 0, .75, .75]
player2_vx = 0
player2_vy = 0
player2_speed = .20


# Make cups
def initialize_cups():
    c_size = 2
    cup1 = [4, 19, c_size, c_size]
    cup2 = [28, 28, c_size, c_size]
    cup3 = [16, 16, c_size, c_size]
    cup4 = [28, 4, c_size, c_size]
    
    return [cup1, cup2, cup3, cup4]
    

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
    
    radius = 5 * scale

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

def zap(player2, cups, c_size, maze):
    
    player2_reach = [player2[0] - player2[2], player2[1] - player2[3], player2[2] * 3, player2[3] * 3]
    
    finished = False
    
    while finished == False:
        new_x = random.randint(1, 30)
        new_y = random.randint(1, 30)
        print("have ints")
        if maze[new_y][new_x] == F:
            finished = True
        else:
            finished = False    
    print("ints:" + str(new_x) + str(new_y))
        
    print(player2_reach)
    for c in cups:
        print(c)
        if intersects.rect_rect(player2_reach, c):
            print("Old: " + str(c[0]) + str(c[1]))
            c = [new_x, new_y, c_size, c_size]
            print("New: " + str(c[0]) + str(c[1]))
    print cups
    
    '''ints exist, program does not change original cups, just makes a copy.'''
    
    return [c for c in cups]
    print("zap!")

cups = []
cups = initialize_cups()

  
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

    up1 = pressed[pygame.K_UP]
    down1 = pressed[pygame.K_DOWN]
    left1 = pressed[pygame.K_LEFT]
    right1 = pressed[pygame.K_RIGHT]
    
    up2 = pressed[pygame.K_w]
    down2 = pressed[pygame.K_s]
    left2 = pressed[pygame.K_a]
    right2 = pressed[pygame.K_d]
    
    reset = pressed[pygame.K_r]
    attempt = pressed[pygame.K_z]
    
    if up1:
        player1_vy = -player1_speed
    elif down1:
        player1_vy = player1_speed
    else:
        player1_vy = 0       
    if left1:
        player1_vx = -player1_speed
    elif right1:
        player1_vx = player1_speed
    else:
        player1_vx = 0

    if up2:
        player2_vy = -player2_speed
    elif down2:
        player2_vy = player2_speed
    else:
        player2_vy = 0       
    if left2:
        player2_vx = -player2_speed
    elif right2:
        player2_vx = player2_speed
    else:
        player2_vx = 0


    if reset:
        cups = initialize_cups()
        win = False
    
    if attempt:
        print("ZAP")
        cups = zap(player2, cups, 1, maze)
        print "back from zap"
        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player horizontally'''
    player1[0] += player1_vx
    player2[0] += player2_vx

            
    '''resolve collisions horizontally'''
    for row_index, row in enumerate(maze):
        for col_index, color in enumerate(row):
            
            r = [col_index, row_index, 1, 1]
            
            if intersects.rect_rect(player1, r) and color != F:
                if player1_vx > 0:
                    player1[0] = r[0] - player1[2]           
                elif player1_vx < 0:
                    player1[0] = r[0] + r[2]
                    
            if intersects.rect_rect(player2, r) and color != MG:
                if player2_vx > 0:
                    player2[0] = r[0] - player2[2]              
                elif player2_vx < 0:
                    player2[0] = r[0] + r[2]
                    
    ''' move the player in vertical direction '''
    player1[1] += player1_vy
    player2[1] += player2_vy

    
    ''' resolve collisions vertically'''
    for row_index, row in enumerate(maze):
        for col_index, color in enumerate(row):
            
            r = [col_index, row_index, 1, 1]
            
            if intersects.rect_rect(player1, r) and color != F:
                if player1_vy > 0:
                    player1[1] = r[1] - player1[3]            
                elif player1_vy < 0:
                    player1[1] = r[1] + r[3]
                    
            if intersects.rect_rect(player2, r) and color != MG:
                if player2_vy > 0:
                    player2[1] = r[1] - player2[3]              
                elif player2_vy < 0:
                    player2[1] = r[1] + r[3]
                       
               
    ''' here is where you should resolve player collisions with screen edges '''
    top1 = player1[1]
    bottom1 = player1[1] + player1[3]
    left1 = player1[0]
    right1 = player1[0] + player1[2]
    if left1 < 0:
        player1[0] = 0
    elif right1 > WIDTH:
        player1[0] = WIDTH - player1[2]
    if top1 < 0:
        player1[1] = 0
    elif bottom1 > HEIGHT:
        player1[1] = HEIGHT - player1[3]

    top2 = player2[1]
    bottom2 = player2[1] + player2[3]
    left2 = player2[0]
    right2 = player2[0] + player2[2]
    if left2 < 0:
        player2[0] = 0
    elif right2 > WIDTH:
        player2[0] = WIDTH - player2[2]
    if top2 < 0:
        player2[1] = 0
    elif bottom2 > HEIGHT:
        player2[1] = HEIGHT - player2[3]

    ''' get the cups '''
    cups = [c for c in cups if not intersects.rect_rect(player1, c)]


    if len(cups) == 0:
        win = True

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(VDG)

    
    draw_image(harry, player1[0], player1[1], scale, player1_size)
  
    draw_image(maze, 0, 0, scale, scale)
    #spotlight(maze, 0, 0, scale, scale, player1[0], player1[1])
   
    draw_image(draco, player2[0], player2[1], scale, player2_size)

    for c in cups:
        draw_image(cup, c[0], c[1], scale, 3)
    
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
