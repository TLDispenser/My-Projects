import pygame
import math
import numpy as np

#models
print("Importing modles.... (Might take a while)")
from model import MODLES
print("DONE!")
#modles

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("3D Rendering Engine")

# Colors
invert_colors = False
if invert_colors:
    WHITE = (0, 0, 0)
    BLACK = (255, 255, 255)
else:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
# Darkning effect
DARKENING_FACTOR = 50

# Show edges?
show_edges = False

class Object:
    # Initialize vertices, edges, and faces
    def __init__(self, shape):
        self.vertices = []
        self.edges = []
        self.faces = []
        self.pivot = (0, 0, 0)
        if shape is None:
            self.import_shape_from_file()
        else:
            self.vertices = MODLES[shape]["vertices"]
            self.edges = MODLES[shape]["edges"]
            self.faces = MODLES[shape]["faces"]
            self.pivot = MODLES[shape]["pivot"]
        
            
    
    def import_shape_from_file(self):
        
        while True:
            print("Available shapes:")
            for key in MODLES.keys():
                print(key)
            input_model = input("Enter the model you want to import: ")
            if input_model in MODLES:
                self.vertices = MODLES[input_model]["vertices"]
                self.edges = MODLES[input_model]["edges"]
                self.faces = MODLES[input_model]["faces"]
                self.pivot = MODLES[input_model]["pivot"]
                break
            else:
                print("Model not found.")

DICT = {
    'square': {
        'object': Object('square'),
        'hp': 100,
        'speed': 10
    },
    'Chat_GPT_dog': {
        'object': Object('Chat_GPT_dog'),
        'hp': 80,
        'attack': 15
    },
    'octahedron': {
        'object': Object('octahedron'),
        'hp': 120,
        'attack': 5
    }
}
# Initialize the shape
working_shape = Object(None)
vertices = working_shape.vertices
edges = working_shape.edges
faces = working_shape.faces
pivot = working_shape.pivot


def project(x, y, z, scale, distance):
    factor = scale / (distance + z)
    x = x * factor + WIDTH // 2
    y = -y * factor + HEIGHT // 2
    return int(x), int(y)

# Draw faces and edges (sometimes)
def draw_faces_and_edges(transformed_vertices):
    # Calculate the average depth of each face
    face_depths = []
    for face in faces:
        vertices_indices, color = face
        avg_depth = np.mean([transformed_vertices[i][2] for i in vertices_indices])
        face_depths.append((avg_depth, face))
    
    # Sort faces by depth (furthest to closest)
    face_depths.sort(reverse=True, key=lambda x: x[0])
    
    # Draw faces in sorted order
    for depth, face in face_depths:
        vertices_indices, color = face
        points = [project(*transformed_vertices[i], 400, 4) for i in vertices_indices]
        
        # Darken the color based on depth
        darken_factor = max(0, min(1, 1 - depth / DARKENING_FACTOR))  # Adjust the divisor to control the darkening effect
        darkened_color = tuple(int(c * darken_factor) for c in color)
        
        pygame.draw.polygon(screen, darkened_color, points)

    if show_edges:    
        # Calculate the average depth of each edge
        edge_depths = []
        for edge in edges:
            avg_depth = np.mean([transformed_vertices[i][2] for i in edge])
            edge_depths.append((avg_depth, edge))
        
        # Sort edges by depth (furthest to closest)
        edge_depths.sort(reverse=True, key=lambda x: x[0])

        # Draw edges in sorted order 
        for _, edge in edge_depths:
            points = []
            for vertex in edge:
                x, y, z = transformed_vertices[vertex]
                points.append(project(x, y, z, 400, 4))   
            pygame.draw.line(screen, WHITE, points[0], points[1], 1)
        # Draw a small circle at each vertex
        for vertex in range(len(vertices)):
            x, y, z = transformed_vertices[vertex]
            screen_x, screen_y = project(x, y, z, 400, 4)
            pygame.draw.circle(screen, WHITE, (screen_x, screen_y), 6)
            # Draw the index of the vertice
            vector_font = pygame.font.SysFont('Arial', 16)
            vector_number = vector_font.render(str(vertex), True, (255, 0, 0))  # Red color for visibility
            screen.blit(vector_number, (screen_x - 5, screen_y - 5))

        


def main():
    
    global vertices
    global edges
    global faces
    global pivot
    
    clock = pygame.time.Clock()
    angle_x = 0
    angle_y = 0
    angle_z = 0
    pos_x = 0
    pos_y = 0
    pos_z = 0
    running = True
    can_move = True
    can_rotate = True
    
    
    while running:
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
                if event.key == pygame.K_m:
                    global show_edges
                    show_edges = not show_edges
                #if event.key == pygame.K_r:
                    
        # Continuous input
        keys = pygame.key.get_pressed()
        if can_rotate:
            if keys[pygame.K_LEFT]:
                angle_y -= 0.1
            if keys[pygame.K_RIGHT]:
                angle_y += 0.1
            if keys[pygame.K_UP]:
                angle_x -= 0.1
            if keys[pygame.K_DOWN]:
                angle_x += 0.1
            if keys[pygame.K_e]:
                angle_z -= 0.1
            if keys[pygame.K_q]:
                angle_z += 0.1  
        speed = 0.1
        if keys[pygame.K_LSHIFT]:
            speed = 0.5    
        if can_move:
            if keys[pygame.K_s]:
                pos_z -= speed
            if keys[pygame.K_w]:
                pos_z += speed
            if keys[pygame.K_a]:
                pos_x -= speed
            if keys[pygame.K_d]:
                pos_x += speed
            if keys[pygame.K_SPACE]:
                pos_y += speed
            if keys[pygame.K_c]:
                pos_y -= speed

        
            # Mouse input
            # Color change the clicked face closest to the camera
            if pygame.mouse.get_pressed()[0]:
                touching_face = []
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i, face in enumerate(faces):
                    vertices_indices, color = face
                    points = [project(*transformed_vertices[j], 400, 4) for j in vertices_indices]
                    polygon = pygame.draw.polygon(screen, color, points)
                    if polygon.collidepoint(mouse_x, mouse_y):
                        touching_face.append((vertices_indices, color))
                if touching_face:
                    face_depths = []
                    for face in touching_face:
                        vertices_indices, color = face
                        avg_depth = np.mean([transformed_vertices[i][2] for i in vertices_indices])
                        face_depths.append((avg_depth, face))
                    # Sort faces by depth (closest to furthest)
                    face_depths.sort(key=lambda x: x[0])
                    vertices_indices, color = face_depths[0][1]
                    points = [project(*transformed_vertices[i], 400, 4) for i in vertices_indices]
                    polygon = pygame.draw.polygon(screen, color, points)
                    
                    while True:
                        try:
                            new_color = (0,255,0)#eval(input("Enter the new color for the face (r, g, b): "))
                            face_index = faces.index(face_depths[0][1])
                            working_shape.faces[face_index] = (vertices_indices, new_color)
                            faces = working_shape.faces[:]
                            break
                        except Exception as e:
                            print(f"Error: {e}")
                                
            
        
        screen.fill(BLACK)
        pygame.draw.rect(screen, (0, 255, 0), (0, HEIGHT // 2, WIDTH, HEIGHT // 2))
        
        
        # Rotate 
        cos_angle_x = math.cos(angle_x)
        sin_angle_x = math.sin(angle_x)
        cos_angle_y = math.cos(angle_y)
        sin_angle_y = math.sin(angle_y)
        cos_angle_z = math.cos(angle_z)
        sin_angle_z = math.sin(angle_z)

        transformed_vertices = []
        for x, y, z in vertices:
            # Translate to pivot
            x -= pivot[0]
            y -= pivot[1]
            z -= pivot[2]
            # Rotate around x-axis
            y, z = y * cos_angle_x - z * sin_angle_x, z * cos_angle_x + y * sin_angle_x
            # Rotate around y-axis
            x, z = x * cos_angle_y - z * sin_angle_y, z * cos_angle_y + x * sin_angle_y
            # Rotate around z-axis
            x, y = x * cos_angle_z - y * sin_angle_z, y * cos_angle_z + x * sin_angle_z
            # Translate back from pivot
            x += pivot[0] + pos_x
            y += pivot[1] + pos_y
            z += pivot[2] + pos_z
            
            transformed_vertices.append((x, y, z))
        
        prevous_x, prevous_y, prevous_z = pos_x, pos_y, pos_z
        # Move the pivot
        if prevous_x != pos_x or prevous_y != pos_y or prevous_z != pos_z:
            pivot = (pivot[0] + pos_x, pivot[1] + pos_y, pivot[2] + pos_z)
        
        
        draw_faces_and_edges(transformed_vertices)

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
