#packages
import pygame
import sys
import math

#import help

#global constants
SCREEN_HEIGHT = 480 
SCREEN_WIDTH = SCREEN_HEIGHT * 2
MAP_SIZE = 22
TILE_SIZE = int((SCREEN_WIDTH / 2) / MAP_SIZE)
FOV =  math.pi / 3
HALF_FOV = FOV / 2
CASTED_RAYS = 160
STEP_ANGLE = FOV / CASTED_RAYS
MAX_DEPTH = int(MAP_SIZE * TILE_SIZE)
SCALE = (SCREEN_WIDTH / 2) / CASTED_RAYS 
MAX_FPS = 30
HIT_TOLERANCE = 5
MAX_WALL_HEIGHT = 21000  / 2.5
ORIGANAL_PLAYER_SPEED = 2
#global variables
player_speed = ORIGANAL_PLAYER_SPEED
player_x = (SCREEN_WIDTH / 2) / 2
player_y = (SCREEN_WIDTH / 2) / 2
player_angle = math.pi

#map
WALL1_TEXTURE = (
    "111111111111"  
    "100001110011"  
    "100001111011"  
    "100001111111" 
    "111111111111"  
    "110110000111"  
    "110111100111"  
    "111111101111"  
    "110000111111"  
    "100000011011"  
    "111000111011"  
    "111111111111" 
)
WALL2_TEXTURE = (
    "1111111111111"  
    "1000011100111"  
    "1000011110111"  
    "1000011111111" 
    "1111111111111"  
    "1101100001111"  
    "1101111001111"  
    "1111111011111"  
    "1100001111111"  
    "1000000110111"  
    "1110001110111"  
    "1111111111110"
    "1111111111111"
)
#22 map size
"""
MAP = (
    "######################"
    "#       r    e       #"
    "#  e   r    ######## #"
    "# e  reer   # e  e e #"
    "#e   r  r   # ########"
    "#  g r  r   #   eee  #"
    "#   er  e   ######## #"
    "#   errrrrrr#eeeeeeee#"
    "#           #eeeeeeee#"
    "##########e## ########"
    "#ggggggg#   #eeeeeeee#"
    "#g     g#   #eeeeeeee#"
    "#g     g#   #eeeeeeee#"
    "#eeeeeee############e#"
    "#  e     e      e    #"
    "#       e            #"
    "#    e     e   e     #"
    "#   e    e           #"
    "#           e    e   #"
    "#   e    e           #"
    "#   e           e    #"
    "######################"
)
"""
"""
#12 map size
MAP = (
    "############"
    "# e        #"
    "#          #"
    "# m        #"
    "#          #"
    "# q        #"
    "#          #"
    "# g        #"
    "#          #"
    "# r        #"
    "#          #"
    "############"
)
"""
"""
#12 map size
MAP = (
    "############"
    "#      #   #"
    "# #  r #   #"
    "# #    #   #"
    "# #        #"
    "# #     m  #"
    "# #        #"
    "# ####### ##"
    "# #        #"
    "# #  e     #"
    "# #        #"
    "############"
)
"""
"""
MAP = (
    "######################"
    "#                    #"
    "#                    #"
    "#                    #"
    "#                    #"
    "#                    #"
    "#                    #"
    "#                    #"
    "#                    #"
    "#                    #"
    "#                    #"
    "#                    #"
    "#                    #"
    "#                    #"
    "#                    #"
    "#                    #"
    "#                    #"
    "#                    #"
    "#                    #"
    "#                    #"
    "#                    #"
    "######################"
)
"""
MAP = (
    "######################"
    "#                    #"
    "#                    #"
    "#  e                 #"
    "#                    #"
    "#                    #"
    "#  m                 #"
    "#                    #"
    "#                    #"
    "#  q                 #"
    "#                    #"
    "#                    #"
    "#  g                 #"
    "#                    #"
    "#                    #"
    "#  r                 #"
    "#                    #"
    "#                    #"
    "#  b                 #"
    "#                    #"
    "#                    #"
    "######################"
)
#NOTES
'''
pygame.draw.rect(what screen? , color (hex), (x, y, width, hight)
'''
#init pygame
pygame.init()

#game window
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("The game")

#init timer
clock = pygame.time.Clock()

def draw_map():
    #iterate over map
    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE):
            #calculate square index
            square = i * MAP_SIZE + j

            #draw map
            if MAP[square] == '#':
                pygame.draw.rect(
                win,  (191, 191, 191), (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1)
                )
            elif MAP[square] == 'e':
                pygame.draw.rect(
                win,  (255, 0, 0), (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1)
                )
            else:
                pygame.draw.rect(
                win,  (65, 65, 65), (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1)
                )

    #draw player
    pygame.draw.circle(win, (162, 0, 255), (int(player_x), int(player_y)), 12)

#ray-casting algorithm
r_counter = 0
g_counter = 0
def ray_casting():
    #left angle of FOV
    start_angle = player_angle - HALF_FOV
    #iterate over casted rays
    for ray in range(CASTED_RAYS):
        for depth in range(MAX_DEPTH):
            #get ray target coordinates
            target_x = player_x - math.sin(start_angle) * depth
            target_y = player_y +  math.cos(start_angle) * depth

            #convert target x, y coordinates to map col, row
            col = int(target_x / TILE_SIZE)
            row = int(target_y / TILE_SIZE)
            #calculate map square index
            square = row * MAP_SIZE + col
            if MAP[square] != ' ':
                pygame.draw.rect(win, (195, 137, 38), (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1))
                    
                #draw casted ray
                pygame.draw.line(win, (233, 166, 49), (player_x, player_y), (target_x, target_y))
                
                #fix fish eye effect
                depth_temp = depth
                depth_temp *= math.cos(player_angle - start_angle) 

                #calculate wall_height
                wall_height = MAX_WALL_HEIGHT / (depth_temp) #21000

                #fix stuck at the wall
                if wall_height > SCREEN_HEIGHT:
                    wall_height = SCREEN_HEIGHT

            #print(square)
            def make_object_3d():
                #wall shading
                if ray % 2 == 0:
                    color1 = 255 / (1 + depth * depth * 0.0001)
                    color2 = 0 / (1 + depth * depth * 0.0001)
                    color3 = 0 / (1 + depth * depth * 0.0001)
                else:
                    color1 = 255 / (1 + depth * depth * 0.0001)
                    color2 = 255 / (1 + depth * depth * 0.0001)
                    color3 = 255 / (1 + depth * depth * 0.0001)

                #draw 3D projection
                # more lines is what i is devided by 
                
                for i in range(0, 10, 1):
                    q = i / 10
                    if i % 2 == 0:
                        color1 = 0 / (1 + depth * depth * 0.0001)
                    else:
                        color1 = 255 / (1 + depth * depth * 0.0001)
                    pygame.draw.rect(win, (color1, color2, color3), (SCREEN_HEIGHT + ray * SCALE, (SCREEN_HEIGHT / 2 ) - wall_height / 2 + wall_height * q, SCALE , wall_height - wall_height * q))
            if MAP[square] == 'e':
                #wall shading
                color1 = 255 / (1 + depth * depth * 0.0001)
                color2 = 0 / (1 + depth * depth * 0.0001)
                color3 = 0 / (1 + depth * depth * 0.0001)
                
                #draw 3D projection
                pygame.draw.rect(win, (color1, color2, color3), (SCREEN_HEIGHT + ray * SCALE, (SCREEN_HEIGHT / 2) - wall_height / 2, SCALE, wall_height ))
                break
            #try to make circle
            if MAP[square] == 'm':
                #draw 3D projection
                for i in range(0, 12, 1):
                    q = i / 12
                    if i < 2:
                        color1 = 200
                        color2 = 200
                        color3 = 200
                    elif i <= 5 :
                        color1 = 255 / (1 + depth * depth * (6 - i) * 0.0001)
                        color2 = 0 / (1 + depth * depth * 0.0001)
                        color3 = 0 / (1 + depth * depth * 0.0001)
                    elif i >= 10:
                        color1 = 100
                        color2 = 100
                        color3 = 100
                    elif i >= 6:
                        color1 = 255 / (1 + depth * depth * (i - 5) * 0.0001)
                        color2 = 0 / (1 + depth * depth * 0.0001)
                        color3 = 0 / (1 + depth * depth * 0.0001)
                    else:
                        color1 = 255 / (1 + depth * depth  * 0.0001)
                    pygame.draw.rect(win, (color1, color2, color3), (SCREEN_HEIGHT + ray * SCALE, (SCREEN_HEIGHT / 2 ) - wall_height / 2 + wall_height * q, SCALE , wall_height - wall_height * q))
                break
            if MAP[square] == 'q':
                for i in range(0, 12, 1):
                    q = i / 12
                    color1 = 255 / (1 + depth * depth * i * 0.0001)
                    color2 = 255 / (1 + depth * depth * i * 0.0001)
                    color3 = 255 / (1 + depth * depth * i * 0.0001)
                    pygame.draw.rect(win, (color1, color2, color3), (SCREEN_HEIGHT + ray * SCALE, (SCREEN_HEIGHT / 2 ) - wall_height / 2 + wall_height * q, SCALE , wall_height - wall_height * q))
                break
            #moving wall for some reasn
            if MAP[square] == 'g':
                global g_counter
                if g_counter >= 13:
                    g_counter  = 0
                #draw 3D projection
                for i in range(0, 13, 1):
                    q = i / 12
                    color1 = (int(WALL2_TEXTURE[i + (g_counter * 12)]) * 255) / (1 + depth * depth * 0.0001)
                    color2 = (int(WALL2_TEXTURE[i + (g_counter * 12)]) * 255) / (1 + depth * depth * 0.0001)
                    color3 = (int(WALL2_TEXTURE[i + (g_counter * 12)]) * 255) / (1 + depth * depth * 0.0001)
                    pygame.draw.rect(win, (color1, color2, color3), (SCREEN_HEIGHT + ray * SCALE, (SCREEN_HEIGHT / 2 ) - wall_height / 2 + wall_height * q, SCALE , wall_height - wall_height * q))
                g_counter += 1
                break
            #texture wall
            if MAP[square] == 'r':
                global r_counter
                if r_counter >= 12:
                    r_counter  = 0
                #draw 3D projection
                for i in range(0, 12, 1):
                    q = i / 12
                    color1 = (int(WALL1_TEXTURE[i + (r_counter * 12)]) * 255) / (1 + depth * depth * 0.0001)
                    color2 = (int(WALL1_TEXTURE[i + (r_counter * 12)]) * 255) / (1 + depth * depth * 0.0001)
                    color3 = (int(WALL1_TEXTURE[i + (r_counter * 12)]) * 255) / (1 + depth * depth * 0.0001)
                    pygame.draw.rect(win, (color1, color2, color3), (SCREEN_HEIGHT + ray * SCALE, (SCREEN_HEIGHT / 2 ) - wall_height / 2 + wall_height * q, SCALE , wall_height - wall_height * q))
                r_counter += 1
                break
            if MAP[square] == '#':
                make_object_3d()
                break
        #increment angle by step
        start_angle += STEP_ANGLE
    #do this to reset total so doesesent go ober and look like its moving
    r_counter = 0
#movement direction
forward = True
#enimi loop
qqq = 0
index = 10 * MAP_SIZE + 6
#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    #convert player x, y coordinates to map col, row
    col = int(player_x / TILE_SIZE)
    row = int(player_y / TILE_SIZE)  

    #calculate map square index
    square = row * MAP_SIZE + col

    # player hits the wall (collision detection)
    if MAP[square] != ' ':
        if forward:
            player_x -= -1 * math.sin(player_angle) * 5
            player_y -= math.cos(player_angle) * 5
        else:
            player_x += -1 * math.sin(player_angle) * 5
            player_y += math.cos(player_angle) * 5
            
    
    #update 2D background
    pygame.draw.rect(win, (0, 0, 0), (0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT))

    #update 3D background
    pygame.draw.rect(win, (100, 100, 100), (480, SCREEN_HEIGHT / 2, SCREEN_HEIGHT, SCREEN_HEIGHT))
    pygame.draw.rect(win, (200, 200, 200), (480, -SCREEN_HEIGHT / 2, SCREEN_HEIGHT, SCREEN_HEIGHT))

    draw_map()
    ray_casting()

    #get user input
    keys = pygame.key.get_pressed()
    #handle user input
    if keys[pygame.K_LSHIFT]:
        player_speed *= player_speed
    elif keys[pygame.K_LEFT]:
        #working with radians, not degrees
        player_angle -= 0.1
    elif keys[pygame.K_RIGHT]:
        player_angle += 0.1
    elif keys[pygame.K_UP]:
        forward = True
        player_x += -1 * math.sin(player_angle) * player_speed
        player_y += math.cos(player_angle) * player_speed
    elif keys[pygame.K_DOWN]:
        forward = False
        player_x -= -1 * math.sin(player_angle) * player_speed
        player_y -= math.cos(player_angle) * player_speed
    elif keys[pygame.K_z]:
        if qqq == 0:
            MAP = MAP[:index] + " " + MAP[index + 1:]
            MAP = MAP[:index + 1] + "e" + MAP[index + 2:]
            qqq += 1
        else:
            MAP = MAP[:index + 1] + " " + MAP[index + 2:]
            MAP = MAP[:index] + "e" + MAP[index + 1:]
            qqq -= 1
    elif keys[pygame.K_SPACE]:
        for depth in range(MAX_DEPTH):
            target_x = player_x - math.sin(player_angle) * depth
            target_y = player_y + math.cos(player_angle) * depth

            # Convert player x, y coordinates to map col, row
            col = int(target_x / TILE_SIZE)
            row = int(target_y / TILE_SIZE)
            if MAP[square] != " " or MAP[square] == "e":
                break
            else:
                if 0 <= col < MAP_SIZE and 0 <= row < MAP_SIZE:
                    # Calculate map square index
                    square = row * MAP_SIZE + col
                    
                # Check for a hit on "e" with tolerance
                    if MAP[square] == "e":
                        MAP = MAP[:square] + " " + MAP[square + 1:]
                        break
                else:
                    # If out of bounds, stop checking further
                    break
    
    #set FPS
    clock.tick(MAX_FPS)
    
    #set FPS
    fps = str(int(clock.get_fps()))
    font = pygame.font.SysFont('Arial', 30)
    fpssurface = font.render(fps, False, (255, 255, 255))
    win.blit(fpssurface, (int(SCREEN_WIDTH / 2), 0))

    #middle cross hair
    cross = "x"
    font = pygame.font.SysFont('Arial', 30)
    crosssurface = font.render(cross, False, (255, 255, 0))
    win.blit(crosssurface, (int(SCREEN_WIDTH / 1.35 ), SCREEN_HEIGHT / 2 - 30))
    
    #update display
    pygame.display.flip()
    
    #update varables
    player_speed = 2
