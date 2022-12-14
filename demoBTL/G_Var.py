import pygame
import default

pygame.init()
walkCount = 0
# set music state
music_state = "Music: On"
# Game delay per screen refresh (adjust char speed)
DELAY = 1
# Movement speed (distance char move when press a key)
speed = 2
# Speed state
speed_state = 0
# Character position
x = 0
y = 0
enableSound = False
random_matrix = [[1 for i in range(default.M)] for j in range(default.N)]
printmtx = 1
matrix_state = "Matrix: Animated"
