import pygame
import random
import math

pixel_size = 100
width = 600
height = 600
fps = 60
refresh = 10
frame = 0
generation = 0
screen = pygame.display.set_mode((width, height))
pygame.init()
pygame.font.init()
pygame.display.set_caption("thta's life")

clock = pygame.time.Clock()
running = True
placing = False
playing = False
pixels = []
colors = []
#EITHER COLOR, GRAY, OR WHITE
color_scheme = "yellow"
pixel_set = set()
while running:
    screen.fill((25, 25, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            placing = True
        if event.type == pygame.MOUSEBUTTONUP:
            placing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    playing = False
                else:
                    playing = True
            if event.key == pygame.K_c:
                pixels = []
                colors = []
                generation = 0
                pixel_set = set()
    if placing:
        x,y = pygame.mouse.get_pos()
        pixels.append((x//pixel_size*pixel_size, y//pixel_size*pixel_size))
        if color_scheme == "color":
            colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        elif color_scheme == "gray":
            gray = random.randint(150, 255)
            colors.append((gray, gray, gray))
        else:
            colors.append(color_scheme)
        pixel_set.add((x//pixel_size*pixel_size, y//pixel_size*pixel_size))
    for i in range(width//pixel_size):
        pygame.draw.line(screen, (20, 20, 20), (i* pixel_size-1, 0), (i*pixel_size-1, height))
    for i in range(height//pixel_size):
        pygame.draw.line(screen, (20, 20, 20), (0, i * pixel_size-1), (width, i*pixel_size-1))
    for i, pixel in enumerate(pixels):
        screen.fill(colors[i], (pixel, (pixel_size, pixel_size)))
    if playing:
        frame += 1
        if frame >= fps/refresh:
            next_pixels = []
            removals = []
            additions = []
            generation += 1
            for i in range(width//pixel_size):
                #i 0 -> 10
                for j in range(height//pixel_size):
                    #j 0 -> 10
                    #print(f"{pixel_set} |||| {i*pixel_size} {j*pixel_size}")
                    neighbors = 0
                    x = i*pixel_size
                    y = j*pixel_size
                    #top left
                    if ((x-pixel_size, y-pixel_size)) in pixel_set:
                        neighbors+=1
                    #top middle
                    if ((x, y-pixel_size)) in pixel_set:
                        neighbors+=1
                    #top right
                    if ((x+pixel_size, y-pixel_size)) in pixel_set:
                        neighbors+=1
                    #middle left
                    if ((x-pixel_size, y)) in pixel_set:
                        neighbors+=1
                    #middle right
                    if (x+pixel_size, y) in pixel_set:
                        neighbors+=1
                    #bottom left
                    if (x-pixel_size, y+pixel_size) in pixel_set:
                        neighbors+=1
                    #bottom middle
                    if (x, y+pixel_size) in pixel_set:
                        neighbors+=1
                    #bottom right
                    if (x+pixel_size, y+pixel_size) in pixel_set:
                        neighbors+=1
                    #logic
                    if neighbors == 3 and ((x, y)) not in pixel_set:
                        next_pixels.append((x, y))
                        if color_scheme == "color":
                            colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                        elif color_scheme == "gray":
                            gray = random.randint(150, 255)
                            colors.append((gray, gray, gray))
                        else:
                            colors.append(color_scheme)
                    if (neighbors == 3 or neighbors == 2) and ((x, y)) in pixel_set:
                        next_pixels.append((x, y))
                        if color_scheme == "color":
                            colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                        elif color_scheme == "gray":
                            gray = random.randint(150, 255)
                            colors.append((gray, gray, gray))
                        else:
                            colors.append(color_scheme)
            pixel_set = set(next_pixels)
            pixels = next_pixels
            frame = 0
        #generation counter
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"gen {generation}", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip()
    clock.tick(fps)