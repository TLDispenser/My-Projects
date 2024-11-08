#packages
import pygame
import sys
import math

import textures_and_mapps

#import help
#I dont know what this does
#import ctypes

# Increas Dots Per inch so it looks sharper
#ctypes.windll.shcore.SetProcessDpiAwareness(True)
#global constants
SCREEN_HEIGHT = 480 
SCREEN_WIDTH = SCREEN_HEIGHT * 2
MAP_SIZE = 22
TEXTURE_SIZE = 16
TILE_SIZE = int((SCREEN_WIDTH / 2) / MAP_SIZE)
FOV =  math.pi / 3
HALF_FOV = FOV / 2
TILES_TO_SEE = 6
CASTED_RAYS = TEXTURE_SIZE * TILES_TO_SEE
STEP_ANGLE = FOV / CASTED_RAYS
MAX_DEPTH = int(MAP_SIZE * TILE_SIZE)
SCALE = (SCREEN_WIDTH / 2) / CASTED_RAYS
SCALE_texture = (SCREEN_HEIGHT / 2) / TEXTURE_SIZE 
MAX_FPS = 30
HIT_TOLERANCE = 5
#MAX_WALL_HEIGHT = 21000  / 2.5
ORIGANAL_PLAYER_SPEED = 2
#global variables
player_speed = ORIGANAL_PLAYER_SPEED
player_x = (SCREEN_WIDTH / 2) / 2
player_y = (SCREEN_WIDTH / 2) / 2
player_angle = math.pi
#just math quick
PIE = math.pi
PIEPIE = math.pi *2
#texture 2

#texture 1
WALL1_TEXTURE = textures_and_mapps.BASE_TEXTURE
#map
MAP = textures_and_mapps.TESTING_MAP
#MUSHROOM!
MUSHROOMM = textures_and_mapps.MUSHROOM

#init pygame
pygame.init()

#game window
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption('Ray-casting')

#init timer
clock = pygame.time.Clock()

def draw_map():
    #iterate over map
    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE):
            #calculate square index
            square = i * MAP_SIZE + j

            #draw map
            pygame.draw.rect(
                win, (191, 191, 191) if MAP[square] != ' ' else (65, 65, 65),
                (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1)
            )

    #draw player
    pygame.draw.circle(win, (162, 0, 255), (int(player_x), int(player_y)), 12)

#ray-casting algorithm
def ray_casting(printt):
    visible_tiles = set()
    #left angle of FOV
    start_angle = player_angle - HALF_FOV
    #lists
    temp_what_is_it_list = []
    temp_depth_list = []
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
                #colors the map tiles to show what you are looking at
                pygame.draw.rect(win, (195, 137, 38), (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1))
                
                #draw casted ray
                pygame.draw.line(win, (233, 166, 49), (player_x, player_y), (target_x, target_y))
                
                #fix fish eye effect
                depth *= math.cos(player_angle - start_angle) 
                
                temp_depth_list.append(depth) 
                
                #sees how may tiles there are
                visible_tiles.add((col, row))
                
                #adds where what direction you see the side at ( also im lazy so i converted to readians)
                temp_start_angle = (start_angle % (PIEPIE))
                if math.radians(0) <= temp_start_angle <= math.radians(45) or math.radians(315) < temp_start_angle <= math.radians(360):
                    side_its_on = "S"
                elif math.radians(45) < temp_start_angle <= math.radians(135):
                    side_its_on = "W"
                elif math.radians(135) < temp_start_angle <= math.radians(225):
                    side_its_on = "N"
                elif math.radians(225) < temp_start_angle <= math.radians(315):
                    side_its_on = "E"
                else:
                    side_its_on = "?"
                    print(temp_start_angle)
                #what is symbol is there and record it AND what side its on as a string
                temp_what_is_it_list.append(str(MAP[square]) + str(side_its_on))
                break
        #increment angle by step
        start_angle += STEP_ANGLE
    #IT GOES TEXTURE STRING VALUE THEN HOW MANY THERE ARE
    result = []
    current_run_character = ""
    run_length = 0
    #gets all the things on screen list and reurns groups of whats there 
    for i in range(len(temp_what_is_it_list)):
        # If it's the start of the string, the current run starts with
        # the first character
        if i == 0:
            current_run_character = temp_what_is_it_list[i]
            run_length = 1
        else:
            current_char = temp_what_is_it_list[i]
            if current_char == current_run_character:
                run_length += 1
            else:
                # The run is over, add this run to the result
                result.append(current_run_character)
                result.append(run_length)
                # Reset the run variables
                current_run_character = current_char
                run_length = 1
    result.append(current_run_character)
    result.append(run_length)
    for pixel_y_pozition in range(TEXTURE_SIZE):
        #counter for walls
        texture_counter = 0
        number_of_symbol_prevous = 0
        temp_depth_range_counter = 0
        for where_and_how_much in range(0, len(result), 2):
            #texture_counter = result[where_and_how_much + 1] % TEXTURE_SIZE
            #use 1 devoided my somthing like depth to not increase when geting closer
            #check to see how many tiles im seeing!!!!!!!
            texture_counter_increaser = len(visible_tiles) / TEXTURE_SIZE
            for number_of_symbol in range(result[where_and_how_much + 1]):
                depth = temp_depth_list[temp_depth_range_counter]
                #calculate wall_height
                wall_height = (TILE_SIZE * SCREEN_HEIGHT) / (depth + 0.1)
                # Fix wall height if too large or small
                
                if wall_height > SCREEN_HEIGHT:
                    wall_height = SCREEN_HEIGHT
                elif wall_height < TILE_SIZE:
                    wall_height = TILE_SIZE
                #here is how to add what you want with colors
                if result[where_and_how_much][0] == '#':
                    color0 = (int(WALL1_TEXTURE[int(texture_counter) + (pixel_y_pozition * TEXTURE_SIZE)]) * 255) / (1 + depth * depth * 0.0001)
                    color1 = (int(WALL1_TEXTURE[int(texture_counter) + (pixel_y_pozition * TEXTURE_SIZE)]) * 255) / (1 + depth * depth * 0.0001)
                    color2 = (int(WALL1_TEXTURE[int(texture_counter) + (pixel_y_pozition * TEXTURE_SIZE)]) * 255) / (1 + depth * depth * 0.0001)
                if result[where_and_how_much][0] == 'b':
                    color0 = 255 / (1 + depth * depth * 0.0001)
                    color1 = 0 / (1 + depth * depth * 0.0001)
                    color2 = 0 / (1 + depth * depth * 0.0001)
                if result[where_and_how_much][0] == 'M':
                    texture_position = int(texture_counter) #(texture_counter // TILES_TO_SEE) * (TEXTURE_SIZE // (TEXTURE_SIZE // TILES_TO_SEE))
                    #(texture_counter / TILES_TO_SEE) * TEXTURE_SIZE
                    #(TILES_TO_SEE / texture_counter)
                     #ONLY WANT TO SHOW 1 so maybe devide or multply by TILES_TO_SEE BUT it figure out to to keep in array
                    color0 = MUSHROOMM[pixel_y_pozition][texture_position][0] / (1 + depth * depth * 0.0001)
                    color1 = MUSHROOMM[pixel_y_pozition][texture_position][1] / (1 + depth * depth * 0.0001)
                    color2 = MUSHROOMM[pixel_y_pozition][texture_position][2] / (1 + depth * depth * 0.0001)
                #draw 3D projection
                """pygame.draw.rect(what screen? , color (hex), (x, y, width, hight)"""
                if printt and pixel_y_pozition == 0:
                    print(f"{result[where_and_how_much]}, Line: {pixel_y_pozition}, {number_of_symbol} / {result[where_and_how_much + 1]} of {result[where_and_how_much + 1]}, {number_of_symbol + number_of_symbol_prevous + 1} / {CASTED_RAYS} rays, {temp_depth_range_counter + 1} / {len(temp_depth_list)} depths = depth of {depth}, (Increasing by {texture_counter_increaser}) {texture_counter} / {TEXTURE_SIZE} int(pixel#on texture), texture counter on: cololm: {texture_counter} row: {pixel_y_pozition} ({int(texture_counter) + (pixel_y_pozition * TEXTURE_SIZE)} / {TEXTURE_SIZE * TEXTURE_SIZE}) wich is a {WALL1_TEXTURE[int(texture_counter) + (pixel_y_pozition * TEXTURE_SIZE)]}, length is {len(visible_tiles)}, angle im at {player_angle} direction facing {result[where_and_how_much][0]}")
                pygame.draw.rect(win, (color0, color1, color2),  (SCREEN_WIDTH  / 2 + ((number_of_symbol + number_of_symbol_prevous) * SCALE),  ((SCREEN_HEIGHT / 2) - (wall_height / 2)) + (((wall_height / TEXTURE_SIZE) * (pixel_y_pozition))) , SCALE, wall_height /  (TEXTURE_SIZE / 2)))
                # Increment `texture_counter` and wrap around if it exceeds `TEXTURE_SIZE`
                texture_counter += texture_counter_increaser 
                if texture_counter >= TEXTURE_SIZE:
                    texture_counter = 0  # Wrap counter within texture array bounds
                temp_depth_range_counter += 1
            #int(texture_counter)      
            number_of_symbol_prevous +=  result[where_and_how_much + 1]
            texture_counter = 0
    pygame.display.flip()
#movement direction
forward = True
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
    ray_casting(False)

    #get user input
    keys_turn = pygame.key.get_pressed()

    #handle user input
    if keys_turn[pygame.K_LEFT]:
        #working with radians, not degrees
        player_angle -= 0.1
    elif keys_turn[pygame.K_RIGHT]:
        player_angle += 0.1
        
    keys_move = pygame.key.get_pressed()
    
    if keys_move[pygame.K_UP]:
        forward = True
        player_x += -1 * math.sin(player_angle) * 5
        player_y += math.cos(player_angle) * 5
    elif keys_move[pygame.K_DOWN]:
        forward = False
        player_x -= -1 * math.sin(player_angle) * 5
        player_y -= math.cos(player_angle) * 5
        
    keys_print = pygame.key.get_pressed()
    #prints out screenshot of everything
    if keys_print[pygame.K_SPACE]:
        ray_casting(True)
    #set FPS
    clock.tick(30)

    #set FPS
    fps = str(int(clock.get_fps()))
    font = pygame.font.SysFont('Arial', 30)
    fpssurface = font.render(fps, False, (255, 255, 255))
    win.blit(fpssurface, (int(SCREEN_WIDTH / 2), 0))
    #update display
    pygame.display.flip()
