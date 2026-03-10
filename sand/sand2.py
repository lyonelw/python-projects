import pygame
import random
import math

pygame.init()

grain_size = 20
brush = 1

width = 600
height = 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
placing = False
added = False
grains = []
grain_set = set()
colors = []
randcolors = [
    (210, 180, 80),
    (220, 190, 90),
    (230, 200, 100),
    (200, 170, 70),
    (215, 185, 75),
    (240, 210, 110),
    (205, 175, 65),
    (225, 195, 85),
]
preset = "big"
if preset == "small":
    grain_size = 40
    brush = 1
elif preset == "medium":
    grain_size = 10
    brush = 5
elif preset == "big":
    grain_size = 2
    brush = 10
#for i in range(0, 400):
#    grains.append((i, 399))
while running:
    
    randcolor = random.choice(randcolors)
    screen.fill((20, 20, 30))
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            width, height = event.size
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                grains = []
                colors = []
                grain_set = set()
            if event.key == pygame.K_UP:
                circlerad+=grain_size
            if event.key == pygame.K_DOWN:
                circlerad-=grain_size
        if event.type == pygame.MOUSEBUTTONDOWN:
            placing = True
        if event.type == pygame.MOUSEBUTTONUP:
            placing = False
    new_grains = []
    circle = []
    if placing:
        pos = pygame.mouse.get_pos()
        pos = (pos[0]//grain_size*grain_size, pos[1]//grain_size*grain_size)
        for i in range(10):
            j = random.randint(-grain_size*brush, grain_size*brush)
            k = random.randint(-grain_size*brush, grain_size*brush)
            circle.append((pos[0]+j//grain_size * grain_size, pos[1]+k//grain_size * grain_size))
        for point in circle:
            if point not in grains:
                grains.append(point)
                grain_set.add(point)
                colors.append(randcolor)
    for i, (x, y) in enumerate(grains):
        screen.fill(colors[i], ((x, y), (grain_size, grain_size)))
        new_y = y+grain_size
        target_pos = ((x, new_y))
        if y < height-grain_size:
            if target_pos not in grain_set:
                new_grains.append((x, new_y))
                grain_set.remove((x, y))
                grain_set.add((x, new_y))
                #colors.append(randcolor)
            #check if grain index is odd or even to determine which side to check first
            elif (x-grain_size, new_y) not in grain_set and x > 0:
                new_grains.append((x-grain_size, new_y))
                grain_set.remove((x, y))
                grain_set.add((x-grain_size, new_y))
                colors.append(randcolor)
            elif (x+grain_size, new_y) not in grain_set and x < width-grain_size:
                new_grains.append((x+grain_size, new_y))
                grain_set.remove((x, y))
                grain_set.add((x+grain_size, new_y))
                colors.append(randcolor)
            else:
                new_grains.append((x, y))
                #colors.append(randcolor)
        else:
            new_grains.append((x, y))
            #colors.append(randcolor)
    grains = new_grains
    pygame.display.flip()
    clock.tick(100)
pygame.quit()