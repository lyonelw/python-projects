import pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
running = True
grains = []
for i in range(0, 400):
    grains.append((i, 399))
while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            grains.append(pos)
    new_grains = []
    for x, y in grains:
        screen.fill("yellow", ((x, y), (1, 1)))
        new_y = y+1
        target_pos = ((x, new_y))
        #if target_pos not in grains:
        if y < 399:
            new_grains.append((x, new_y))
        if target_pos not in grains:
            new_grains.append((x, new_y))
        else:
            new_grains.append((x, y))
    grains = new_grains

    pygame.display.flip()
    clock.tick(60)

pygame.quit()