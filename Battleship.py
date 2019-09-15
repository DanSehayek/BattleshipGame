import pygame
import time
import random
import math

pygame.init()

# COLOURS #

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
green = (34,177,76)
yellow = (200,200,0)
light_green = (0,255,0)
light_yellow = (255,255,0)
light_red = (255,0,0)
blue = (0,0,255)
light_blue = (135, 206, 205)
orange = (255, 165, 0)
gray = (190, 190, 190)

# SCREEN DIMENSIONS #

display_width = 800
display_height = 600

# SPRITE DIMENSIONS #

grid_width = 449
grid_height = 445
ship_width = 43
ship_height = 186
ship2_width = 37
ship2_height = 146
ship3_width = 30
ship3_height = 110
ship4_width = 31
ship4_height = 65
star_width = 43
star_height = 42

# GAME SCREEN AND TITLE #

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Battleship')

# IMAGES #

ship_img = pygame.image.load('Images/Battleship1_Image2.png')
ship2_img = pygame.image.load('Images/Battleship2_Image2.png')
ship3_img = pygame.image.load('Images/Battleship3_Image2.png')
ship4_img = pygame.image.load('Images/Battleship4_Image2.png')
shipT_img = pygame.image.load('Images/Battleship1_ImageT.png')
ship2T_img = pygame.image.load('Images/Battleship2_ImageT.png')
ship3T_img = pygame.image.load('Images/Battleship3_ImageT.png')
ship4T_img = pygame.image.load('Images/Battleship4_ImageT.png')
ship11_img = pygame.image.load('Images/Ship1_Image1.png')
ship12_img = pygame.image.load('Images/Ship1_Image2.png')
ship13_img = pygame.image.load('Images/Ship1_Image3.png')
ship14_img = pygame.image.load('Images/Ship1_Image4.png')
ship15_img = pygame.image.load('Images/Ship1_Image5.png')
ship16_img = pygame.image.load('Images/Ship1_Image6.png')
ship21_img = pygame.image.load('Images/Ship2_Image1.png')
ship22_img = pygame.image.load('Images/Ship2_Image2.png')
ship23_img = pygame.image.load('Images/Ship2_Image3.png')
ship24_img = pygame.image.load('Images/Ship2_Image4.png')
ship25_img = pygame.image.load('Images/Ship2_Image5.png')
ship31_img = pygame.image.load('Images/Ship3_Image1.png')
ship32_img = pygame.image.load('Images/Ship3_Image2.png')
ship33_img = pygame.image.load('Images/Ship3_Image3.png')
ship34_img = pygame.image.load('Images/Ship3_Image4.png')
ship41_img = pygame.image.load('Images/Ship4_Image1.png')
ship42_img = pygame.image.load('Images/Ship4_Image2.png')
ship43_img = pygame.image.load('Images/Ship4_Image3.png')
eship11_img = pygame.image.load('Images/EShip1_Image1.png')
eship12_img = pygame.image.load('Images/EShip1_Image2.png')
eship21_img = pygame.image.load('Images/EShip2_Image1.png')
eship22_img = pygame.image.load('Images/EShip2_Image2.png')
eship31_img = pygame.image.load('Images/EShip3_Image1.png')
eship32_img = pygame.image.load('Images/EShip3_Image2.png')
eship41_img = pygame.image.load('Images/EShip4_Image1.png')
eship42_img = pygame.image.load('Images/EShip4_Image2.png')

menu_img = pygame.image.load('Images/MenuBackground_Image.png')
menu_b1_img = pygame.image.load('Images/MenuBackgroundB1_Image.png')
menu_b2_img = pygame.image.load('Images/MenuBackgroundB2_Image.png')
shop_p1_img = pygame.image.load('Images/ShopBackgroundP1_Image.png')
shop_p1b1_img = pygame.image.load('Images/ShopBackgroundP1B1_Image.png')
shop_p1b2_img = pygame.image.load('Images/ShopBackgroundP1B2_Image.png')
shop_p1b3_img = pygame.image.load('Images/ShopBackgroundP1B3_Image.png')
shop_p2_img = pygame.image.load('Images/ShopBackgroundP2_Image.png')
shop_p2b1_img = pygame.image.load('Images/ShopBackgroundP2B1_Image.png')
shop_p2b2_img = pygame.image.load('Images/ShopBackgroundP2B2_Image.png')
shop_p2b3_img = pygame.image.load('Images/ShopBackgroundP2B3_Image.png')
gameover_p1_img = pygame.image.load('Images/GameOverP1_Image.png')
gameover_p1b1_img = pygame.image.load('Images/GameOverP1B1_Image.png')
gameover_p1b2_img = pygame.image.load('Images/GameOverP1B2_Image.png')
gameover_p2_img = pygame.image.load('Images/GameOverP2_Image.png')
gameover_p2b1_img = pygame.image.load('Images/GameOverP2B1_Image.png')
gameover_p2b2_img = pygame.image.load('Images/GameOverP2B2_Image.png')

grid_img = pygame.image.load('Images/Grid_Image5.png')
bluestar_img = pygame.image.load('Images/Star1_Image.png')
redstar_img = pygame.image.load('Images/Star2_Image.png')
graystar_img = pygame.image.load('Images/Star3_Image.png')

falcon_upgrade_img = pygame.image.load('Images/FalconMissile_Image.png')
hawkH_upgrade_img = pygame.image.load('Images/HawkHMissile_Image.png')
hawkV_upgrade_img = pygame.image.load('Images/HawkVMissile_Image.png')

number0_img = pygame.image.load('Images/Number0_Image.png')
number1_img = pygame.image.load('Images/Number1_Image.png')
number2_img = pygame.image.load('Images/Number2_Image.png')
number3_img = pygame.image.load('Images/Number3_Image.png')
number4_img = pygame.image.load('Images/Number4_Image.png')
number5_img = pygame.image.load('Images/Number5_Image.png')
number6_img = pygame.image.load('Images/Number6_Image.png')
number7_img = pygame.image.load('Images/Number7_Image.png')
number8_img = pygame.image.load('Images/Number8_Image.png')
number9_img = pygame.image.load('Images/Number9_Image.png')

table_img = pygame.image.load('Images/ShipTable_Image.png')
enemytable_img = pygame.image.load('Images/EnemyShipTable_Image.png')
missiletable_img = pygame.image.load('Images/MissileTable_Image.png')
tablenumber0_img = pygame.image.load('Images/Number0_Image2.png')
tablenumber1_img = pygame.image.load('Images/Number1_Image2.png')
tablenumber2_img = pygame.image.load('Images/Number2_Image2.png')
tablenumber3_img = pygame.image.load('Images/Number3_Image2.png')
tablenumber4_img = pygame.image.load('Images/Number4_Image2.png')
tablenumber5_img = pygame.image.load('Images/Number5_Image2.png')

missileselection_img = pygame.image.load('Images/MissileSelection_Image.png')
missileselection1_img = pygame.image.load('Images/MissileSelectionM1_Image.png')
missileselection2_img = pygame.image.load('Images/MissileSelectionM2_Image.png')
missileselection3_img = pygame.image.load('Images/MissileSelectionM3_Image.png')

rotation_img = pygame.image.load('Images/RotationButton_Image.png')
missile_img = pygame.image.load('Images/MissileButton_Image.png')
missileactive_img = pygame.image.load('Images/MissileButtonActive_Image.png')

player1_img = pygame.image.load('Images/Player1_Image.png')
player2_img = pygame.image.load('Images/Player2_Image.png')

tutorial1_img = pygame.image.load('Images/Tutorial1_Image.png')
tutorial2_img = pygame.image.load('Images/Tutorial2_Image.png')

game_icon = pygame.image.load('Images/GameIcon_Image.png')

# GAME ICON #
pygame.display.set_icon(game_icon)

# SOUNDS #
button_confirm_sound = pygame.mixer.Sound("Audio/Button_Sound2.wav")

# CLOCK #
clock = pygame.time.Clock()

# FUNCTIONS #
def coins(number, x_pos, y_pos):

    number = str(number)
    for x in range(0, len(number)):
        if number[x] == "0":
            gameDisplay.blit(number0_img, (x_pos + 36 * x, y_pos))
        elif number[x] == "1":
            gameDisplay.blit(number1_img, (x_pos + 36 * x, y_pos))
        elif number[x] == "2":
            gameDisplay.blit(number2_img, (x_pos + 36 * x, y_pos))
        elif number[x] == "3":
            gameDisplay.blit(number3_img, (x_pos + 36 * x, y_pos))
        elif number[x] == "4":
            gameDisplay.blit(number4_img, (x_pos + 36 * x, y_pos))
        elif number[x] == "5":
            gameDisplay.blit(number5_img, (x_pos + 36 * x, y_pos))
        elif number[x] == "6":
            gameDisplay.blit(number6_img, (x_pos + 36 * x, y_pos))
        elif number[x] == "7":
            gameDisplay.blit(number7_img, (x_pos + 36 * x, y_pos))
        elif number[x] == "8":
            gameDisplay.blit(number8_img, (x_pos + 36 * x, y_pos))
        elif number[x] == "9":
            gameDisplay.blit(number9_img, (x_pos + 36 * x, y_pos))

def missile_count(numbers, x_pos, y_pos):

    for x in range(0, len(numbers)):
        if str(numbers[x]) == "0":
            gameDisplay.blit(tablenumber0_img, (x_pos + 100 * x, y_pos))
        elif str(numbers[x]) == "1":
            gameDisplay.blit(tablenumber1_img, (x_pos + 100 * x, y_pos))
        elif str(numbers[x]) == "2":
            gameDisplay.blit(tablenumber2_img, (x_pos + 100 * x, y_pos))
        elif str(numbers[x]) == "3":
            gameDisplay.blit(tablenumber3_img, (x_pos + 100 * x, y_pos))
        elif str(numbers[x]) == "4":
            gameDisplay.blit(tablenumber4_img, (x_pos + 100 * x, y_pos))
        elif str(numbers[x]) == "5":
            gameDisplay.blit(tablenumber5_img, (x_pos + 100 * x, y_pos))

# MENU CLASSES #

class Main_Menu:

    def __init__(self):

        self.run = True
        self.button_1 = "Inactive"      #self.button = "Active" occurs when the user places their mouse on the button and will outline the button in orange
        self.button_2 = "Inactive"
        self.image = menu_img

    def render(self):

        for event in pygame.event.get():        #Allows the user to quit if they click the close button
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(self.image, (0,0))     #Blits the menu image to the screen

        self.button(60, 508, 210, 563, "play")      #Verifies that the play/quit button has been clicked and responds accordingly
        self.button(611, 507, 737, 566, "quit")

        if self.button_1 == "Inactive" and self.button_2 == "Inactive":
            self.image = menu_img

        pygame.display.update()
        clock.tick(15)

    def button(self, x, y, x2, y2, action):

        cur = pygame.mouse.get_pos()            #Retrieves the cursor position
        click = pygame.mouse.get_pressed()      #Indicates which mouse buttons are currently clicked

        if x < cur[0] < x2 and y < cur[1] < y2:

            if click[0] == 1:       #If the left mouse button is clicked

                pygame.mixer.Sound.play(button_confirm_sound)

                if action == "quit":        #Quits if the user clicks the QUIT button
                    pygame.quit()
                    quit()
                elif action == "play":      #Goes to the game if the user clicks the PLAY button and resets attributes if the user has already played at least once
                    shop.run = True
                    self.run = False
                    gameLoop()

            else:       #If the user has placed the cursor on one of the buttons but has not clicked it then that button will light up in orange

                if action == "play":
                    self.image = menu_b1_img
                    self.button_1 = "Active"
                elif action == "quit":
                    self.image = menu_b2_img
                    self.button_2 = "Active"

        else:       #If the user has not placed the cursor on any of the buttons then all buttons will be set back to default style

            if action == "play":
                self.button_1 = "Inactive"
            elif action == "quit":
                self.button_2 = "Inactive"

class Shop:

    def __init__(self):

        self.money = 500
        self.p1 = True
        self.p2 = False
        self.type = 1
        self.run = True
        self.p1_arsenal = [0,0,0]
        self.p2_arsenal = [0,0,0]
        self.image = shop_p1_img
        self.key_counter = 0
        self.button_1 = "Inactive"
        self.button_2 = "Inactive"
        self.button_3 = "Inactive"

    def render(self):

        if self.money < 100 and self.p1 == True:        #Switches to Player 2 if Player 1 cannot buy anymore missiles

            self.p2 = True
            self.p1 = False
            self.money = 500
            self.type = 1

        elif self.money < 100 and self.p2 == True:      #Switches to the game screen if Player 2 cannot buy anymore missiles

            self.p2 = False
            self.run = False

        if self.p1 == True:

            self.image = shop_p1_img

        elif self.p2 == True:

            self.image = shop_p2_img

        self.button(69, 523, 129, 576, "left")
        self.button(343, 523, 452, 576, "buy")
        self.button(664, 523, 724, 576, "right")

        if self.button_1 == "Inactive" and self.button_2 == "Inactive" and self.button_3 == "Inactive":

            if self.p1 == True:
                self.image = shop_p1_img

            elif self.p2 == True:
                self.image = shop_p2_img

        gameDisplay.blit(self.image, (0,0))     #Blits the shop menu to the screen

        coins(self.money, 660, 35)      #Blits the number of coins the currently player has to the screen

        if self.type == 1:
            gameDisplay.blit(falcon_upgrade_img, (210, 127))        #Blits the Falcon missile image and description to the shop menu

        if self.type == 2:
            gameDisplay.blit(hawkH_upgrade_img, (210, 127))         #Blits the HawkH missile image and description to the shop menu

        if self.type == 3:
            gameDisplay.blit(hawkV_upgrade_img, (210, 127))         #Blits the HawkV missile image and description to the shop menu

        if 0 < self.key_counter < 8:        #Sets a timer after the left/right arrow is clicked to ensure that the program does not register another immediate click
            self.key_counter += 1

        elif self.key_counter == 8:
            self.key_counter = 0

    def button(self, x, y, x2, y2, action):

        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < cur[0] < x2 and y < cur[1] < y2:

            if click[0] == 1:

                if action == "left":        #Allows the user to navigate to the previous missile if the LEFT button is clicked

                    if self.key_counter == 0:
                        self.type -= 1
                        if self.type < 1:       #Ensures that the user cannot move past the first missile
                            self.type = 1
                        else:
                            pygame.mixer.Sound.play(button_confirm_sound)
                        self.key_counter += 1

                    elif self.key_counter == 8:
                        self.key_counter = 0

                elif action == "buy":       #Allows the user to buy the current missile if the BUY button is clicked

                    if self.key_counter == 0:

                        pygame.mixer.Sound.play(button_confirm_sound)
                        if self.p1 == True:
                            if self.type == 1:      #Deducts 100 coins if the Falcon missile is selected
                                self.p1_arsenal[0] += 1
                                self.money -= 100

                            if self.type == 2:      #Deducts 150 coins if the HawkH missile is selected
                                if self.money >= 150:
                                    self.p1_arsenal[1] += 1
                                    self.money -= 150

                            if self.type == 3:      #Deducts 150 coins if the HawkV missile is selected

                                if self.money >= 150:
                                    self.p1_arsenal[2] += 1
                                    self.money -= 150

                        if self.p2 == True:

                            if self.type == 1:
                                self.p2_arsenal[0] += 1
                                self.money -= 100

                            if self.type == 2:

                                if self.money >= 150:
                                    self.p2_arsenal[1] += 1
                                    self.money -= 150

                            if self.type == 3:

                                if self.money >= 150:
                                    self.p2_arsenal[2] += 1
                                    self.money -= 150

                        self.key_counter += 1

                    elif self.key_counter == 8:
                        self.key_counter = 0

                elif action == "right":         #Allows the user to navigate to the next missile if the RIGHT button is clicked

                    if self.key_counter == 0:
                        self.type += 1
                        if self.type > 3:       #Ensures that the user cannot move past the last missile
                            self.type = 3
                        else:
                            pygame.mixer.Sound.play(button_confirm_sound)
                        self.key_counter += 1

                    elif self.key_counter == 8:
                        self.key_counter = 0

            else:

                if action == "left":
                    if self.p1 == True:
                        self.image = shop_p1b1_img
                    elif self.p2 == True:
                        self.image = shop_p2b1_img
                    self.button_1 = "Active"
                elif action == "buy":
                    if self.p1 == True:
                        self.image = shop_p1b2_img
                    elif self.p2 == True:
                        self.image = shop_p2b2_img
                    self.button_2 = "Active"
                elif action == "right":
                    if self.p1 == True:
                        self.image = shop_p1b3_img
                    elif self.p2 == True:
                        self.image = shop_p2b3_img
                    self.button_3 = "Active"

        else:

            if action == "left":
                self.button_1 = "Inactive"
            elif action == "buy":
                self.button_2 = "Inactive"
            elif action == "right":
                self.button_3 = "Inactive"

class Game_Over:

    def __init__(self):

        self.run = False
        self.button_1 = "Inactive"      #Buttons have same interactivity as buttons in main menu class
        self.button_2 = "Inactive"
        self.image = gameover_p1_img
        self.p1 = False
        self.p2 = False

    def render(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        self.button(38, 512, 391, 566, "play")
        self.button(632, 512, 757, 569, "quit")

        gameDisplay.blit(self.image, (0,0))

        if self.button_1 == "Inactive" and self.button_2 == "Inactive":

            if self.p1 == True:
                self.image = gameover_p1_img

            elif self.p2 == True:
                self.image = gameover_p2_img

        pygame.display.update()
        clock.tick(15)

    def button(self, x, y, x2, y2, action):

        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < cur[0] < x2 and y < cur[1] < y2:

            if click[0] == 1:

                pygame.mixer.Sound.play(button_confirm_sound)

                if action == "quit":        #Allows the user to quit if they click the QUIT button
                    pygame.quit()
                    quit()

                elif action == "play":      #Allows the user to play again if they click the PLAY AGAIN button and resets attributes accordingly
                    grid.p1 = True
                    grid.p2 = False
                    grid.p1_ships = True
                    grid.p2_ships = False
                    grid.turn = True
                    grid.x_select = 0
                    grid.y_select = 0
                    grid.time_counter = 0
                    grid.pos_list1 = []
                    grid.pos_list2 = []
                    grid.pre_hit = 0
                    grid.pre_hit1 = 0
                    grid.pre_hit2 = 0
                    grid.ship_x = display_width / 2 - grid_width / 2 + 2 - 100
                    grid.ship_y = display_height / 2 - grid_height / 2 + 16 + 16
                    grid.ship_orient = "Vertical"
                    grid.rotate = False
                    grid.ship_counter = 0
                    grid.ship_list1 = []
                    grid.ship_list2 = []
                    grid.occupied = False
                    grid.list_switch = 0
                    grid.hit_counter1 = [0,0,0,0]
                    grid.hit_counter2 = [0,0,0,0]
                    grid.special_missile1 = False
                    grid.special_missile2 = False
                    grid.special_missile3 = False
                    grid.missile_selection = False
                    grid.missile_counter = 0
                    grid.missile_counter2 = 0
                    grid.selection_x = 0.5 * display_width - 0.5 * grid.selection_width
                    grid.selection_y = 0.5 * display_height - 0.5 * grid.selection_height
                    grid.posT_list = []
                    grid.position_counter = 0
                    shop.money = 500
                    shop.p1 = True
                    shop.p2 = False
                    shop.type = 1
                    shop.run = True
                    shop.p1_arsenal = [0,0,0]
                    shop.p2_arsenal = [0,0,0]
                    shop.image = shop_p1_img
                    shop.key_counter = 0
                    self.win = False
                    self.run = False
                    gameLoop()

            else:

                if action == "play":

                    if self.p1 == True:
                        self.image = gameover_p1b1_img

                    elif self.p2 == True:
                        self.image = gameover_p2b1_img

                    self.button_1 = "Active"

                elif action == "quit":

                    if self.p1 == True:
                        self.image = gameover_p1b2_img

                    elif self.p2 == True:
                        self.image = gameover_p2b2_img

                    self.button_2 = "Active"

        else:

            if action == "play":
                self.button_1 = "Inactive"
            elif action == "quit":
                self.button_2 = "Inactive"

# GAME CLASSES #

class Grid:

    def __init__(self):

        self.x = display_width / 2 - grid_width / 2 - 100
        self.y = display_height / 2 - grid_height / 2 + 16
        self.width = grid_width
        self.height = grid_height
        self.p1 = True
        self.p2 = False
        self.p1_ships = True
        self.p2_ships = False
        self.turn = True
        self.x_select = 0
        self.y_select = 0
        self.time_counter = 0
        self.pos_list1 = []
        self.pos_list2 = []
        self.pre_hit = 0
        self.pre_hit1 = 0
        self.pre_hit2 = 0
        self.ship_x = display_width / 2 - grid_width / 2 + 2 - 100
        self.ship_y = display_height / 2 - grid_height / 2 + 16 + 16
        self.ship_orient = "Vertical"
        self.rotate = False
        self.ship_counter = 0
        self.ship_list1 = []
        self.ship_list2 = []
        self.occupied = False
        self.list_switch = 0
        self.hit_counter1 = [0,0,0,0]
        self.hit_counter2 = [0,0,0,0]
        self.special_missile1 = False
        self.special_missile2 = False
        self.special_missile3 = False
        self.offsetV_x = [2,5,8,8]
        self.offsetV_y = [16,15,14,14]
        self.offsetH_x = [17,14,11,12]
        self.offsetH_y = [1,4,8,7]
        self.ship_width = [ship_width, ship2_width, ship3_width, ship4_width]
        self.ship_height = [ship_height, ship2_height, ship3_height, ship4_height]
        self.ship1_list = [ship11_img, ship12_img, ship13_img, ship14_img, ship15_img, ship16_img]
        self.ship2_list = [ship21_img, ship22_img, ship23_img, ship24_img, ship25_img]
        self.ship3_list = [ship31_img, ship32_img, ship33_img, ship34_img]
        self.ship4_list = [ship41_img, ship42_img, ship43_img]
        self.table_x = 0.8 * display_width - 30
        self.table_y = display_height / 2 - grid_height / 2 - 5
        self.enemytable_x = 0.8 * display_width - 30
        self.enemytable_y = display_height / 2 - grid_height / 2 + 232
        self.increment = 44.7
        self.rotation_size = 63
        self.rotate_counter = 0
        self.missile_selection = False
        self.missile_counter = 0
        self.missile_counter2 = 0
        self.selection_width = 623
        self.selection_height = 117
        self.selection_x = 0.5 * display_width - 0.5 * self.selection_width
        self.selection_y = 0.5 * display_height - 0.5 * self.selection_height
        self.posT_list = []
        self.position_counter = 0
        self.win = False
        self.tutorial1 = False
        self.tutorial1_width = 465
        self.tutorial1_height = 211
        self.t1_counter = 1
        self.tutorial2 = False
        self.tutorial2_width = 265
        self.tutorial2_height = 211
        self.t2_counter = 1
        self.missile_image = missile_img
        self.missile_active = False

    def button(self, x, y, x2, y2, action):

        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < cur[0] < x2 and y < cur[1] < y2:

            if click[0] == 1:

                if action == "rotate" and self.rotate_counter == 0:             #Switches the current ship's orientation if the rotate button is clicked
                                                                                #Rotate_counter = 0 ensures that the button was not clicked less than 1.33 seconds ago
                    pygame.mixer.Sound.play(button_confirm_sound)

                    if self.ship_orient == "Vertical":
                        self.ship_orient = "Horizontal"
                        self.rotate = True

                    elif grid.ship_orient == "Horizontal":
                        self.ship_orient = "Vertical"
                        self.rotate = True

                    self.rotate_counter += 1                                    #Starts a timer that will prevent the button from being clicked again
                                                                                #for the next 1.33 seconds
                if action == "missile":                                         #Toggles the player's current missile if the missile button is clicked

                    if self.missile_counter2 == 0:                              #Missile_counter2 = 0 ensures that the button was not clicked less than 1.33 seconds ago

                        pygame.mixer.Sound.play(button_confirm_sound)

                        if self.missile_active == True:                         #Sets the player's current missile back to the default missile if a special missile is
                                                                                #currently active
                            self.missile_active = False
                            self.special_missile1 = False
                            self.special_missile2 = False
                            self.special_missile3 = False

                            self.missile_counter2 += 1                          #Starts a timer that will prevent the button from being clicked again
                                                                                #for the next 1.33 seconds
                        else:

                            if self.missile_selection == False:

                                self.missile_selection = True                   #Missile_selection = True will notify the player that they have selected a special
                                self.missile_counter2 += 1                      #missile by lighting the missile button green

                            elif self.missile_selection == True:

                                self.missile_selection = False                  #Missile_selection = False will notify the player that they have deselected a
                                self.missile_counter2 += 1                      #special missile by returning the missile button to its original colour

    def render(self):

        gameDisplay.blit(grid_img, (self.x, self.y))                            #Blits the grid to the screen

        gameDisplay.blit(table_img, (self.table_x, self.table_y))                           #Blits the table of the current player's ships to the screen
        gameDisplay.blit(enemytable_img, (self.enemytable_x, self.enemytable_y))            #Blits the table of the enemy player's ships to the screen

        if self.p1 == True:

            gameDisplay.blit(missiletable_img, (self.x, 0))                     #Blits the table showing the number of each missile the current player has

            missile_count(shop.p1_arsenal, self.x + 38, 37)                     #Blits the number for each missile to the table

            gameDisplay.blit(self.ship1_list[self.hit_counter1[0]], (self.table_x + 7, self.table_y + 54))          #Blits each of the current player's ships to the
            gameDisplay.blit(self.ship2_list[self.hit_counter1[1]], (self.table_x + 7, self.table_y + 104))         #player table
            gameDisplay.blit(self.ship3_list[self.hit_counter1[2]], (self.table_x + 7, self.table_y + 144))         #The hit_counter corresponds to the number of red
            gameDisplay.blit(self.ship4_list[self.hit_counter1[3]], (self.table_x + 7, self.table_y + 184))         #dots that ship will have

        elif self.p2 == True:                                                   #Same as above but for player 2

            gameDisplay.blit(missiletable_img, (self.x, 0))

            missile_count(shop.p2_arsenal, self.x + 38, 37)

            gameDisplay.blit(self.ship1_list[self.hit_counter2[0]], (self.table_x + 7, self.table_y + 54))
            gameDisplay.blit(self.ship2_list[self.hit_counter2[1]], (self.table_x + 7, self.table_y + 104))
            gameDisplay.blit(self.ship3_list[self.hit_counter2[2]], (self.table_x + 7, self.table_y + 144))
            gameDisplay.blit(self.ship4_list[self.hit_counter2[3]], (self.table_x + 7, self.table_y + 184))

        if self.missile_active == True:                                         #Lights the missile button green if a special missile is selected
            self.missile_image = missileactive_img

        elif self.missile_active == False:                                      #Returns the missile button to the original colour is a special missile is deselected
            self.missile_image = missile_img

        gameDisplay.blit(self.missile_image, (0.55 * display_width, 7))         #Blits the missile button to the screen

        self.button(0.55 * display_width, 7, 0.55 * display_width + self.rotation_size, 7 + self.rotation_size, "missile")      #Checks to see if the missile button
                                                                                                                                #has been clicked
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.missile_counter > 0:                                            #Each of these counters ensures that the computer does not register more than one
            self.missile_counter += 1                                           #mouse or key click when the user only intends for one click


        if self.missile_counter == 40:
            self.missile_counter = 0

        if self.missile_counter2 > 0:
            self.missile_counter2 += 1

        if self.missile_counter2 == 40:
            self.missile_counter2 = 0

        if self.time_counter > 0:
            self.time_counter += 1

        if self.time_counter == 40:                                             #Switches to the next player's turn once the current player has made there move
                                                                                #Ensures that no special missile is immediately activated
            if self.p1 == True:
                self.p2 = True
                self.p1 = False

                self.missile_active = False
                self.special_missile1 = False
                self.special_missile2 = False
                self.special_missile3 = False

            elif self.p2 == True:
                self.p1 = True
                self.p2 = False

                self.missile_active = False
                self.special_missile1 = False
                self.special_missile2 = False
                self.special_missile3 = False

            self.turn = True
            self.time_counter = 0

        if click[0] != 1:                                                       #Transparent stars are shown as the user moves the cursor along the grid to show
                                                                                #what tiles are currently selected
            if self.special_missile1 == True:

                if cur[0] < self.x + self.increment or cur[0] > self.x + self.width - self.increment:     #Ensures that falcon missile stars are not shown if a portion
                    self.pre_hit = 2                                                                      #of those stars are not on the grid


                # Setting pre_hit = 2 prevents stars from being shown if the cursor is not on the grid
                elif cur[1] < self.y + self.increment or cur[1] > self.y + self.height - self.increment:
                    self.pre_hit = 2

                else:
                    self.pre_hit = 0                                            #Setting pre_hit = 0 ensures that stars are shown as the cursor is confirmed to be
                                                                                #on the grid
            elif self.special_missile2 == True:

                if cur[0] < self.x + self.increment * 2 or cur[0] > self.x + self.width - self.increment * 2 or cur[1] < self.y or cur[1] > self.y + self.height:
                    self.pre_hit = 2                                            #Ensures that the HawkH stars are not shown if a portion of those stars
                                                                                #are not on the grid
                else:
                    self.pre_hit = 0

            elif self.special_missile3 == True:
                if cur[1] < self.y + self.increment * 2  or cur[1] > self.y + self.height - self.increment * 2 or cur[0] < self.x or cur[0] > self.x + self.width:
                    self.pre_hit = 2                                            #Ensures that the HawkV stars are not shown if a portion of those stars
                                                                                #are not on the grid
                else:
                    self.pre_hit = 0

            else:
                if cur[0] < self.x or cur[0] > self.x + self.width or cur[1] < self.y or cur[1] > self.y + self.height:
                    self.pre_hit = 2                                            #Case for which no special missile is selected
                else:
                    self.pre_hit = 0

            for x in range(0, 10):
                if self.x + (x) * self.increment < cur[0] < self.x + (x + 1) * self.increment:      #Obtains the horizontal position (column) that the cursor is
                    self.x_select = self.x + x * self.increment                                     #currently on
                    break

            for y in range(0, 10):
                if self.y + (y) * self.increment < cur[1] < self.y + (y + 1) * self.increment:      #Obtains the vertical position (row) that the cursor is
                    self.y_select = self.y + y * self.increment                                     #currently on
                    break

            if self.pre_hit == 0:

                if self.special_missile1 == True:                                                   #Assigns a position to each of the transparent stars based on
                                                                                                    #position and missile that is selected
                    self.posT_list.append([self.x_select, self.y_select])
                    self.posT_list.append([self.x_select + self.increment, self.y_select])
                    self.posT_list.append([self.x_select - self.increment, self.y_select])
                    self.posT_list.append([self.x_select, self.y_select + self.increment])
                    self.posT_list.append([self.x_select, self.y_select - self.increment])

                elif self.special_missile2 == True:

                    self.posT_list.append([self.x_select, self.y_select])
                    self.posT_list.append([self.x_select + self.increment, self.y_select])
                    self.posT_list.append([self.x_select - self.increment, self.y_select])
                    self.posT_list.append([self.x_select + self.increment * 2, self.y_select])
                    self.posT_list.append([self.x_select - self.increment * 2, self.y_select])

                elif self.special_missile3 == True:

                    self.posT_list.append([self.x_select, self.y_select])
                    self.posT_list.append([self.x_select, self.y_select + self.increment])
                    self.posT_list.append([self.x_select, self.y_select - self.increment])
                    self.posT_list.append([self.x_select, self.y_select + self.increment * 2])
                    self.posT_list.append([self.x_select, self.y_select - self.increment * 2])

                else:
                    self.posT_list.append([self.x_select, self.y_select])

                for pos in self.posT_list:                                      #Blits each of the transparent stars to the screen
                    gameDisplay.blit(graystar_img, (pos[0], pos[1]))

                self.posT_list = []                                             #Empties the list to ensure that the current stars do not remain once the cursor has been moved

        if self.turn == True and click[0] == 1 and self.missile_selection == False and self.missile_counter == 0:       #If the player has clicked a tile

            if self.x < cur[0] < self.x + self.width and self.y < cur[1] < self.y + self.height:                        #If the cursor is on the grid

                if self.special_missile1 == True:
                    if cur[0] < self.x + self.increment or cur[0] > self.x + self.width - self.increment:               #Ensures that none of the Falcon missile
                                                                                                                        #stars are off the grid
                        if self.p1 == True:
                            self.pre_hit1 = 2                                                                           #Setting prehit = 2 notifies that program
                                                                                                                        #that it cannot blit the stars to the screen
                        elif self.p2 == True:
                            self.pre_hit2 = 2

                    elif cur[1] < self.y + self.increment or cur[1] > self.y + self.height - self.increment:

                        if self.p1 == True:
                            self.pre_hit1 = 2

                        elif self.p2 == True:
                            self.pre_hit2 = 2

                if self.special_missile2 == True:                               #Ensures that none of the HawkH missile stars are off the grid

                    if cur[0] < self.x + self.increment * 2 or cur[0] > self.x + self.width - self.increment * 2:

                        if self.p1 == True:
                            self.pre_hit1 = 2

                        elif self.p2 == True:
                            self.pre_hit2 = 2

                if self.special_missile3 == True:                               #Ensures that none of the HawkV missile stars are off the the grid

                    if cur[1] < self.y + self.increment * 2  or cur[1] > self.y + self.height - self.increment * 2:

                        if self.p1 == True:
                            self.pre_hit1 = 2

                        elif self.p2 == True:
                            self.pre_hit2 = 2

                for x in range(0, 10):
                    if self.x + (x) * self.increment < cur[0] < self.x + (x + 1) * self.increment:      #Obtains the horizontal position (column) that the cursor
                                                                                                        #is currently on
                        self.x_select = self.x + x * self.increment
                        break

                for y in range(0, 10):
                    if self.y + (y) * self.increment < cur[1] < self.y + (y + 1) * self.increment:      #Obtains the vertical position (row) that the cursor
                                                                                                        #is currently on
                        self.y_select = self.y + y * self.increment
                        break

                if self.p1 == True:

                    for pos in self.pos_list1:                                      #Refers to the list of positions that Player 1 has already hit

                        if self.special_missile1 == True:                           #Ensures that none of the currently selected tiles coincide with any of the
                                                                                    #previously selected tiles based on Falcon missile selection
                            if self.x_select - 44 <= pos[0] <= self.x_select + 44:
                                if self.y_select - self.increment - 44 <= pos[1] <= self.y_select + self.increment + 44:
                                    self.pre_hit1 = 1                               #Setting pre_hit = 1 will prevent the player from being able to select those tiles

                            elif self.x_select + self.increment - 44 <= pos[0] <= self.x_select + self.increment + 44:
                                if self.y_select - 44 <= pos[1] <= self.y_select + 44:
                                    self.pre_hit1 = 1

                            elif self.x_select - self.increment - 44 <= pos[0] <= self.x_select - self.increment + 44:
                                if self.y_select - 44 <= pos[1] <= self.y_select + 44:
                                    self.pre_hit1 = 1

                        elif self.special_missile2 == True:                         #Ensures that none of the currently selected tiles coincide with any of the
                                                                                    #previously selected tiles based on HawkH missile selection
                            for i in range(5):

                                if self.x_select - self.increment * (2 - i) - 20 <= pos[0] <= self.x_select - self.increment * (2 - i) + 20:
                                    if self.y_select - 20 <= pos[1] <= self.y_select + 20:
                                        self.pre_hit1 = 1

                        elif self.special_missile3 == True:                         #Ensures that none of the currently selected tiles coincide with any of the
                                                                                    #previously selected tiles based on HawkV missile selection
                             for i in range(5):

                                if self.y_select - self.increment * (2 - i) - 20 <= pos[1] <= self.y_select - self.increment * (2 - i) + 20:
                                    if self.x_select - 20 <= pos[0] <= self.x_select + 20:
                                        self.pre_hit1 = 1

                        else:       #Ensures that none of the currently selected tiles coincide with any of the previously selected tiles based on default missile selection

                            if pos == [self.x_select, self.y_select, False] or pos == [self.x_select, self.y_select, True]:
                                self.pre_hit1 = 1

                    if self.pre_hit1 == 0:                                      #Prehit_1 = 0 notifies the program that the player can select those tiles

                        if self.special_missile1 == True:       #Appends those tiles to the position list containing the selected tiles based on Falcon missile selection

                            self.pos_list1.append([self.x_select, self.y_select, False])        #The boolean element will be set to true if the tile contains a ship
                            self.pos_list1.append([self.x_select + self.increment, self.y_select, False])
                            self.pos_list1.append([self.x_select - self.increment, self.y_select, False])
                            self.pos_list1.append([self.x_select, self.y_select + self.increment, False])
                            self.pos_list1.append([self.x_select, self.y_select - self.increment, False])
                            self.special_missile1 = False
                            shop.p1_arsenal[0] -= 1

                        elif self.special_missile2 == True:     #Appends those tiles to the position list containing the selected tiles based on HawkH missile selection

                            self.pos_list1.append([self.x_select, self.y_select, False])
                            self.pos_list1.append([self.x_select + self.increment, self.y_select, False])
                            self.pos_list1.append([self.x_select - self.increment, self.y_select, False])
                            self.pos_list1.append([self.x_select + self.increment * 2, self.y_select, False])
                            self.pos_list1.append([self.x_select - self.increment * 2, self.y_select, False])
                            self.special_missile2 = False
                            shop.p1_arsenal[1] -= 1

                        elif self.special_missile3 == True:     #Appends those tiles to the position list containing the selected tiles based on HawkV missile selection

                            self.pos_list1.append([self.x_select, self.y_select, False])
                            self.pos_list1.append([self.x_select, self.y_select + self.increment, False])
                            self.pos_list1.append([self.x_select, self.y_select - self.increment, False])
                            self.pos_list1.append([self.x_select, self.y_select + self.increment * 2, False])
                            self.pos_list1.append([self.x_select, self.y_select - self.increment * 2, False])
                            self.special_missile3 = False
                            shop.p1_arsenal[2] -= 1

                        else:                           #Appends those tiles to the position list containing the selected tiles based on default missile selection
                            self.pos_list1.append([self.x_select, self.y_select, False])

                        self.turn = False
                        self.time_counter = 1

                    else:
                        self.pre_hit1 = 0

                if self.p2 == True:                     #Same functionality as the if self.p1 == True statement but for Player 2

                    for pos in self.pos_list2:
                        if self.special_missile1 == True:
                            if self.x_select - 44 <= pos[0] <= self.x_select + 44:
                                if self.y_select - self.increment - 44 <= pos[1] <= self.y_select + self.increment + 44:
                                    self.pre_hit2 += 1

                            elif self.x_select + self.increment - 44 <= pos[0] <= self.x_select + self.increment + 44:
                                if self.y_select - 44 <= pos[1] <= self.y_select + 44:
                                    self.pre_hit2 += 1

                            elif self.x_select - self.increment - 44 <= pos[0] <= self.x_select - self.increment + 44:
                                if self.y_select - 44 <= pos[1] <= self.y_select + 44:
                                    self.pre_hit2 += 1

                        elif self.special_missile2 == True:

                            for i in range(5):

                                if self.x_select - self.increment * (2 - i) - 20 <= pos[0] <= self.x_select - self.increment * (2 - i) + 20:
                                    if self.y_select - 20 <= pos[1] <= self.y_select + 20:
                                        self.pre_hit2 += 1

                        elif self.special_missile3 == True:

                            for i in range(5):

                                if self.y_select - self.increment * (2 - i) - 20 <= pos[1] <= self.y_select - self.increment * (2 - i) + 20:
                                    if self.x_select - 20 <= pos[0] <= self.x_select + 20:
                                        self.pre_hit2 += 1

                        else:
                            if pos == [self.x_select, self.y_select, False] or pos == [self.x_select, self.y_select, True]:
                                self.pre_hit2 += 1

                    if self.pre_hit2 == 0:

                        if self.special_missile1 == True:

                            self.pos_list2.append([self.x_select, self.y_select, False])
                            self.pos_list2.append([self.x_select + self.increment, self.y_select, False])
                            self.pos_list2.append([self.x_select - self.increment, self.y_select, False])
                            self.pos_list2.append([self.x_select, self.y_select + self.increment, False])
                            self.pos_list2.append([self.x_select, self.y_select - self.increment, False])
                            self.special_missile1 = False
                            shop.p2_arsenal[0] -= 1

                        elif self.special_missile2 == True:

                            self.pos_list2.append([self.x_select, self.y_select, False])
                            self.pos_list2.append([self.x_select + self.increment, self.y_select, False])
                            self.pos_list2.append([self.x_select - self.increment, self.y_select, False])
                            self.pos_list2.append([self.x_select + self.increment * 2, self.y_select, False])
                            self.pos_list2.append([self.x_select - self.increment * 2, self.y_select, False])
                            self.special_missile2 = False
                            shop.p2_arsenal[1] -= 1

                        elif self.special_missile3 == True:

                            self.pos_list2.append([self.x_select, self.y_select, False])
                            self.pos_list2.append([self.x_select, self.y_select + self.increment, False])
                            self.pos_list2.append([self.x_select, self.y_select - self.increment, False])
                            self.pos_list2.append([self.x_select, self.y_select + self.increment * 2, False])
                            self.pos_list2.append([self.x_select, self.y_select - self.increment * 2, False])
                            self.special_missile3 = False
                            shop.p2_arsenal[2] -= 1

                        else:
                            self.pos_list2.append([self.x_select, self.y_select, False])

                        self.turn = False
                        self.time_counter = 1

                    else:
                        self.pre_hit2 = 0

        if self.p1 == True:

            for x in range (0, len(self.pos_list1)):                            #Compares each position that Player 1 has selected with each position of
                                                                                #Player 2's ships and sets a boolean element equal to True if there is a match
                for i in range (0, len(self.ship_list2)):
                    if self.ship_list2[i][0] - 20 <= self.pos_list1[x][0] <= self.ship_list2[i][0] + 20 and self.pos_list1[x][2] == False:
                        if self.ship_list2[i][1] - 20 <= self.pos_list1[x][1] <= self.ship_list2[i][1] + 20:
                            self.pos_list1[x][2] = True
                            self.hit_counter2[(self.ship_list2[i][3] - 1)] += 1

            for pos in self.pos_list1:

                if pos[2] == True:          #Blits a red star to the screen if the selected tile coincides with the position of one of the enemy ships
                    gameDisplay.blit(redstar_img, (pos[0], pos[1]))

                elif pos[2] == False:       #Blits a blue star to the screen if the selected tile does not coincide with the position of one of the enemy ships
                    gameDisplay.blit(bluestar_img, (pos[0], pos[1]))

            gameDisplay.blit(player1_img, (self.table_x + 20, 0))

            if self.hit_counter2[0] == 5:   #Notifies Player 1 if Player 2's 5 tile ship has been sunk
                gameDisplay.blit(eship12_img, (self.enemytable_x + 7, self.enemytable_y + 54))
            else:
                gameDisplay.blit(eship11_img, (self.enemytable_x + 7, self.enemytable_y + 54))

            if self.hit_counter2[1] == 4:   #Notifies Player 1 if Player 2's 4 tile ship has been sunk
                gameDisplay.blit(eship22_img, (self.enemytable_x + 7, self.enemytable_y + 104))
            else:
                gameDisplay.blit(eship21_img, (self.enemytable_x + 7, self.enemytable_y + 104))

            if self.hit_counter2[2] == 3:   #Notifies Player 1 if Player 2's 3 tile ship has been sunk
                gameDisplay.blit(eship32_img, (self.enemytable_x + 7, self.enemytable_y + 144))
            else:
                gameDisplay.blit(eship31_img, (self.enemytable_x + 7, self.enemytable_y + 144))

            if self.hit_counter2[3] == 2:   #Notifies Player 1 if Player 2's 2 tile ship has been sunk
                gameDisplay.blit(eship42_img, (self.enemytable_x + 7, self.enemytable_y + 184))
            else:
                gameDisplay.blit(eship41_img, (self.enemytable_x + 7, self.enemytable_y + 184))

        if self.p2 == True:                 #Same funtionality as the if self.p1 == True statement but for Player 2

            for x in range (0, len(self.pos_list2)):
                for i in range (0, len(self.ship_list1)):

                    if self.ship_list1[i][0] - 20 <= self.pos_list2[x][0] <= self.ship_list1[i][0] + 20 and self.pos_list2[x][2] == False:
                        if self.ship_list1[i][1] - 20 <= self.pos_list2[x][1] <= self.ship_list1[i][1] + 20:
                            self.pos_list2[x][2] = True
                            self.hit_counter1[(self.ship_list1[i][3] - 1)] += 1

            for pos in self.pos_list2:
                if pos[2] == True:
                    gameDisplay.blit(redstar_img, (pos[0], pos[1]))
                elif pos[2] == False:
                    gameDisplay.blit(bluestar_img, (pos[0], pos[1]))

            gameDisplay.blit(player2_img, (self.table_x + 20, 0))

            if self.hit_counter1[0] == 5:
                gameDisplay.blit(eship12_img, (self.enemytable_x + 7, self.enemytable_y + 54))
            else:
                gameDisplay.blit(eship11_img, (self.enemytable_x + 7, self.enemytable_y + 54))

            if self.hit_counter1[1] == 4:
                gameDisplay.blit(eship22_img, (self.enemytable_x + 7, self.enemytable_y + 104))
            else:
                gameDisplay.blit(eship21_img, (self.enemytable_x + 7, self.enemytable_y + 104))

            if self.hit_counter1[2] == 3:
                gameDisplay.blit(eship32_img, (self.enemytable_x + 7, self.enemytable_y + 144))
            else:
                gameDisplay.blit(eship31_img, (self.enemytable_x + 7, self.enemytable_y + 144))

            if self.hit_counter1[3] == 2:
                gameDisplay.blit(eship42_img, (self.enemytable_x + 7, self.enemytable_y + 184))
            else:
                gameDisplay.blit(eship41_img, (self.enemytable_x + 7, self.enemytable_y + 184))

        if self.missile_selection == True:      #If missile selection menu is open

            if self.selection_x < cur[0] < self.selection_x + 171 and self.selection_y < cur[1] < self.selection_y + 116:

                if click[0] == 1:               #If player selects the Falcon missile
                    if grid.special_missile1 == False:
                        if grid.p1 == True and shop.p1_arsenal[0] > 0 or grid.p2 == True and shop.p2_arsenal[0] > 0:
                            grid.special_missile1 = True        #Enables the Falcon missile if the current player has any available
                            grid.special_missile2 = False
                            grid.special_missile3 = False
                            self.missile_active = True

                    elif grid.special_missile1 == True:
                        grid.special_missile1 = False

                    self.missile_counter += 1
                    self.missile_selection = False
                else:
                    gameDisplay.blit(missileselection1_img, (self.selection_x, self.selection_y))

            elif self.selection_x + 219 < cur[0] < self.selection_x + 399 and self.selection_y < cur[1] < self.selection_y + 116:

                if click[0] == 1:               #If the player selects the HawkH missile

                    if grid.special_missile2 == False:

                        if grid.p1 == True and shop.p1_arsenal[1] > 0 or grid.p2 == True and shop.p2_arsenal[1] > 0:
                            grid.special_missile2 = True        #Enables the HawkH missile if the current player has any available
                            grid.special_missile1 = False
                            grid.special_missile3 = False
                            self.missile_active = True

                    elif grid.special_missile2 == True:
                        grid.special_missile2 = False

                    self.missile_counter += 1
                    self.missile_selection = False

                else:
                    gameDisplay.blit(missileselection2_img, (self.selection_x, self.selection_y))

            elif self.selection_x + 439 < cur[0] < self.selection_x + 622 and self.selection_y < cur[1] < self.selection_y + 116:

                if click[0] == 1:               #If the player selects the HawkV missile

                    if grid.special_missile3 == False:
                        if grid.p1 == True and shop.p1_arsenal[2] > 0 or grid.p2 == True and shop.p2_arsenal[2] > 0:
                            grid.special_missile3 = True        #Enables the HawkV missile if the current player has any available
                            grid.special_missile1 = False
                            grid.special_missile2 = False
                            self.missile_active = True

                    elif grid.special_missile3 == True:
                        grid.special_missile3 = False

                    self.missile_counter += 1
                    self.missile_selection = False

                else:
                    gameDisplay.blit(missileselection3_img, (self.selection_x, self.selection_y))

            else:
                gameDisplay.blit(missileselection_img, (self.selection_x, self.selection_y))

        if self.t2_counter > 0:         #Sets a timer that shows the tutorial image 1.33 seconds after the counter is initiated
            self.t2_counter += 1

        if self.t2_counter == 40:
            gameDisplay.blit(tutorial2_img, (display_width/2 - self.tutorial2_width/2, display_height/2 - self.tutorial2_height/2))
            self.tutorial2 = True
            self.t2_counter = 0

        if self.hit_counter1 == [5,4,3,2] or self.hit_counter2 == [5,4,3,2]:        #Notifies the players that one of them has won and brings them to a new menu
            self.win = True

    def position_ships(self):

        gameDisplay.blit(grid_img, (self.x, self.y))        #Blits the grid to the screen
        gameDisplay.blit(table_img, (self.table_x, self.table_y))                       #Blits the table containing the current player's ships to the screen
        gameDisplay.blit(enemytable_img, (self.enemytable_x, self.enemytable_y))        #Blits the table containing the enemy player's ships to the screen

        if self.p1_ships == True:

            gameDisplay.blit(missiletable_img, (self.x, 0))     #Blits the missile table showing the player's special missile quantities to the screen
            missile_count(shop.p1_arsenal, self.x + 38, 37)     #Blits the missile numbers to the screen

            gameDisplay.blit(self.ship1_list[self.hit_counter1[0]], (self.table_x + 7, self.table_y + 54))          #Blits each of the player's ships to the
            gameDisplay.blit(self.ship2_list[self.hit_counter1[1]], (self.table_x + 7, self.table_y + 104))         #player table with only gray dots to
            gameDisplay.blit(self.ship3_list[self.hit_counter1[2]], (self.table_x + 7, self.table_y + 144))         #indicate that no damage has been received
            gameDisplay.blit(self.ship4_list[self.hit_counter1[3]], (self.table_x + 7, self.table_y + 184))         #so far
            gameDisplay.blit(player1_img, (self.table_x + 20, 0))

        elif self.p2_ships == True:     #Same functionality as the if self.p1_ships == True statement but for Player 2

            gameDisplay.blit(missiletable_img, (self.x, 0))
            missile_count(shop.p2_arsenal, self.x + 38, 37)

            gameDisplay.blit(self.ship1_list[self.hit_counter2[0]], (self.table_x + 7, self.table_y + 54))
            gameDisplay.blit(self.ship2_list[self.hit_counter2[1]], (self.table_x + 7, self.table_y + 104))
            gameDisplay.blit(self.ship3_list[self.hit_counter2[2]], (self.table_x + 7, self.table_y + 144))
            gameDisplay.blit(self.ship4_list[self.hit_counter2[3]], (self.table_x + 7, self.table_y + 184))
            gameDisplay.blit(player2_img, (self.table_x + 20, 0))

        gameDisplay.blit(eship11_img, (self.enemytable_x + 7, self.enemytable_y + 54))          #Blits each of the enemy ships to the enemy table
        gameDisplay.blit(eship21_img, (self.enemytable_x + 7, self.enemytable_y + 104))
        gameDisplay.blit(eship31_img, (self.enemytable_x + 7, self.enemytable_y + 144))
        gameDisplay.blit(eship41_img, (self.enemytable_x + 7, self.enemytable_y + 184))

        gameDisplay.blit(rotation_img, (0.55 * display_width, 7))       #Blits the rotation button to the screen

        if 0 < self.rotate_counter < 8:     #Sets a timer to ensure that the rotate button does not register another immediate click after it is clicked
            self.rotate_counter += 1

        elif self.rotate_counter == 8:
            self.rotate_counter = 0

        self.button(0.55 * display_width, 7, 0.55 * display_width + self.rotation_size, 7 + self.rotation_size, "rotate")       #Checks to see if the rotate button
                                                                                                                                #has been clicked and responds
        if self.ship_counter == 4:                                                                                              #accordingly
            if self.position_counter == 0:          #Registers that the current player has plotted all of their ships
                self.position_counter = 1

        if 0 < self.position_counter < 40:          #Sets a timer to allow the current player to acknowledge all of their current ships and their positions
            self.position_counter += 1              #before moving on to the next stage

        elif self.position_counter == 40:

            if self.p1_ships == True:               #Switches to Player 2 if Player 1 has finished plotting their ships

                self.position_counter = 0
                self.p1_ships = False               #Resets attributes for Player 2
                self.p2_ships = True
                self.ship_counter = 0
                self.list_switch = 1
                self.ship_orient = "Vertical"

                self.ship_x = display_width / 2 - grid_width / 2 + 2 - 100
                self.ship_y = display_height / 2 - grid_height / 2 + 16 + 16

            if self.p2_ships == True and len(self.ship_list2) > 0:      #Switches to the battle stage if Player 2 has finished plotting their ships

                self.position_counter = 0
                self.p2_ships = False
                self.ship_counter = 0

        for pos in [self.ship_list1, self.ship_list2][self.list_switch]:        #self.list_switch = 0 if Player 1's turn and equal to 1 if Player 2's Turn

            if pos[3] == 1 and pos[4] == "Front":                               #Blits the 5 tile ship to its current position based on its orientation
                if pos[2] == "Vertical":
                    gameDisplay.blit(ship_img, (pos[0], pos[1]))

                elif pos[2] == "Horizontal":
                    gameDisplay.blit(pygame.transform.rotate(ship_img, 90), (pos[0], pos[1]))

            if pos[3] == 2 and pos[4] == "Front":                               #Blits the 4 tile ship to its current position based on its orientation
                if pos[2] == "Vertical":
                    gameDisplay.blit(ship2_img, (pos[0], pos[1]))

                elif pos[2] == "Horizontal":
                    gameDisplay.blit(pygame.transform.rotate(ship2_img, 90), (pos[0], pos[1]))

            if pos[3] == 3 and pos[4] == "Front":                               #Blits the 3 tile ship to its current position based on its orientation
                if pos[2] == "Vertical":
                    gameDisplay.blit(ship3_img, (pos[0], pos[1]))

                elif pos[2] == "Horizontal":
                    gameDisplay.blit(pygame.transform.rotate(ship3_img, 90), (pos[0], pos[1]))

            if pos[3] == 4 and pos[4] == "Front":                               #Blits the 2 tile ship to its current position based on its orientation
                if pos[2] == "Vertical":
                    gameDisplay.blit(ship4_img, (pos[0], pos[1]))

                elif pos[2] == "Horizontal":
                    gameDisplay.blit(pygame.transform.rotate(ship4_img, 90), (pos[0], pos[1]))

        if self.ship_orient == "Vertical" and self.ship_counter < 4:    #Note that the ship is positioned back to the top left of the grid whenever it is rotated

            if self.ship_x > self.x + self.width - 10:      #Prevents the current ship from moving past the right edge of the grid
                self.ship_x = display_width / 2 - grid_width / 2 + self.offsetV_x[self.ship_counter] + self.increment * 9 - 100

            elif self.ship_x < self.x or self.rotate == True:       #Prevents the current ship from moving past the left edge of the grid
                self.ship_x = display_width / 2 - grid_width / 2 + self.offsetV_x[self.ship_counter] - 100

            if self.ship_y + self.ship_height[self.ship_counter] > self.y + self.height:        #Prevents the current ship from moving past the bottom of the grid
                self.ship_y = display_height / 2 - grid_height / 2 + self.offsetV_y[self.ship_counter] + self.increment * (5 + self.ship_counter) + 16

            elif self.ship_y < self.y or self.rotate == True:       #Prevents the current ship from moving past the top of the grid
                self.ship_y = display_height / 2 - grid_height / 2 + self.offsetV_y[self.ship_counter] + 16

            if self.rotate == True:     #Ensures that the ship only rotates once when the rotate button is clicked
                self.rotate = False

            if self.p1_ships == True or self.p2_ships == True:      #Blits the ship the currently being positioned in a lighter gray to the screen

                if self.ship_counter == 0:
                    gameDisplay.blit(shipT_img, (self.ship_x, self.ship_y))

                elif self.ship_counter == 1:
                    gameDisplay.blit(ship2T_img, (self.ship_x, self.ship_y))

                elif self.ship_counter == 2:
                    gameDisplay.blit(ship3T_img, (self.ship_x, self.ship_y))

                elif self.ship_counter == 3:
                    gameDisplay.blit(ship4T_img, (self.ship_x, self.ship_y))

        if self.ship_orient == "Horizontal" and self.ship_counter < 4:      #Considers a horizontal orientation instead of a vertical orientation for the current ship

            if self.ship_x + self.ship_height[self.ship_counter] > self.x + self.width:     #Prevents the ship from moving past the right edge of the grid
                self.ship_x = display_width / 2 - grid_width / 2 + self.offsetH_x[self.ship_counter] + self.increment * (5 + self.ship_counter) - 100

            elif self.ship_x < self.x or self.rotate == True:       #Prevents the ship from moving past the left edge of the grid
                self.ship_x = display_width / 2 - grid_width / 2 + self.offsetH_x[self.ship_counter] - 100

            if self.ship_y + self.ship_width[self.ship_counter] > self.y + self.height:     #Prevents the ship from moving past the bottom of the grid
                self.ship_y = display_height / 2 - grid_height / 2 + self.offsetH_y[self.ship_counter] + (self.increment - 0.5) * 9 + 16

            elif self.ship_y < self.y or self.rotate == True:       #Prevents the ship from moving past the top of the grid
                self.ship_y = display_height / 2 - grid_height / 2 + self.offsetH_y[self.ship_counter] + 16

            if self.rotate == True:     #Ensures that the ship only rotates once when the rotate button is clicked
                self.rotate = False

            if self.p1_ships == True or self.p2_ships == True:      #Blits the ship the currently being positioned in a lighter gray to the screen

                if self.ship_counter == 0:
                    gameDisplay.blit(pygame.transform.rotate(shipT_img, 90), (self.ship_x, self.ship_y))

                elif self.ship_counter == 1:
                    gameDisplay.blit(pygame.transform.rotate(ship2T_img, 90), (self.ship_x, self.ship_y))

                elif self.ship_counter == 2:
                    gameDisplay.blit(pygame.transform.rotate(ship3T_img,90), (self.ship_x, self.ship_y))

                elif self.ship_counter == 3:
                    gameDisplay.blit(pygame.transform.rotate(ship4T_img,90), (self.ship_x, self.ship_y))

        if self.t1_counter > 0:     #Initiates the Tutorial image 1.33 seconds after this counter is started
            self.t1_counter += 1

        if self.t1_counter == 40:       #Blits the Tutorial Image to the screen
            gameDisplay.blit(tutorial1_img, (display_width/2 - self.tutorial1_width/2, display_height/2 - self.tutorial1_height/2))
            self.tutorial1 = True
            self.t1_counter = 0

# INSTANCES #

grid = Grid()
shop = Shop()
main_menu = Main_Menu()
game_over = Game_Over()

# LOOPS #

def gameLoop():
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():        #Allows the user to quit by clicking the close button

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:      #Allows the user to move to the previous missile if the shop menu is open
                    if shop.run == True:
                        shop.type -= 1
                        if shop.type < 1:
                            shop.type = 1

                    else:           #Allows the user to move their ship to the left if they are in the position_ships stage
                        grid.ship_x -= grid.increment

                elif event.key == pygame.K_RIGHT:       #Allows the user to move to the next missile if the shop menu is open
                    if shop.run == True:
                        shop.type += 1
                        if shop.type > 3:
                            shop.type = 3

                    else:           #Allows the user to move their ship to the right if they are in the position_ships stage
                        grid.ship_x += grid.increment

                elif event.key == pygame.K_UP:      #Allows the user to move their ship up if they are in the position_ships stage

                    if grid.ship_orient == "Vertical":
                        grid.ship_y -= grid.increment

                    elif grid.ship_orient == "Horizontal":
                        grid.ship_y -= grid.increment - 0.5

                elif event.key == pygame.K_DOWN:    #Allows the user to move their ship down if they are in the position_ships stage

                    if grid.ship_orient == "Vertical":
                        grid.ship_y += grid.increment

                    elif grid.ship_orient == "Horizontal":
                        grid.ship_y += grid.increment - 0.5

                elif event.key == pygame.K_r:               #Allows the user to switch the orientation of the ship that they are currently positioning if they
                    if grid.ship_orient == "Vertical":      #press the R key
                        grid.ship_orient = "Horizontal"
                        grid.rotate = True

                    elif grid.ship_orient == "Horizontal":
                        grid.ship_orient = "Vertical"
                        grid.rotate = True

                elif event.key == pygame.K_RETURN:      #Allows the user to plot their ship if they press the ENTER key

                    grid.occupied = False       #Verifies that the occupied tiles of the ship that is being plotted do not coincide with any of current ship tiles

                    if grid.ship_orient == "Vertical":
                        for pos in [grid.ship_list1, grid.ship_list2][grid.list_switch]:
                            for i in range(5 - grid.ship_counter):      #Takes into account the number of tiles of the ship that it being plotted
                                if grid.ship_x - 20 <= pos[0] <= grid.ship_x + 20 and grid.ship_y - 20 <= pos[1] <= (grid.ship_y + grid.increment * i) + 20:
                                    # grid.occupied = True notifies that program that the player cannot plot their ship as it is on top
                                    # of at least one of their other ships
                                    grid.occupied = True

                    elif grid.ship_orient == "Horizontal":

                        for pos in [grid.ship_list1, grid.ship_list2][grid.list_switch]:
                            for i in range(5 - grid.ship_counter):
                                if grid.ship_x - 20 <= pos[0] <= (grid.ship_x + grid.increment * i) + 20 and grid.ship_y - 20 <= pos[1] <= grid.ship_y + 20:
                                    grid.occupied = True

                    if grid.occupied == False:      #grid.occupied = False notifies that program that the player can plot their current ship
                        grid.ship_counter += 1

                        if grid.p1_ships == True:       #Appends the positions of the ship that was recently plotted to the list of already occuped tile positions
                            grid.ship_list1.append((grid.ship_x, grid.ship_y, grid.ship_orient, grid.ship_counter, "Front"))        #Front indicates the first tile
                                                                                                                                    #of the ship
                        elif grid.p2_ships == True:
                            grid.ship_list2.append((grid.ship_x, grid.ship_y, grid.ship_orient, grid.ship_counter, "Front"))

                        if grid.ship_orient == "Vertical":

                            for x in range(1,6 - grid.ship_counter):    #The rest of the tile positions are appended to the position list based on the orientation
                                                                        #and length of the ship
                                if grid.p1_ships == True:
                                    grid.ship_list1.append((grid.ship_x, grid.ship_y + grid.increment * x, grid.ship_orient, grid.ship_counter, "Back"))

                                elif grid.p2_ships == True:
                                    grid.ship_list2.append((grid.ship_x, grid.ship_y + grid.increment * x, grid.ship_orient, grid.ship_counter, "Back"))

                        elif grid.ship_orient == "Horizontal":

                            for x in range(1,6 - grid.ship_counter):
                                if grid.p1_ships == True:
                                    grid.ship_list1.append((grid.ship_x + grid.increment * x, grid.ship_y, grid.ship_orient, grid.ship_counter, "Back"))
                                if grid.p2_ships == True:
                                    grid.ship_list2.append((grid.ship_x + grid.increment * x, grid.ship_y, grid.ship_orient, grid.ship_counter, "Back"))

                        grid.ship_orient = "Vertical"

                        if grid.ship_counter == 1:      #Brings the next ship to the top left of the grid after the previous ship has been plotted
                            grid.ship_x = display_width / 2 - grid_width / 2 + 5 - 100
                            grid.ship_y = display_height / 2 - grid_height / 2 + 16 + 16

                        elif grid.ship_counter == 2:
                            grid.ship_x = display_width / 2 - grid_width / 2 + 8 - 100
                            grid.ship_y = display_height / 2 - grid_height / 2 + 15 + 16

                        elif grid.ship_counter == 3:
                            grid.ship_x = display_width / 2 - grid_width / 2 + 8 - 100
                            grid.ship_y = display_height / 2 - grid_height / 2 + 14 + 16


        gameDisplay.fill(white)

        if main_menu.run == True:
            main_menu.render()

        elif shop.run == True:
            shop.render()

        elif grid.p1_ships == True or grid.p2_ships == True:
            grid.position_ships()

        elif grid.p1_ships == False and grid.p2_ships == False and game_over.run == False:
            grid.render()

        elif game_over.run == True:

            if grid.win == True:        #Brings the users to the game over menu once one of the players have won
                pygame.time.delay(3000)
                grid.win = False

            game_over.render()

        pygame.display.update()

        if grid.tutorial1 == True:      #Displays the tutorial images to the screen at the appropriate times
            pygame.time.delay(4000)
            grid.tutorial1 = False

        elif grid.tutorial2 == True:
            pygame.time.delay(4000)
            grid.tutorial2 = False

        clock.tick(30)

        if grid.win == True:        #Determines which of the players have won

            if grid.hit_counter1 == [5,4,3,2]:
                game_over.p2 = True
                game_over.run = True

            elif grid.hit_counter2 == [5,4,3,2]:
                game_over.p1 = True
                game_over.run = True

    pygame.quit()
    quit()

gameLoop()
