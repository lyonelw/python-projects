import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
anglex = 0
angley = 0

#cube
shape = [(-0.5,-0.5,-0.5),(0.5,-0.5,-0.5),(-0.5,0.5,-0.5),(0.5,0.5,-0.5),(0.5,0.5,0.5),(0.5,-0.5,0.5),(-0.5,-0.5,0.5),(-0.5,0.5,0.5)]
edges = [(0,1), (1,3), (3,2), (2,0), (4,5), (5,6), (6,7), (7,4), (0,6), (1,5), (2,7), (3,4)]

#triangle
shape = [(-0.5, -0.5, 0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0, 0.5, 0)]
edges = [(0,1), (0,2), (1,3), (1,4), (0,4), (2,4), (2,3), (3,4)]

#dodecahedron
shape = [(-0.92, -0.92, -0.92),
    (-0.92, -0.92,  0.92),
    (-0.92,  0.92, -0.92),
    (-0.92,  0.92,  0.92),
    ( 0.92, -0.92, -0.92),
    ( 0.92, -0.92,  0.92),
    ( 0.92,  0.92, -0.92),
    ( 0.92,  0.92,  0.92),

    (0, -0.5686, -1.4886),
    (0, -0.5686,  1.4886),
    (0,  0.5686, -1.4886),
    (0,  0.5686,  1.4886),

    (-0.5686, -1.4886, 0),
    (-0.5686,  1.4886, 0),
    ( 0.5686, -1.4886, 0),
    ( 0.5686,  1.4886, 0),

    (-1.4886, 0, -0.5686),
    (-1.4886, 0,  0.5686),
    ( 1.4886, 0, -0.5686),
    ( 1.4886, 0,  0.5686)]  # 19
edges = [(0,1),(0,2),(0,8),
    (1,3),(1,9),
    (2,3),(2,10),
    (3,11),

    (4,5),(4,6),(4,8),
    (5,7),(5,9),
    (6,7),(6,10),
    (7,11),

    (8,16),(8,18),
    (9,17),(9,19),
    (10,16),(10,18),
    (11,17),(11,19),

    (12,13),(12,14),
    (13,15),(14,15),

    (12,16),(13,17),
    (14,18),(15,19)]
while running:
    anglex += 0.01
    angley += 0.02
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mx = pygame.mouse.get_pos()
            anglex = -mx[0]/100
            angley = -mx[1]/100
        #movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                for i in range(len(shape)):
                    print("forward")
                    x,y,z = shape[i]
                    z -= 0.1
                    shape[i] = (x,y,z)
            if event.key == pygame.K_s:
                print("backward")
                for i in range(len(shape)):
                    x,y,z = shape[i]
                    z += 0.1
                    shape[i] = (x,y,z)

    projected_points = []
    for x, y, z in shape:
        # XAxis Rotation
        ry = y * math.cos(angley) - z * math.sin(angley)
        rz = y * math.sin(angley) + z * math.cos(angley)
        #Y axis rotation
        rx = x * math.cos(anglex) + rz * math.sin(anglex)
        rz = x * -math.sin(anglex) + rz * math.cos(anglex)

        z_depth = rz + 4
        f_length = 600
        
        px = (rx * f_length) / z_depth + 640 
        py = (ry * f_length) / z_depth + 360
        projected_points.append((px, py))
    #for i in range(len(projected_points)):
    #    pygame.draw.circle(screen, "white", projected_points[i], 5)
    for edge in edges:
        pygame.draw.line(screen, "white", projected_points[edge[0]], projected_points[edge[1]], 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()