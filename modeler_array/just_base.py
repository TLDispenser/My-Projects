testing_one = False

import pygame
import math
import numpy as np

# models
print("Importing models.... (Might take a while)")
from model import MODLES
print("DONE!")
# models

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("3D Rendering Engine")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Darkening effect
DARKENING_FACTOR = 50


class Object:
    # Initialize vertices, edges, and faces
    def __init__(self, shape):
        print("intializing object: " + shape)
        self.vertices = MODLES[shape]["vertices"]
        self.edges = MODLES[shape]["edges"]
        self.faces = MODLES[shape]["faces"]
        self.pivot = MODLES[shape]["pivot"]
        self.get_bounding_box()

    def __str__(self):
        return f"Object({self.vertices}, {self.edges}, {self.faces}, {self.pivot})"

    def __repr__(self):
        return f"Object({self.vertices}, {self.edges}, {self.faces}, {self.pivot})"

    def get_bounding_box(self):
        min_x = min(v[0] for v in self.vertices)
        max_x = max(v[0] for v in self.vertices)
        min_y = min(v[1] for v in self.vertices)
        max_y = max(v[1] for v in self.vertices)
        min_z = min(v[2] for v in self.vertices)
        max_z = max(v[2] for v in self.vertices)
        self.bounding_box = (min_x, max_x), (min_y, max_y), (min_z, max_z)
        return self.bounding_box

    def update_object(self, vertices, edges, faces, pivot):
        self.vertices = vertices
        self.edges = edges
        self.faces = faces
        self.pivot = pivot

# Dictionary of objects
DICT = {
    'square': {
        'object_class': Object('square'),
        'render': False,
        'move': False
    },
    'Chat_GPT_dog': {
        'object_class': Object('bulbasaur'),
        'render': True,
        'move': True
    },
    'octahedron': {
        'object_class': Object('octahedron'),
        'render': True,
        'move': False
    }
}


def project(x, y, z, scale, distance):
    factor = scale / (distance + z)
    x = x * factor + WIDTH // 2
    y = -y * factor + HEIGHT // 2
    return int(x), int(y)


def draw_faces(all_vertices, sorted_faces):
    for depth, face in sorted_faces:
        vertices_indices, color = face
        points = [project(all_vertices[i][0], all_vertices[i][1], all_vertices[i][2], 400, 4) for i in vertices_indices]
        
        # Darken the color based on depth
        darken_factor = max(0, min(1, 1 - depth / DARKENING_FACTOR))  # Adjust the divisor to control the darkening effect
        darkened_color = tuple(int(c * darken_factor) for c in color)

        pygame.draw.polygon(screen, darkened_color, points)


def calculate_position(obj_class, angle_x, angle_y, angle_z, pos_x, pos_y, pos_z, prevous_x, prevous_y, prevous_z):
    # Rotate
    cos_angle_x = math.cos(angle_x)
    sin_angle_x = math.sin(angle_x)
    cos_angle_y = math.cos(angle_y)
    sin_angle_y = math.sin(angle_y)
    cos_angle_z = math.cos(angle_z)
    sin_angle_z = math.sin(angle_z)

    transformed_vertices = []
    for x, y, z in obj_class.vertices:
        # Translate to pivot
        x -= obj_class.pivot[0]
        y -= obj_class.pivot[1]
        z -= obj_class.pivot[2]
        
        # Rotate around x-axis
        y, z = y * cos_angle_x - z * sin_angle_x, z * cos_angle_x + y * sin_angle_x
        # Rotate around y-axis
        x, z = x * cos_angle_y - z * sin_angle_y, z * cos_angle_y + x * sin_angle_y
        # Rotate around z-axis
        x, y = x * cos_angle_z - y * sin_angle_z, y * cos_angle_z + x * sin_angle_z
        
        # Apply position offsets
        x += obj_class.pivot[0] + pos_x
        y += obj_class.pivot[1] + pos_y
        z += obj_class.pivot[2] + pos_z
        
        
        # Move the pivot
        if prevous_x != pos_x or prevous_y != pos_y or prevous_z != pos_z:
            pivot = (obj_class.pivot[0] + pos_x, obj_class.pivot[1] + pos_y, obj_class.pivot[2] + pos_z)
        else:
            pivot = obj_class.pivot
            
        transformed_vertices.append((x, y, z))
    
    obj_class.update_object(transformed_vertices, obj_class.edges, obj_class.faces, pivot)
    
    return transformed_vertices




def sort_high_to_low(all_vertices, all_faces, camera_position, camera_front):
    sorted_faces = []
    for face in all_faces:
        vertices_indices, color = face
        try:
            # Calculate the centroid of the face
            centroid = np.mean([all_vertices[i] for i in vertices_indices], axis=0)
            # Calculate the vector from the camera to the centroid
            vector_to_centroid = centroid - camera_position
            # Calculate the dot product with the camera's front vector
            dot_product = np.dot(vector_to_centroid, camera_front)
        except IndexError:
            print(f"IndexError: One of the indices in {vertices_indices} is out of range for transformed_vertices")
            continue
        sorted_faces.append((dot_product, face))
    sorted_faces.sort(reverse=True, key=lambda x: x[0])
    return sorted_faces


def check_collision(obj1, obj2):
    (min_x1, max_x1), (min_y1, max_y1), (min_z1, max_z1) = obj1.get_bounding_box()
    (min_x2, max_x2), (min_y2, max_y2), (min_z2, max_z2) = obj2.get_bounding_box()

    return (min_x1 <= max_x2 and max_x1 >= min_x2 and
            min_y1 <= max_y2 and max_y1 >= min_y2 and
            min_z1 <= max_z2 and max_z1 >= min_z2)


def main():
    clock = pygame.time.Clock()
    
    collisions_on = True
    running = True
    can_move = True
    can_rotate = True

    # Define the camera's position and front vector
    camera_position = np.array([0, 0, -5])
    camera_front = np.array([0, 0, 1])
    
    while running:
        # Reset values to prevent continuous movement
        angle_x = 0
        angle_y = 0
        angle_z = 0
        pos_x = 0
        pos_y = 0
        pos_z = 0
        
        # Single input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                global WIDTH, HEIGHT
                WIDTH, HEIGHT = event.size
                global screen
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_r:
                    print("Collision detection is now", not collisions_on)
                    collisions_on = not collisions_on
                if event.key == pygame.K_t:
                    # DEBUG: Prints every object's bounding box
                    for obj_name, obj in DICT.items():
                        print(f"{obj_name}: {obj['object_class'].get_bounding_box()}")
                    input("Press Enter to continue...")
                    
        # Previous position
        prevous_x, prevous_y, prevous_z = pos_x, pos_y, pos_z
                
        # Continuous input
        keys = pygame.key.get_pressed()
        if can_rotate:
            rotation_speed = 0.05
            if keys[pygame.K_LEFT] and not keys[pygame.K_LCTRL]:
                angle_y -= rotation_speed
            if keys[pygame.K_RIGHT] and not keys[pygame.K_LCTRL]:
                angle_y += rotation_speed
            if keys[pygame.K_UP] and not keys[pygame.K_LCTRL]:
                angle_x -= rotation_speed
            if keys[pygame.K_DOWN] and not keys[pygame.K_LCTRL]:
                angle_x += rotation_speed
            if keys[pygame.K_e]:
                angle_z -= rotation_speed
            if keys[pygame.K_q]:
                angle_z += rotation_speed
        move_speed = 0.1
        if keys[pygame.K_LSHIFT]:
            move_speed = 0.5
        if can_move:
            if keys[pygame.K_s]:
                pos_z -= move_speed
            if keys[pygame.K_w]:
                pos_z += move_speed
            if keys[pygame.K_a]:
                pos_x -= move_speed
            if keys[pygame.K_d]:
                pos_x += move_speed
            if keys[pygame.K_SPACE]:
                pos_y += move_speed
            if keys[pygame.K_c]:
                pos_y -= move_speed

        # Camera movement
        camera_move_speed = 0.1
        if keys[pygame.K_LCTRL]:
            if keys[pygame.K_LEFT]:
                camera_position[0] -= camera_move_speed
            if keys[pygame.K_RIGHT]:
                camera_position[0] += camera_move_speed
            if keys[pygame.K_UP]:
                camera_position[1] += camera_move_speed
            if keys[pygame.K_DOWN]:
                camera_position[1] -= camera_move_speed

        screen.fill(BLACK)
        pygame.draw.rect(screen, (0, 255, 0), (0, HEIGHT // 2, WIDTH, HEIGHT // 2))
 
        
        # NOT WORKING !!!!!!!!!!!!!!!!
        # Check for collisions
        if collisions_on:
            for obj_name1, obj1 in DICT.items():
                for obj_name2, obj2 in DICT.items():
                    if obj1['render'] and obj2['render']:
                        if obj_name1 != obj_name2:
                            if check_collision(obj1['object_class'], obj2['object_class']):
                                #print(f"Collision detected between {obj_name1} and {obj_name2}")
                                pos_x, pos_y, pos_z = prevous_x, prevous_y, prevous_z
 
        
        all_vertices = []
        all_faces = []
        vertex_offset = 0
        for obj_name, obj in DICT.items():
            if obj['render']:
                obj_class = obj['object_class']
                if obj['move']:
                    calculate_position(obj_class, angle_x, angle_y, angle_z, pos_x, pos_y, pos_z, prevous_x, prevous_y, prevous_z)
                all_vertices += obj_class.vertices
                for face in obj_class.faces:
                    vertices_indices, color = face
                    adjusted_indices = [index + vertex_offset for index in vertices_indices]
                    all_faces.append((adjusted_indices, color))
                vertex_offset += len(obj_class.vertices)
        
        # Sort faces by dot product with camera's front vector
        sorted_faces = sort_high_to_low(all_vertices, all_faces, camera_position, camera_front)

        # Draw all faces
        draw_faces(all_vertices, sorted_faces)


        # See FPS
        fps = str(int(clock.get_fps()))
        font = pygame.font.SysFont('Arial', 30)
        fpssurface = font.render(fps, False, (255, 255, 255))
        screen.blit(fpssurface, (0, 0))

        if testing_one:
            running = False
        
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()


if __name__ == "__main__":
    main()
