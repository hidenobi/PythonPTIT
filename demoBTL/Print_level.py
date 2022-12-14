import pygame, sys, random, os

import Screen
import default
import G_Var
from Char_Move import move
from button import Button
from Random_Matrix import generate_maze, output_to_file

def print_matrix(level):
    os.getcwd()  # Log this line.
    left = default.default_left
    right = default.default_right
    # get time
    CheckTime = 0

    # play time
    secs = 60 if level != 5 else 120


    def read_matrix(f):
        a = []
        for lines in f.readlines():
            a.append([int(x) for x in lines.split()])
        return a

    def get_start(a, n, m):
        for i in range(n):
            for j in range(m):
                if a[i][j] == 8:
                    a[i][j] = 0
                    return (i, j)
        return (-1, -1)

    def get_end(a, n, m):
        for i in range(n):
            for j in range(m):
                if a[i][j] == 9:
                    a[i][j] = 0
                    return (i, j)
        return (-1, -1)

    # check if win
    def check_win(x, y):
        if y > 30 * (M - 1):
            return True
        return False

    if level == 5:
        default.SCREEN.fill("black")
        G_MTX_TEXT = default.get_font(20).render("Generating map... Do not exit!!!", True, "white")
        G_MTX_RECT = G_MTX_TEXT.get_rect(center=(400, 700))
        default.SCREEN.blit(G_MTX_TEXT,G_MTX_RECT)

        random_matrix = generate_maze(default.SCREEN,default.N,default.M,G_Var.printmtx)
        output_to_file(default.N,default.M,random_matrix)

    # read input matrix
    f_level = open(f"assets/Matrix/Matrix_level_{level}.txt",'r')
    matrix = read_matrix(f_level)
    f_level.close()
    # matrix size, M is column
    N = len(matrix)
    M = len(matrix[0])
    # top left of matrix
    OFFSET_X = 40
    OFFSET_Y = 30
    start = get_start(matrix, N, M)
    # setting starting position
    x = start[0]*30
    y = start[1]*30
    if x == -1 or y == -1:
        print("Matrix doesn't have starting point.")
        exit()
    # get the exit of matrix
    end = get_end(matrix, N, M)
    end_x = end[0]
    end_y = end[1]
    if end_x == -1 or end_y == -1:
        print("Matrix doesn't have ending point.")
        exit()
    # set background image
    bglevel = level
    if level == 5:
        bglevel = random.randint(1,9)
    BG = pygame.image.load(f"assets/img/background_level_{bglevel}.png")
    BG = pygame.transform.scale(BG, (1280,720))
    # set block image
    block_image = pygame.image.load(f"assets/img/block_level_{bglevel}.png")
    block_image = pygame.transform.scale(block_image, (30, 30))
    # init back button
    LEVEL_BACK = Button(image=None, pos=(40, 705),
                        text_input="BACK", font=default.get_font(15), base_color="Black", hovering_color="Green")
    LEVEL_NEXT = Button(image=None, pos=(820, 705),
                        text_input="NEXT LEVEL", font=default.get_font(15), base_color="Black", hovering_color="Green")

    walkRight = []
    walkLeft = []
    idleRight = []
    idleLeft = []
    frames = 10
    for i in range (frames):
        img_R = pygame.image.load(f"assets/img/char/RunR ({i+1}).png")
        img_R = pygame.transform.scale(img_R, (30,30))
        img_L = pygame.image.load(f"assets/img/char/RunL ({i+1}).png")
        img_L = pygame.transform.scale(img_L, (30,30))
        idle_R = pygame.image.load(f"assets/img/char/IdleR ({i+1}).png")
        idle_R = pygame.transform.scale(idle_R, (30,30))
        idle_L = pygame.image.load(f"assets/img/char/IdleL ({i+1}).png")
        idle_L = pygame.transform.scale(idle_L, (30,30))
        walkRight.append(img_R)
        walkLeft.append(img_L)
        idleRight.append(idle_R)
        idleLeft.append(idle_L)

    def all_keys_released():
        keys = pygame.key.get_pressed()
        return not (keys[pygame.K_DOWN] or keys[pygame.K_UP] or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT])

    def redrawGameWindow(x, y):
        if G_Var.walkCount + 1 >= 27:
            G_Var.walkCount = 0
        # print(all_keys_released())
        if all_keys_released():
            if left:
                default.SCREEN.blit(idleLeft[G_Var.walkCount // 3], (x, y))
            else:
                default.SCREEN.blit(idleRight[G_Var.walkCount // 3], (x, y))
        elif left:
            default.SCREEN.blit(walkLeft[G_Var.walkCount // 3], (x, y))
        elif right:
            default.SCREEN.blit(walkRight[G_Var.walkCount // 3], (x, y))
        G_Var.walkCount += 1
        pygame.display.update()

    while True:
        default.SCREEN.blit(BG, (0,0))

        Time_Text = default.get_font(20).render(str(secs) + "S", True, "blue")
        Time_Rect = Time_Text.get_rect(center=(1200, 705))
        default.SCREEN.blit(Time_Text, Time_Rect)

        PLAYING_MOUSE_POS = pygame.mouse.get_pos()
        LEVEL_BACK.changeColor(PLAYING_MOUSE_POS)
        LEVEL_BACK.update(default.SCREEN)
        LEVEL_NEXT.changeColor(PLAYING_MOUSE_POS)
        LEVEL_NEXT.update(default.SCREEN)


        # print the matrix
        for j in range(N):
            for i in range(M):
                if matrix[j][i] != 0:
                    default.SCREEN.blit(block_image, (OFFSET_X + 30 * i+1, OFFSET_Y + 30 * j+1))
        redrawGameWindow(OFFSET_X + y, OFFSET_Y + x)

        # pygame.display.update()

        # check for event
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL_BACK.checkForInput(PLAYING_MOUSE_POS):
                    Screen.play_menu()
                    break
                if LEVEL_NEXT.checkForInput(PLAYING_MOUSE_POS):
                    if level > 4:
                        print_matrix(5)
                        break
                    else: print_matrix(level+1)
                    break
            if event.type == pygame.KEYDOWN:
                if not all_keys_released():
                    if not default.channel2.get_busy():
                        if G_Var.enableSound: default.channel2.play(default.moving_sound)
        if all_keys_released():
            if default.channel2.get_busy() and G_Var.enableSound:
                default.channel2.stop()
        # get key pressed
        pygame.time.delay(G_Var.DELAY)

        if key[pygame.K_UP]:
            (x,y) = move(matrix,-1,0,x,y)
        if key[pygame.K_DOWN]:
            (x,y) = move(matrix,1,0,x,y)
        if key[pygame.K_LEFT]:
            (x,y) = move(matrix,0,-1,x,y)
            left = True
            right = False
        if key[pygame.K_RIGHT]:
            (x,y) = move(matrix,0,1,x,y)
            left = False
            right = True

        if check_win(x, y):
            Screen.win_screen(level)
            break
        # pygame.display.update()

        CheckTime += 1
        if CheckTime == 60:
            secs -= 1
            CheckTime = 0
        Clock = pygame.time.Clock()
        Clock.tick(60)
        pygame.display.update()
        if (secs == 0):
            Screen.lose_screen(level)
