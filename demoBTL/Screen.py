import pygame, sys
from button import Button
from Print_level import print_matrix
import default, G_Var

# win screen
def win_screen(level):
    default.SCREEN.blit(pygame.image.load('assets/img/win_bg.png'),(0,0))
    # init back button
    WIN_BACK = Button(image=None, pos=(80, 40),
                      text_input="BACK", font=default.get_font(30), base_color="white", hovering_color="green")
    WIN_NEXT = Button(image=None, pos=(820, 690),
                        text_input="NEXT LEVEL", font=default.get_font(30), base_color="white", hovering_color="green")

    default.win_sound.play()
    while True:
        WIN_MOUSE_POS = pygame.mouse.get_pos()
        # set back button to screen
        WIN_BACK.changeColor(WIN_MOUSE_POS)
        WIN_BACK.update(default.SCREEN)
        WIN_NEXT.changeColor(WIN_MOUSE_POS)
        WIN_NEXT.update(default.SCREEN)


        # check for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIN_BACK.checkForInput(WIN_MOUSE_POS):
                    play_menu()
                    break
                if WIN_NEXT.checkForInput(WIN_MOUSE_POS):
                    if level > 4:
                        print_matrix(5)
                        break
                    else: print_matrix(level+1)
                    break

        pygame.display.update()


def lose_screen(level):
    default.SCREEN.blit(default.BG,(0,0))
    # init win text
    LOSE_TEXT = default.get_font(70).render("You lose!!!", True, "white")
    LOSE_RECT = LOSE_TEXT.get_rect(center=(640, 200))
    # init back button
    BACK = Button(image=None, pos=(640, 560),
                  text_input="BACK", font=default.get_font(30), base_color="white", hovering_color="green")
    Play_Again = Button(image=None, pos=(640, 460),
                        text_input="Play Again", font=default.get_font(30), base_color="white", hovering_color="green")
    default.lose_sound.play()
    while True:
        LOSE_MOUSE_POS = pygame.mouse.get_pos()
        # set win text to screen
        default.SCREEN.blit(LOSE_TEXT, LOSE_RECT)
        # set back button to screen
        BACK.changeColor(LOSE_MOUSE_POS)
        BACK.update(default.SCREEN)
        Play_Again.changeColor(LOSE_MOUSE_POS)
        Play_Again.update(default.SCREEN)

        # check for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(LOSE_MOUSE_POS):
                    play_menu()
                    break
                if Play_Again.checkForInput(LOSE_MOUSE_POS):
                    print_matrix(level)
                    break

        pygame.display.update()

# print play menu
def play_menu():

    default.SCREEN.blit(default.BG, (0,0))
    # init play text
    PLAY_TEXT = default.get_font(45).render("CHOOSE LEVEL", True, "White")
    PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
    default.SCREEN.blit(PLAY_TEXT, PLAY_RECT)
    # init back button
    PLAY_BACK = Button(image=None, pos=(80, 40),
                       text_input="BACK", font=default.get_font(30), base_color="White", hovering_color="Green")


    # init level button
    LEVEL_POSITION = [(300,220), (980, 220), (300,410), (980, 410), (640, 600)]
    LEVEL_BUTTON = []
    for level in range(5):
        # load preview level image
        level_preview = pygame.image.load(f'assets/img/preview_level_{level+1}.png')
        level_preview = pygame.transform.scale(level_preview, (400, 150))
        if level != 4:
            LEVEL_PLAY = Button(image=level_preview, pos=LEVEL_POSITION[level],
                                text_input=f"Level {level+1}", font=default.get_font(30), base_color="White",
                                hovering_color="Green")
        else: LEVEL_PLAY = Button(image=level_preview, pos=LEVEL_POSITION[level],
                                text_input="Level ???", font=default.get_font(30), base_color="White",
                                hovering_color="Green")
        LEVEL_BUTTON.append(LEVEL_PLAY)
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(default.SCREEN)
        for LEVEL_PLAY in LEVEL_BUTTON:
            LEVEL_PLAY.changeColor(PLAY_MOUSE_POS)
            LEVEL_PLAY.update(default.SCREEN)

        # check for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                    break
                for level_choose in range(5):
                    if LEVEL_BUTTON[level_choose].checkForInput(PLAY_MOUSE_POS):
                        print_matrix(level_choose+1)
                        break
        pygame.display.update()

# print option menu
def options():
    OPTION_SPEED_STATE = {0:['Speed: Default',1, 3], 1:['Speed: Slow',1,1],
                   2:['Speed: Normal',1,2], 3:['Speed: Fast',1,4], 4:['Speed: Very Fast',1,6]}
    speed_list = OPTION_SPEED_STATE.get(G_Var.speed_state)
    # init option text
    OPTIONS_TEXT = default.get_font(45).render("SETTING OPTIONS", True, "white")
    OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))

    # init back button
    OPTIONS_BACK = Button(image=None, pos=(80, 40),
                          text_input="BACK", font=default.get_font(30), base_color="white", hovering_color="green")
    while True:
        default.SCREEN.blit(default.BG,(0,0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        # set option text
        default.SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # set back button
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(default.SCREEN)
        # init music button
        MUSIC_OPTION = Button(image=None, pos=(640, 230),
                              text_input=G_Var.music_state, font=default.get_font(75), base_color="white", hovering_color="green")

        MUSIC_OPTION.changeColor(OPTIONS_MOUSE_POS)
        MUSIC_OPTION.update(default.SCREEN)

        # init speed button
        SPEED_OPTION = Button(image=None, pos=(640, 360),
                              text_input=speed_list[0], font=default.get_font(75), base_color="white", hovering_color="green")

        SPEED_OPTION.changeColor(OPTIONS_MOUSE_POS)
        SPEED_OPTION.update(default.SCREEN)
        # init matrix option
        MATRIX_OPTION = Button(image=None, pos=(640, 490),
                               text_input=G_Var.matrix_state, font=default.get_font(75), base_color="white", hovering_color="green")

        MATRIX_OPTION.changeColor(OPTIONS_MOUSE_POS)
        MATRIX_OPTION.update(default.SCREEN)
        # check for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                    break
                if MUSIC_OPTION.checkForInput(OPTIONS_MOUSE_POS):
                    if G_Var.music_state == "Music: On":
                        G_Var.music_state = "Music: Off"
                        default.music_song.stop()
                        G_Var.enableSound = False
                    else:
                        G_Var.enableSound = True
                        G_Var.music_state = "Music: On"
                        default.music_song.play(loops=-1)

                if SPEED_OPTION.checkForInput(OPTIONS_MOUSE_POS):

                    G_Var.speed_state += 1
                    if G_Var.speed_state == 5:
                        G_Var.speed_state = 0

                    speed_list = OPTION_SPEED_STATE.get(G_Var.speed_state)
                    G_Var.DELAY = speed_list[1]
                    G_Var.speed = speed_list[2]
                if MATRIX_OPTION.checkForInput(OPTIONS_MOUSE_POS):
                    if G_Var.matrix_state == "Matrix: Animated":
                        G_Var.matrix_state = "Matrix: None"
                        G_Var.printmtx = 0
                    else:
                        G_Var.matrix_state = "Matrix: Animated"
                        G_Var.printmtx = 1


        pygame.display.update()

# print main menu
def main_menu():

    # set background
    default.SCREEN.blit(default.BG, (0, 0))
    # set menu text
    # render: render the text into an image with a given color
    MENU_TEXT = default.get_font(100).render("MAIN MENU", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
    # init button in menu
    PLAY_BUTTON = Button(image=pygame.image.load("assets/img/Play Rect.png"), pos=(640, 250),
                         text_input="PLAY", font=default.get_font(75), base_color="#d7fcd4", hovering_color="White")
    OPTIONS_BUTTON = Button(image=pygame.image.load("assets/img/Options Rect.png"), pos=(640, 400),
                            text_input="OPTIONS", font=default.get_font(75), base_color="#d7fcd4", hovering_color="White")
    QUIT_BUTTON = Button(image=pygame.image.load("assets/img/Quit Rect.png"), pos=(640, 550),
                         text_input="QUIT", font=default.get_font(75), base_color="#d7fcd4", hovering_color="White")
    # set menu text to screen
    default.SCREEN.blit(MENU_TEXT, MENU_RECT)

    while True:
        # get mouse position
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        # set button to screen
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(default.SCREEN)

        # check for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_menu()
                    break
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                    break
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
