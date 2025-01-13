import random
# Example: 3D array representing voxels
world = [[[0 for z in range(10)] for y in range(10)] for x in range(10)]  
# 0 represents an empty voxel (air)
for x in range(10):
    for y in range(10):
        for z in range(10):
            world[x][y][z] = 0 #random.randint(0, 10)
world[0][0][0] = 1
print(world)
import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_world(world):
    screen.fill(BLACK)
    size = len(world)
    
    for x in range(size):
        for y in range(size):
            for z in range(size):
                if world[x][y][z] == 1:
                    pygame.draw.rect(screen, WHITE, (x * 10, y * 10, 10, 10))
                    
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_world(world)
    draw_world(world)
    




pygame.quit()
