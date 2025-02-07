import pygame
import sys
import math
import numpy as np
import pygame.gfxdraw

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
# Rendering distance
RENDER_DISTANCE = 30


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
        'render': True,
        'move': True,
        'collision': True,
        'start_pos': (0, 0, 0)
    },
    'bulbasaur': {
        'object_class': Object('bulbasaur'),
        'render': False,
        'move': False,
        'collision': False,
        'start_pos': (-3, 0, 0)
    },
    'octahedron': {
        'object_class': Object('octahedron'),
        'render': True,
        'move': False,
        'collision': True,
        'start_pos': (3, 0, 0)
    }
}
class Cam:
    def __init__(self, pos=(0, 0, 0), rot=(0, 0)):
        self.pos = list(pos)
        self.rot = list(rot)

    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            x, y = event.rel
            x /= 200
            y /= 200
            self.rot[0] += y
            self.rot[1] += x

    def update(self, dt, key):
        s = dt * 10

        if key[pygame.K_c]:
            self.pos[1] += s
        if key[pygame.K_SPACE]:
            self.pos[1] -= s

        x, y = s * math.sin(self.rot[1]), s * math.cos(self.rot[1])

        if self.rot[0] <= -1.58:
            self.rot[0] = -1.58

        if self.rot[0] >= 1.58:
            self.rot[0] = 1.58

        if key[pygame.K_w]:
            self.pos[0] += x
            self.pos[2] += y
        if key[pygame.K_s]:
            self.pos[0] -= x
            self.pos[2] -= y
        if key[pygame.K_a]:
            self.pos[0] -= y
            self.pos[2] += x
        if key[pygame.K_d]:
            self.pos[0] += y
            self.pos[2] -= x

        if key[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()  # Quits Game#

    def transform(self, vertices):
        transformed_vertices = []
        cos_x, sin_x = math.cos(self.rot[0]), math.sin(self.rot[0])
        cos_y, sin_y = math.cos(self.rot[1]), math.sin(self.rot[1])
        for x, y, z in vertices:
            x -= self.pos[0]
            y -= self.pos[1]
            z -= self.pos[2]

            # Rotate around x-axis
            y, z = y * cos_x - z * sin_x, z * cos_x + y * sin_x
            # Rotate around y-axis
            x, z = x * cos_y - z * sin_y, z * cos_y + x * sin_y

            transformed_vertices.append((x, y, z))
        return transformed_vertices

def project(x, y, z, scale, distance, aspect_ratio):
    factor = scale / (distance + z)
    x = x * factor * aspect_ratio + WIDTH // 2
    y = -y * factor + HEIGHT // 2
    return int(x), int(y)


def calculate_position(obj_class, angle_x, angle_y, angle_z, pos_x, pos_y, pos_z, prevous_x, prevous_y, prevous_z):
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
        
        # Update pivot's position
        pivot = (obj_class.pivot[0] + pos_x, obj_class.pivot[1] + pos_y, obj_class.pivot[2] + pos_z)
            
        transformed_vertices.append((x, y, z))
    
    obj_class.update_object(transformed_vertices, obj_class.edges, obj_class.faces, pivot)
    
    return transformed_vertices

def sort_high_to_low(all_vertices, all_faces, camera_position, camera_front):
    sorted_faces = []
    for face in all_faces:
        vertices_indices, color = face
        try:
            # Ensure indices are within range
            if all(0 <= index < len(all_vertices) for index in vertices_indices):
                # Calculate the average depth of the face
                depth = sum(all_vertices[index][2] for index in vertices_indices) / len(vertices_indices)
                sorted_faces.append((depth, face))
        except IndexError:
            print(f"One of the indices in {vertices_indices} is out of range for transformed_vertices")
    
    # Sort faces by depth in descending order
    sorted_faces.sort(key=lambda x: x[0], reverse=True)
    return sorted_faces

def check_collision(obj1, obj2):
    (min_x1, max_x1), (min_y1, max_y1), (min_z1, max_z1) = obj1.get_bounding_box()
    (min_x2, max_x2), (min_y2, max_y2), (min_z2, max_z2) = obj2.get_bounding_box()

    return (min_x1 <= max_x2 and max_x1 >= min_x2 and
            min_y1 <= max_y2 and max_y1 >= min_y2 and
            min_z1 <= max_z2 and max_z1 >= min_z2)

def draw_faces(all_vertices, sorted_faces, aspect_ratio):
    for depth, face in sorted_faces:
        vertices_indices, color = face
        points = [project(all_vertices[i][0], all_vertices[i][1], all_vertices[i][2], 400, 4, aspect_ratio) for i in vertices_indices]
        
        # Darken the color based on depth
        darken_factor = max(0, min(1, 1 - depth / DARKENING_FACTOR))  # Adjust the divisor to control the darkening effect
        darkened_color = tuple(int(c * darken_factor) for c in color)
        
        try:
            vertices_indices[0] = float(vertices_indices[0])
            if isinstance(vertices_indices[0], float):
                pygame.draw.polygon(screen, darkened_color, points)
        except Exception:
            print(f"Error drawing polygon with points: {points}")

def main():
    global screen
    clock = pygame.time.Clock()
    
    collisions_on = True
    running = True
    can_move = True
    can_rotate = True

    # Define the camera's position and front vector
    camera_position = np.array([0, 0, -5])
    camera_front = np.array([0, 0, 1])
    
    cam = Cam((0, 0, -5))
    pygame.event.get()
    pygame.mouse.get_rel()
    pygame.mouse.set_visible(0)
    pygame.event.set_grab(1)
    
    # Updates the start position of the objects
    for obj_name, obj in DICT.items():
        calculate_position(obj['object_class'], 0, 0, 0, *obj['start_pos'], 0, 0, 0)

    while running:
        dt = clock.tick() / 1000
        
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
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            cam.events(event)
        
        keys = pygame.key.get_pressed()
        cam.update(dt, keys)
        
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

        # Previous position
        prevous_x, prevous_y, prevous_z = pos_x, pos_y, pos_z

        # Check for collisions
        if collisions_on:
            for obj_name1, obj1 in DICT.items():
                for obj_name2, obj2 in DICT.items():
                    if obj_name1 != obj_name2 and obj1['collision'] and obj2['collision']:
                        if check_collision(obj1['object_class'], obj2['object_class']):
                            # Reset position of the colliding objects
                            obj1['object_class'].update_object(obj1['object_class'].vertices, obj1['object_class'].edges, obj1['object_class'].faces, obj1['object_class'].pivot)
                            obj2['object_class'].update_object(obj2['object_class'].vertices, obj2['object_class'].edges, obj2['object_class'].faces, obj2['object_class'].pivot)
                            # Reset position of moving objects
                            if obj1['move'] or obj2['move']:
                                pos_x, pos_y, pos_z = -1.1 * prevous_x, -1.1 * prevous_y, -1.1 * prevous_z
                                calculate_position(obj1['object_class'], angle_x, angle_y, angle_z, pos_x, pos_y, pos_z, prevous_x, prevous_y, prevous_z)

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

        # Transform vertices based on camera position and rotation
        transformed_vertices = cam.transform(all_vertices)

        # Sort faces by dot product with camera's front vector
        sorted_faces = sort_high_to_low(transformed_vertices, all_faces, camera_position, camera_front)
        
        # Calculate aspect ratio
        aspect_ratio = pygame.display.get_surface().get_width() / pygame.display.get_surface().get_height()

        # Draw all faces
        draw_faces(transformed_vertices, sorted_faces, aspect_ratio)

        # See FPS
        fps = str(int(clock.get_fps()))
        font = pygame.font.SysFont('Arial', 30)
        fpssurface = font.render(fps, False, (255, 255, 255))
        screen.blit(fpssurface, (0, 0))

        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()

if __name__ == "__main__":
    main()
