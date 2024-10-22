#packages
import pygame
import sys
import math

#import help

#global constants
SCREEN_HEIGHT = 480 
SCREEN_WIDTH = SCREEN_HEIGHT * 2
MAP_SIZE = 22
TEXTURE_SIZE = 16
TILE_SIZE = int((SCREEN_WIDTH / 2) / MAP_SIZE)
FOV =  math.pi / 3
HALF_FOV = FOV / 2
CASTED_RAYS = TEXTURE_SIZE * 6
STEP_ANGLE = FOV / CASTED_RAYS
MAX_DEPTH = int(MAP_SIZE * TILE_SIZE)
SCALE = (SCREEN_WIDTH / 2) / CASTED_RAYS
SCALE_texture = (SCREEN_HEIGHT / 2) / TEXTURE_SIZE 
MAX_FPS = 30
HIT_TOLERANCE = 5
MAX_WALL_HEIGHT = 21000  / 2.5
ORIGANAL_PLAYER_SPEED = 2
#global variables
player_speed = ORIGANAL_PLAYER_SPEED
player_x = (SCREEN_WIDTH / 2) / 2
player_y = (SCREEN_WIDTH / 2) / 2
player_angle = math.pi



WALL1_TEXTURE = (
    "0000000101111111" #just added this to make debug ezey
    "0000000000000000"
    "0111111111111110"
    "0111111111111110"
    "0111111111111110"
    "0111111111111110"
    "0111111111111110"
    "0111111111111110"
    "0111111111111110"
    "0111111111111110"
    "0111111111111110"
    "0111111111111110"
    "0111111111111110"
    "0111111111111110"
    "0111111111111110"
    "0111111111111110"
    #"0000000000000000"
    )
#map
MAP = (
    "######################"
    "#                    #"
    "#                    #"
    "#                    #"
    "#       b    b       #"
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
#init pygame
pygame.init()

#game window
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ray-casting')


def ray_casting():
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
                pygame.draw.rect(win, (195, 137, 38), (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1))
                    
                #draw casted ray
                pygame.draw.line(win, (233, 166, 49), (player_x, player_y), (target_x, target_y))
                
                temp_what_is_it_list.append(MAP[square])
                
                #fix fish eye effect
                depth *= math.cos(player_angle - start_angle) 
                
                temp_depth_list.append(depth)   
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
    print(f"Casting summerised{result}")
    for pixel_y_pozition in range(TEXTURE_SIZE):
        #counter for walls
        #texture_counter = 0 whent to where_and_how_much
        texture_counter_increaser = 1
        number_of_symbol_prevous = 0
        temp_depth_range_counter = 0
        for where_and_how_much in range(0, len(result), 2):
            texture_counter = result[where_and_how_much + 1] / TEXTURE_SIZE
            for number_of_symbol in range(result[where_and_how_much + 1]):
                depth = temp_depth_list[temp_depth_range_counter]
                if pixel_y_pozition == 0:
                    print(f"{result[where_and_how_much]}, Line: {pixel_y_pozition}, {number_of_symbol} / {result[where_and_how_much + 1]} of {result[where_and_how_much + 1]}, {number_of_symbol + number_of_symbol_prevous + 1} / {CASTED_RAYS} rays, {temp_depth_range_counter + 1} / {len(temp_depth_list)} depths = depth of {depth}, (Increasing by {texture_counter_increaser}) {texture_counter} / {TEXTURE_SIZE} int(pixel#on texture), texture counter on: cololm: {texture_counter} row: {pixel_y_pozition} ({int(texture_counter) + (pixel_y_pozition * TEXTURE_SIZE)} / {TEXTURE_SIZE * TEXTURE_SIZE}) wich is a {WALL1_TEXTURE[int(texture_counter) + (pixel_y_pozition * TEXTURE_SIZE)]}")
                #calculate wall_height
                wall_height = MAX_WALL_HEIGHT / (depth) #21000

                #fix stuck at the wall
                if wall_height > SCREEN_HEIGHT:
                    wall_height = SCREEN_HEIGHT
                    
                if result[where_and_how_much] == '#':
                    #print(f"{texture_counter + (pixel_y_pozition * TEXTURE_SIZE)} / {len(WALL1_TEXTURE)}")
                    color1 = (int(WALL1_TEXTURE[int(texture_counter) + (pixel_y_pozition * TEXTURE_SIZE)]) * 255) / (1 + depth * depth * 0.0001)
                    color2 = (int(WALL1_TEXTURE[int(texture_counter) + (pixel_y_pozition * TEXTURE_SIZE)]) * 255) / (1 + depth * depth * 0.0001)
                    color3 = (int(WALL1_TEXTURE[int(texture_counter) + (pixel_y_pozition * TEXTURE_SIZE)]) * 255) / (1 + depth * depth * 0.0001)
                if result[where_and_how_much] == 'b':
                    color1 = 255 / (1 + depth * depth * 0.0001)
                    color2 = 0 / (1 + depth * depth * 0.0001)
                    color3 = 0 / (1 + depth * depth * 0.0001)
                #draw 3D projection
                """pygame.draw.rect(what screen? , color (hex), (x, y, width, hight)"""
                pygame.draw.rect(win, (color1, color2, color3),  (SCREEN_WIDTH  / 2 + ((number_of_symbol + number_of_symbol_prevous) * SCALE),  ((SCREEN_HEIGHT / 2) - (wall_height / 2)) + (((wall_height / TEXTURE_SIZE) * (pixel_y_pozition))) , SCALE, wall_height /  (TEXTURE_SIZE / 2)))
                # FIX HERE TO FIX WARPING OF WALLS UDWAUDHWAUDYHUI 
                #texture_counter = int(number_of_symbol / TEXTURE_SIZE) #* TEXTURE_SIZE
                # ALSO FIGURE OUT HOW TO DITECT 1/16 of a  wall and so on !!!!!!
                #(number_of_symbol + number_of_symbol_prevous)
                """RENEMBER EVERYTHING IS COLLOR NOT THE DRAWLING
                
                18 / 16 = 1.125
                
                16 * .125 = 2
                
                Maybe use that  ( % because 18 % 16 = 2)
                
                """
                texture_counter_increaser = 1
                texture_counter += texture_counter_increaser  #(number_of_symbol / TEXTURE_SIZE)
                if texture_counter  >= (TEXTURE_SIZE): 
                    texture_counter = 0
                temp_depth_range_counter += 1
            if pixel_y_pozition == 0:
                print()
            #int(texture_counter)      
            number_of_symbol_prevous +=  result[where_and_how_much + 1]
    pygame.display.flip()
    
pygame.draw.rect(win, (100, 100, 100), (480, SCREEN_HEIGHT / 2, SCREEN_HEIGHT, SCREEN_HEIGHT))
pygame.draw.rect(win, (200, 200, 200), (480, -SCREEN_HEIGHT / 2, SCREEN_HEIGHT, SCREEN_HEIGHT))
ray_casting()
input("Contenu? ")
