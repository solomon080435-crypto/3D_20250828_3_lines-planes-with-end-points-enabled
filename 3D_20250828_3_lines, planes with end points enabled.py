# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 10:47:23 2025

@author: Solo
version info:
    modulized some thing, adding parameters for future use.
"""

import random
import pygame
import math



#game constants
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
skyblue = (140, 200, 255)
WIDTH = 1000         #changable
HEIGHT = 750        #changable

#game variables
score = 0
player_x = 0.0   #changable
player_y = 0.0   #changable
player_z = 0.0
player_a_hor = 0 #radians, player_Angle_horizontal
player_a_ver = 0 #radians, player_Angle_vertical
player_dx = 0.0
player_dy = 0.0
player_dz = 0.0
player_fb = 0 #velocity of front and back
player_lr = 0 #velocity of left and right
player_da_hor = 0.0
player_da_ver = 0.0
cos_a_v, cos_a_h = math.cos(player_a_ver), math.cos(player_a_hor)
sin_a_v, sin_a_h = math.sin(player_a_ver), math.sin(player_a_hor)
gravity = 1
obstacles = [300, 450, 600]
obstacle_speed = 2
active = False

visibility = 10000

#0: pos, 1:index = None, 2: color, 3: distance
row_pixels = (lambda n: [n for i in range(WIDTH)])([[0, 0], None, skyblue, visibility])
screen_pixels = (lambda n: [n for i in range(HEIGHT)])(row_pixels)
for i in range(HEIGHT):
    for j in range(WIDTH):
        screen_pixels[0] = [j - (WIDTH/2), (HEIGHT/2) - i]

#{index: 0: Dimensions, 1: infinite?, 2:color, 3: radius, 4: points pos sequence, 5: vector, 6:transparency}
#point: {index: 0: Dimensions = 0, 1: infinite? = 0, 2:color, 3: radius(not to scale), 4: points pos sequence(len = 1), 5: vector = (0, 0, 0), 6:transparency}
#line: {index: 0: Dimensions = 1, 1: infinite? = 0, 2:color, 3: radius(not to scale), 4: points pos sequence(len = 2), 5: vector = d, 6:transparency}
#infinite line: {index: 0: Dimensions = 1, 1: infinite? = 1, 2:color, 3: radius(not to scale), 4: points pos sequence(len = 2), 5: vector = d, 6:transparency}
#plane: {index: 0: Dimensions = 2, 1: infinite? = 0, 2:color, 3: radius = 0, 4: points pos sequence(sequential), 5: vector = n, 6:transparency}


elements_3D = {(2, 0): [2, 0, green, 0, [[100, 500, -100], [-100, 500, -100], [-100, -500, -100], [100, -500, -100]], (0, 0, 1), 255], 
               (0, 0): [0, 0, black, 10, [[100, 100, 100]], (0, 0, 0), 255], (0, 1): [0, 0, black, 10, [[-100, 100, 100]], (0, 0, 0), 255], (0, 2): [0, 0, black, 10, [[100, 100, -100]], (0, 0, 0), 255], (0, 3): [0, 0, black, 10, [[-100, 100, -100]], (0, 0, 0), 255], 
               (0, 4): [0, 0, black, 10, [[100, 200, 100]], (0, 0, 0), 255], (0, 5): [0, 0, black, 10, [[-100, 200, 100]], (0, 0, 0), 255], (0, 6): [0, 0, black, 10, [[100, 200, -100]], (0, 0, 0), 255], (0, 7): [0, 0, black, 10, [[-100, 200, -100]], (0, 0, 0), 255], 
               (0, 8): [0, 0, black, 10, [[100, 500, 100]], (0, 0, 0), 255], (0, 9): [0, 0, black, 10, [[-100, 500, 100]], (0, 0, 0), 255], (0, 10): [0, 0, black, 10, [[100, 500, -100]], (0, 0, 0), 255], (0, 11): [0, 0, black, 10, [[-100, 500, -100]], (0, 0, 0), 255], 
               (0, 12): [0, 0, black, 10, [[100, -500, 100]], (0, 0, 0), 255], (0, 13): [0, 0, black, 10, [[-100, -500, 100]], (0, 0, 0), 255], (0, 14): [0, 0, black, 10, [[100, -500, -100]], (0, 0, 0), 255], (0, 15): [0, 0, black, 10, [[-100, -500, -100]], (0, 0, 0), 255], 
               (0, 16): [0, 0, black, 10, [[100, -200, 100]], (0, 0, 0), 255], (0, 17): [0, 0, black, 10, [[-100, -200, 100]], (0, 0, 0), 255], (0, 18): [0, 0, black, 10, [[100, -200, -100]], (0, 0, 0), 255], (0, 19): [0, 0, black, 10, [[-100, -200, -100]], (0, 0, 0), 255], 
               (0, 20): [0, 0, black, 10, [[100, 0, 100]], (0, 0, 0), 255], (0, 21): [0, 0, black, 10, [[-100, 0, 100]], (0, 0, 0), 255], (0, 22): [0, 0, black, 10, [[100, 0, -100]], (0, 0, 0), 255], (0, 23): [0, 0, black, 10, [[-100, 0, -100]], (0, 0, 0), 255], 
               (0, 24): [0, 0, black, 10, [[100, 0, 0]], (0, 0, 0), 255], (0, 25): [0, 0, black, 10, [[-100, 0, 0]], (0, 0, 0), 255], (0, 26): [0, 0, black, 10, [[0, 0, -100]], (0, 0, 0), 255], (0, 27): [0, 0, black, 10, [[0, 0, 100]], (0, 0, 0), 255], 
               (0, 28): [0, 0, black, 10, [[0, 500, 0]], (0, 0, 0), 255], 
               (1, 0): [1, 0, red, 10, [[100, 500, 100], [100, -500, 100]], (0, -1000, 0), 255], 
               (1, 1): [1, 0, red, 10, [[-100, 500, 100], [-100, -500, 100]], (0, -1000, 0), 255], 
               (1, 2): [1, 0, red, 10, [[100, 500, -100], [100, -500, -100]], (0, -1000, 0), 255], 
               (1, 3): [1, 0, red, 10, [[-100, 500, -100], [-100, -500, -100]], (0, -1000, 0), 255], 
               (1, 4): [1, 0, red, 10, [[100, 0, 100], [100, 0, -100]], (0, 0, -200), 255], 
               (1, 5): [1, 0, red, 10, [[-100, 0, 100], [-100, 0, -100]], (0, 0, -200), 255], 
               (1, 6): [1, 0, red, 10, [[100, 0, 100], [-100, 0, 100]], (-200, 0, 0), 255], 
               (1, 7): [1, 0, red, 10, [[100, 0, -100], [-100, 0, -100]], (-200, 0, 0), 255], 
               }

elements_3D_rel = {}
elements_2D = {}
fov = 90
screen_distance = WIDTH/(2*math.tan(math.radians(fov/2)))

def pos_OnScreen(pos_2D):
    return [(WIDTH/2) + pos_2D[0], (HEIGHT/2) - pos_2D[1]]

def get_rel_element(element):
    points = list(map(get_rel_point_3D, element[4]))
    vector = get_rel_vector_3D(element[5])
    new_element = []
    new_element.extend(element[0:4])
    new_element.extend([points, vector, element[6]])
    return new_element

def get_rel_point_3D(point):
    global cos_a_v, cos_a_h
    global sin_a_v, sin_a_h
    global player_x, player_y, player_z
    rel_point0 = [point[0] - player_x, point[1] - player_y, point[2] - player_z]
    rel_point1 = [(rel_point0[0] * cos_a_h) - (rel_point0[1] * sin_a_h), (rel_point0[0] * sin_a_h) + (rel_point0[1] * cos_a_h), rel_point0[2]]
    rel_point2 = [rel_point1[0], (rel_point1[1] * cos_a_v) + (rel_point1[2] * sin_a_v), (rel_point1[1] * -sin_a_v) + (rel_point1[2] * cos_a_v)]
    distance_sqr = (rel_point2[0] ** 2) + (rel_point2[1] ** 2) + (rel_point2[2] ** 2)
    return [rel_point2[0], rel_point2[1], rel_point2[2], distance_sqr]


def get_rel_vector_3D(vector):
    global cos_a_v, cos_a_h
    global sin_a_v, sin_a_h
    vector1 = [(vector[0] * cos_a_h) - (vector[1] * sin_a_h), (vector[0] * sin_a_h) + (vector[1] * cos_a_h), vector[2]]
    vector2 = [vector1[0], (vector1[1] * cos_a_v) + (vector1[2] * sin_a_v), (vector1[1] * -sin_a_v) + (vector1[2] * cos_a_v)]
    VectorLen = ((vector2[0] ** 2) + (vector2[1] ** 2) + (vector2[2] ** 2)) ** 0.5
    return [vector2[0], vector2[1], vector2[2], VectorLen]


def handle_point_out(point_in_3D, point_out_3D, point_in_2D):
    d_3D = [point_out_3D[i] - point_in_3D[i] for i in range(3)]
    t1 = (screen_distance - point_in_3D[1])/d_3D[1]
    t2 = (2*screen_distance - point_in_3D[1])/d_3D[1]
    point_1f_2D = get_point_2D([point_in_3D[i] + d_3D[i]*t1 for i in range(3)])
    point_2f_2D = get_point_2D([point_in_3D[i] + d_3D[i]*t2 for i in range(3)])
    d_2D = [point_1f_2D[i] - point_2f_2D[i] for i in range(2)]
    return [point_in_2D[0] + d_2D[0] * 1000, point_in_2D[1] + d_2D[1] * 1000, 0]
    

def get_element_2D(element):
    points_3D = element[4]
    num_points = len(points_3D)
    points_2D = []
    for i in range(num_points):
        if points_3D[i][1] > 0:
            point_2D = get_point_2D(points_3D[i])
            if points_3D[(i-1) % num_points][1] <= 0:
                points_2D.append(handle_point_out(points_3D[i], points_3D[(i-1) % num_points], point_2D))
            points_2D.append(point_2D)
            if points_3D[(i+1) % num_points][1] <= 0:
                points_2D.append(handle_point_out(points_3D[i], points_3D[(i+1) % num_points], point_2D))
    vector = element[5] #I don't know what's its function yet.
    new_element = []
    new_element.extend(element[0:4])
    new_element.extend([points_2D, vector, element[6]])
    return new_element

def get_point_2D(point):
    global screen_distance
#    if point[1] > 0:
    x = screen_distance * point[0] / point[1]
    y = screen_distance * point[2] / point[1]
    """
    else:
        x = screen_distance * point[0] *1000
        y = screen_distance * point[2] *1000
        """
    return [x, y, 1] #, point[1] > 0, point[3]

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('3D engine')   #changable
background = skyblue
fps = 60
font_EN1 = pygame.font.Font('freesansbold.ttf', 16)
font_CH1 = pygame.font.Font('TaipeiSansTCBeta-Regular.ttf', 24)
timer = pygame.time.Clock()

running = True
while running:
    timer.tick(fps)
    screen.fill(background)
    """
    if not active:
        instruction_text = font_EN1.render(f'Space Bar to Start', True, white, black)
        screen.blit(instruction_text, (140,50))
        instruction_text2 = font_EN1.render(f'Space Bar Jumps. Left/Right Moves.', True, white, black)
        screen.blit(instruction_text2, (80, 90))
    """

    """
    score_text = font_EN1.render(f'Score: {score} ', True, white, black)
    screen.blit(score_text, (160, 250))
    floor = pygame.draw.rect(screen, white, [0, 220, WIDTH, 5])
    player = pygame.draw.rect(screen, green, [player_x, player_y, 20, 20])
    obstacle0 = pygame.draw.rect(screen, red, [obstacles[0], 200, 20, 20])
    obstacle1 = pygame.draw.rect(screen, orange, [obstacles[1], 200, 20, 20])
    obstacle2 = pygame.draw.rect(screen, yellow, [obstacles[2], 200, 20, 20])
    """
    

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        """
        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                obstacles = [300, 450, 600]
                player_x = 50
                score = 0
                active = True
        """
        
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_da_hor = 0.01
            if event.key == pygame.K_LEFT:
                player_da_hor = -0.01
            if event.key == pygame.K_UP:
                player_da_ver = 0.01
            if event.key == pygame.K_DOWN:
                player_da_ver = -0.01
            if event.key == pygame.K_SPACE and player_dz == 0:
                player_dz = 18
            if event.key == pygame.K_d:
                player_lr = 2
            if event.key == pygame.K_a:
                player_lr = -2
            if event.key == pygame.K_w:
                player_fb = 2
            if event.key == pygame.K_s:
                player_fb = -2

                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_da_hor = 0
            if event.key == pygame.K_LEFT:
                player_da_hor = 0
            if event.key == pygame.K_UP:
                player_da_ver = 0
            if event.key == pygame.K_DOWN:
                player_da_ver = 0
            if event.key == pygame.K_d:
                player_lr = 0
            if event.key == pygame.K_a:
                player_lr = 0
            if event.key == pygame.K_w:
                player_fb = 0
            if event.key == pygame.K_s:
                player_fb = 0


    """
    for i in range(len(obstacles)):
        if active:
            obstacles[i] -= obstacle_speed
            if obstacles[i] < -20:
                obstacles[i] = random.randint(470, 570)
                score += 1
            if player.colliderect(obstacle0) or player.colliderect(obstacle1) or player.colliderect(obstacle2):
                active = False
                """
    if math.pi / 2 >= player_a_ver  >= -math.pi /2:
        player_a_ver += player_da_ver
    if player_a_ver > math.pi / 2:
        player_a_ver = math.pi / 2
    elif player_a_ver < -math.pi / 2:
        player_a_ver = -math.pi / 2
    player_a_hor += player_da_hor
    cos_a_v, cos_a_h = math.cos(player_a_ver), math.cos(player_a_hor)
    sin_a_v, sin_a_h = math.sin(player_a_ver), math.sin(player_a_hor)

    #逆時針旋轉 (-theta)
    player_dx =  player_lr * cos_a_h + player_fb * sin_a_h
    player_dy = -player_lr * sin_a_h + player_fb * cos_a_h

    if -500 <= player_x <= 500:
        player_x += player_dx
    if player_x < -500:
        player_x = -500
    if player_x > 500:
        player_x = 500
        
    if -500 <= player_y <= 500:
        player_y += player_dy
    if player_y < -500:
        player_y = -500
    if player_y > 500:
        player_y = 500
    
    if player_dz > 0 or player_z > 0:
        player_z += player_dz
        player_dz -= gravity
    if player_z < 0:
        player_z = 0
    if player_z == 0 and player_dz < 0:
        player_dz = 0
    
    elements_3D_rel = dict(zip(list(elements_3D.keys()), list(map(get_rel_element, list(elements_3D.values())))))
    #print(elements_3D_rel)
    elements_2D = dict(zip(list(elements_3D_rel.keys()), list(map(get_element_2D, list(elements_3D_rel.values())))))
    
    for element in elements_2D.values():
        if len(element[4]) > 0:
            if element[0] == 0:
                for point in element[4]:
                    pygame.draw.circle(screen, element[2], pos_OnScreen(point), element[3])
            elif element[0] == 1:
                pygame.draw.line(screen, element[2], pos_OnScreen(element[4][0]), pos_OnScreen(element[4][1]), element[3])
            elif element[0] == 2:
                pygame.draw.polygon(screen, element[2], list(map(pos_OnScreen, element[4])), element[3])
    """
    for element in elements_3D_rel:
        for point in element[5]:
            pos = get_point_2D(point)
            if not pos == -1:
                if pos[2]:
                    pygame.draw.circle(screen, black, ((WIDTH/2) + pos[0], (HEIGHT/2) - pos[1]), 10)
    """

    
    pygame.display.flip()
pygame.quit()