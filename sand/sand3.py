import pygame
import random

pygame.init()

WIDTH = 1920
HEIGHT = 1080
GRAIN_SIZE = 10
COLS = WIDTH // GRAIN_SIZE
ROWS = HEIGHT // GRAIN_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("sand project")
clock = pygame.time.Clock()

grid = [[0] * ROWS for _ in range(COLS)]
color_grid = [[(0, 0, 0)] * ROWS for _ in range(COLS)]

SAND_COLORS = [
    (210, 180, 80),
    (220, 190, 90),
    (230, 200, 100),
    (200, 170, 70),
    (215, 185, 75),
    (240, 210, 110),
    (205, 175, 65),
    (225, 195, 85),
]

def place_sand(px, py):
    gx = px // GRAIN_SIZE
    gy = py // GRAIN_SIZE
    if 0 <= gx < COLS and 0 <= gy < ROWS and grid[gx][gy] == 0:
        grid[gx][gy] = 1
        color_grid[gx][gy] = random.choice(SAND_COLORS)

def update_grid():
    for y in range(ROWS - 2, -1, -1):
        # Shuffle x order to avoid directional bias
        xs = list(range(COLS))
        random.shuffle(xs)
        for x in xs:
            if grid[x][y] == 1:
                # Try to fall straight down
                if grid[x][y + 1] == 0:
                    grid[x][y + 1] = 1
                    color_grid[x][y + 1] = color_grid[x][y]
                    grid[x][y] = 0
                    color_grid[x][y] = (0, 0, 0)
                else:
                    # Try diagonal left or right (randomly pick order)
                    dirs = [-1, 1]
                    random.shuffle(dirs)
                    moved = False
                    for dx in dirs:
                        nx = x + dx
                        if 0 <= nx < COLS and grid[nx][y + 1] == 0:
                            grid[nx][y + 1] = 1
                            color_grid[nx][y + 1] = color_grid[x][y]
                            grid[x][y] = 0
                            color_grid[x][y] = (0, 0, 0)
                            moved = True
                            break

def draw_grid():
    screen.fill((50, 40, 80))
    for x in range(COLS):
        for y in range(ROWS):
            if grid[x][y] == 1:
                pygame.draw.rect(
                    screen,
                    color_grid[x][y],
                    (x * GRAIN_SIZE, y * GRAIN_SIZE, GRAIN_SIZE, GRAIN_SIZE)
                )

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            # Clear grid with C key
            grid = [[0] * ROWS for _ in range(COLS)]
            color_grid = [[(0, 0, 0)] * ROWS for _ in range(COLS)]
        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.size
    # Hold left mouse button to place sand
    if pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()
        # Place a small cluster for faster fill
        for _ in range(50):
            jx = mx + random.randint(-GRAIN_SIZE*15, GRAIN_SIZE*15)
            jy = my + random.randint(-GRAIN_SIZE*15, GRAIN_SIZE*15)
            place_sand(jx, jy)

    update_grid()
    draw_grid()
    pygame.display.flip()
    clock.tick(300)

pygame.quit()