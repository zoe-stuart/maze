# Imports
import intersects
import math
import pygame
import random

# Initialize game engine
pygame.init()


# Window
scale = 30

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
DR = (100, 0, 0)
O = (255, 148, 0)
Y = (255, 208, 0)
S = (232, 193, 139)
LG = (156, 203, 79)
MG = (97, 144, 16)
DG = (48, 75, 7)
VDG = (37, 61, 25)
LB = (26, 189, 239)
BL = (147, 188, 255)

F = None

maze = [[MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG,MG],
        [ F, F, F, F, F, F, F, F, F, F, F, F, F, F, F,MG, F, F, F, F, F, F, F, F, F, F, F, F, F, F,MG],
        [ F, F, F, F, F, F, F, F, F, F, F, F, F, F, F,MG, F, F, F, F, F, F, F, F, F, F, F, F, F, F,MG],
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

cup  =  [[F, F, F, G, G, G, G, G, G, G, F, F, F],
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

cedric =[[F, F, F,BR,BR,BR,BR,BR,BR,BR,BR, F, F, F, F, F],
         [F, F,BR,BR,BR,BR,BR,BR,BR,BR,BR,BR, F, F, F, F],
         [F,BR,BR,BR,BR,BR,BR,BR,BR,BR,BR,BR,BR, F, F, F],
         [F,BR,BR,BR,BR,BR,BR,BR,BR,BR,BR,BR,BR, F, F, F],
         [F,BR,BR,BR,BR, S, S, S, S, S,BR,BR,BR, F, F, F],
         [F,BR, S,BR, S, W, B, S, S, W, B, S,BR, F, F, F],
         [F,BR,BR, S, S, S, S, S, S, S, S, S,BR, F, F, F],
         [F, F, S, S, S, S, S, S, S, S, S, S, F, F, F, F],
         [F, F, F, S, S, S, S, S, S, S, S, F, F, F, F,BR],
         [F, F, B, G, Y, G, Y, G, Y, G, B, F, F, F, F,BR],
         [F, B, B, Y, Y, G, Y, G, Y, G, B, B, F, F, F,BR],
         [B, B, B, G, G, B, W, W, W, B, B, B, B, F, F,BR],
         [B, B, B, Y, Y, B, B, B, B, B, Y, B, B, B, B, S],
         [B, B, B, G, G, B, B, W, B, B, G, B, B, B, B,BR],
         [B, B, B, Y, Y, B, W, W, W, B, B, B, F, B, B, F],
         [S, S, B, B, B,GD,GD,GD,GD,GD, B, B, F, F, F, F],
         [F, F, B, B,GD,GD,GD, B,GD,GD,GD, B, F, F, F, F],
         [F, F, B, B,GD,GD, B, B, B,GD,GD, B, F, F, F, F],
         [F, F, B, B,GD,GD, F, F, F,GD,GD, B, F, F, F, F]]

krum =   [[F, F, F, B, B, B, B, B, B, B, B, F, F, F, F, F],
         [F, F, B, B, B, B, B, B, B, B, B, B, F, F, F, F],
         [F, B, B, B, B, B, B, B, B, B, B, B, B, F, F, F],
         [F, B, B, B, B, B, B, B, B, B, B, B, B, F, F, F],
         [F, B, B, B, S, S, S, S, S, S, S, B, B, F, F, F],
         [F, B, B, S, S, W, B, S, S, W, B, S, B, F, F, F],
         [F, B, S, S, S, S, S, S, S, S, S, S, B, F, F, F],
         [F, B, B, S, S, S, S, S, S, S, S, S, B, F, F, F],
         [F, F, F, F, S, S, S, S, S, S, S, F, F, F, F,BR],
         [F, F, R, R,DR,DR,DR,DR,DR,BR,BR, F, F, F, F,BR],
         [F, R, R, R,DR,DR,DR,DR, B,BR, R, R, F, F, F,BR],
         [R, R, R, R,DR,DR, B, B,DR,BR, R, R, R, F, F,BR],
         [R, R, R, R, B, B,DR,DR,DR,DR,BR, R, R, R, R, S],
         [R, R, R, R, B, B, B, B, B, B,BR, R, R, R, R,BR],
         [R, R, R, R,DR,DR,DR,DR,DR,DR,BR, R, F, F, F, F],
         [S, S, R, R,DR, B, B, B, B, B,BR, R, R, F, F, F],
         [F, F, R, R, B, B, B, R, B, B, B,BR, R, F, F, F],
         [F, F, R, R, B, B, R, R, R, B, B,BR, R, F, F, F],
         [F, F, R, R, B, B, F, F, F, B, B,BR, R, R, F, F]]

fleur = [[ F, F, F, Y, Y, Y, Y, Y, Y, Y, Y, F, F, F, F, F],
         [ F, F, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, F, F, F, F],
         [ F, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, F, F, F],
         [ F, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, F, F, F],
         [ F, Y, Y, Y, S, S, S, S, S, S, S, Y, Y, F, F, F],
         [ F, Y, Y, S, S, W,LB, S, S, W,LB, S, Y, F, F, F],
         [ F, Y, S, S, S, S, S, S, S, S, S, S, Y, F, F, F],
         [ F, Y, Y, S, S, S, S, S, S, S, S, S, Y, F, F, F],
         [ F, Y, Y, Y, S, S, S, S, S, S, S, Y, Y, F, F,BR],
         [ F, Y,BL,BL,BL, W, W, W, W, W,BL, Y, Y, F, F,BR],
         [ F,BL,BL,BL,BL,BL, W, W, W,BL,BL,BL, Y, F, F,BR],
         [BL,BL,BL,BL,BL,BL, W, W, W,BL,BL,BL,BL, F, F,BR],
         [BL,BL,BL,BL,BL,BL,BL,BL,BL,BL,BL,BL,BL,BL,BL, S],
         [BL,BL,BL,BL,BL,BL,BL, W,BL,BL,BL,BL,BL,BL,BL,BR],
         [BL,BL,BL,BL,BL,BL, W, W, W,BL,BL,BL, F, F, F, F],
         [ S, S,BL,BL,BL, B, B, B, B, B,BL,BL, F, F, F, F],
         [ F, F,BL,BL, B, B, B,BL, B, B, B,BL, F, F, F, F],
         [ F, F,BL,BL, B, B,BL,BL,BL, B, B,BL, F, F, F, F],
         [ F, F,BL,BL, B, B, F, F, F, B, B,BL, F, F, F, F]]


# Make a player
player = [2, 1, 1.5, 1.5]
player_vx = 0
player_vy = 0
player_speed = .15

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
    global player, stage, cups, score, time_remaining, ticks, win
    
    c_size = 2
    cup1 = [4, 19, c_size, c_size]
    cup2 = [25, 25, c_size, c_size]
    cup3 = [16, 16, c_size, c_size]
    cup4 = [28, 4, c_size, c_size]
    cups = [cup1, cup2, cup3, cup4]
    
    score = 0
    player = [2, 1, 1.5, 1.5]
    stage = START
    time_remaining = 30
    ticks = 0
    win = False

wizard = ["h", harry]
alt1 = ["k", krum]
alt2 = ["f", fleur]
alt3 = ["c", cedric]

# Game loop
big_font = pygame.font.Font(None, scale * 2)
small_font = pygame.font.Font(None, scale)
score = 0
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
                elif event.key == pygame.K_k:
                    wizard = ["k", krum]
                    alt1 = ["h", harry]
                    alt2 = ["f", fleur]
                    alt3 = ["c", cedric]
                elif event.key == pygame.K_h:
                    wizard = ["h", harry]
                    alt1 = ["k", krum]
                    alt2 = ["f", fleur]
                    alt3 = ["c", cedric]
                elif event.key == pygame.K_f:
                    wizard = ["f", fleur]
                    alt1 = ["h", harry]
                    alt2 = ["k", krum]
                    alt3 = ["c", cedric]
                elif event.key == pygame.K_c:    
                    wizard = ["c", cedric]
                    alt1 = ["h", harry]
                    alt2 = ["f", fleur]
                    alt3 = ["k", krum]
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

        if left < 0 and player_vx < 1:
            player[0] = 30
            player[1] = 28
        if right > WIDTH and player_vx >= 0:           
            if len(cups) == 0:
                win = True
            else:
                player[0] = 0
                player[1] = 1

        '''timer stuff'''
        ticks += 1

        if ticks % refresh_rate == 0:
            time_remaining -= 1

        if time_remaining == 0:
            stage = END

        ''' get the cups '''        
        #coins = [c for c in coins if not intersects.rect_rect(player, c)]
         
        hit_list = [c for c in cups if intersects.rect_rect(player, c)]
        
        for hit in hit_list:
            cups.remove(hit)
            score += 1
            time_remaining += 5
            print("sound!")

        if win:
            stage = END
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(VDG) 

    if stage == START:
        text1 = big_font.render("WELCOME TO THE TRIWIZARD MAZE!", True, Y)
        text2 = small_font.render("perilous adventure awaits within...", True, MG)
        text3 = small_font.render("press space to start", True, MG)
        text_width1 = text1.get_width()
        text_width2 = text2.get_width()
        text_width3 = text3.get_width()
        height = text1.get_height() + text2.get_height() + text3.get_height() 
        screen.blit(text1, [(388/25 * scale) - (text_width1 / 2), (388/25 * scale) - 35/25 * scale])
        screen.blit(text2, [(388/25 * scale) - (text_width2 / 2), (388/25 * scale) + 5/25 * scale])
        screen.blit(text3, [(388/25 * scale) - (text_width3 / 2), (388/25 * scale) + 25/25 * scale])


        text4 = small_font.render("press " + str(alt1[0]), True, MG)
        text5 = small_font.render("press " + str(alt2[0]), True, MG)
        text6 = small_font.render("press " + str(alt3[0]), True, MG)
        screen.blit(text4, [2 * scale + 1.5 * scale, 20 * scale + (8 * scale)])
        screen.blit(text5, [12.3 * scale + 1.5 * scale, 20 * scale + (8 * scale)])
        screen.blit(text6, [23.8 * scale + 1.5 * scale, 20 * scale + (8 * scale)])

        
        draw_image(wizard[1], 12.3, 4, scale, 10/25 * scale)
        draw_image(cup, 2, 4, scale, 10/25 * scale)
        draw_image(cup, 23.8, 4, scale, 10/25 * scale)
        draw_image(alt1[1], 2, 20, scale, 10/25 * scale)
        draw_image(alt2[1], 12.3, 20, scale, 10/25 * scale)
        draw_image(alt3[1], 23.8, 20, scale, 10/25 * scale)


    if stage == PLAYING:
        draw_image(wizard[1], player[0], player[1], scale, 2)
        draw_image(maze, 0, 0, scale, scale)
        '''spotlight(maze, 0, 0, scale, scale, player[0], player[1])'''
       
        for c in cups:
            draw_image(cup, c[0], c[1], scale, 3)

        text = small_font.render( "score: " + str(score), True, Y)
        screen.blit(text, [28 * scale, 0]) 
            
    if stage == END:
        if win:
            text1 = big_font.render("You Win!", True, Y)
        else:
            text1 = big_font.render("You Lose!", True, R)
        text2 = small_font.render("press space to reset", True, MG)
        text_width1 = text1.get_width()
        text_width2 = text2.get_width()
        text_height1 = text1.get_height()
        text_height2 = text2.get_height()
        screen.blit(text1, [(388/25 * scale) - (text_width1 / 2), (388/25 * scale) - text_height1])
        screen.blit(text2, [(388/25 * scale) - (text_width2 / 2), (388/25 * scale) + text_height1 / 2])

        draw_image(wizard[1], 12.3, 4, scale, 10/25 * scale)
        draw_image(cup, 2, 4, scale, 10/25 * scale)
        draw_image(cup, 23.8, 4, scale, 10/25 * scale)
        draw_image(alt1[1], 2, 20, scale, 10/25 * scale)
        draw_image(alt2[1], 12.3, 20, scale, 10/25 * scale)
        draw_image(alt3[1], 23.8, 20, scale, 10/25 * scale)

    ''' timer text '''
    timer_text = small_font.render("Time: " + str(time_remaining), True, Y)
    screen.blit(timer_text, [1, 1])
    
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
