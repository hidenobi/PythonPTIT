import pygame

# get text font and size
def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

pygame.init()
default_left = False
default_right = False

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Mysterious Maze Explorer")

# set background image
BG = pygame.image.load("assets/img/Background_10.png")

# set music song
# music_song = pygame.mixer.Sound("assets/BG_Music.mp3")
# moving_sound= pygame.mixer.Sound('assets/Running.mp3')
# lose_sound=pygame.mixer.Sound('assets/sound_lose.mp3')
# win_sound=pygame.mixer.Sound('assets/winS.mp3')
pygame.mixer.set_num_channels(3)
channel2 = pygame.mixer.Channel(2)
# Matrix size
N = 22
M = 40

