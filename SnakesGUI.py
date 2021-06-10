import pygame
import random
import time
pygame.mixer.init()
pygame.init()

# Initializing Display Screen
SW = 900
SH = 600
Screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("SNAKE AND FRUIT")
pygame.display.update()
Clock = pygame.time.Clock()
SnakeHead = pygame.image.load("Contents\\SnakeHeadRight.png").convert_alpha()
Food = pygame.image.load("Contents\\Apple.png").convert_alpha()
# Global Variable
Game_Exit = False
# Black = (0, 0, 0)


class ScreenTemplate:

    def __init__(self, Screen, BackgroundImg, BackgroundsMusic, Volume, BoundaryX, BoundaryY ):
       
        self.Window = Screen
        self.BgI = BackgroundImg
        self.Bgm = BackgroundsMusic 
        self.V = Volume
        self.X = BoundaryX
        self.Y = BoundaryY
        pygame.mixer.music.load(self.Bgm)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(self.V)
        self.Window.blit(pygame.image.load(self.BgI), (self.X, self.Y))
        pygame.display.update()
        
# Event Handling        
def Home_Screen(): # Completed! Pic editing required
    """The Main Game Takes Place Here"""
    global Game_Exit
    global SnakeHead
    global Clock
    Red = (255, 0, 0)
    Plane = pygame.image.load("Backgrounds\\HomeScreen.png")
    SnakeLeft = pygame.image.load("Contents\\HomeSnakeLeft.png")
    SnakeRight = pygame.image.load("Contents\\HomeSnakeRight.png")
    SnakeUP = pygame.image.load("Contents\\HomeSnakeUP.png")
    SnakeDown = pygame.image.load("Contents\\HomeSnakeDown.png")
    Snake1 = SnakeRight
    Snake2 = SnakeLeft
    Snake_UX = -82
    Snake_LX = SW
    Snake_UY = 0
    Snake_LY = SH-82
    HomeScreen = ScreenTemplate(Screen, "Backgrounds\\HomeScreen.png", "Sounds\\HomeMusic.mp3", 0.4 , 0,0)
    # Home Screen Decoration
    while not Game_Exit:
        Screen.blit(Plane, (0,0))
        # MPos = pygame.mouse.get_pos()
        # MX = MPos[0]
        # MY = MPos[1]
        # pygame.draw.rect(Screen, Red, (SW/8, SH/2.4, 675,65), 2)
        Screen.blit(Snake1, (Snake_UX,Snake_UY))
        Screen.blit(Snake2, (Snake_LX, Snake_LY))
        Snake_UX += 10
        Snake_LX -= 10
        if Snake_UX>SW-82:
            Snake_UX = SW-82
            Snake1 = SnakeDown
            Snake_UY += 10
            if Snake_UY>SH:
                Snake_UY = 0
                Snake1 = SnakeRight
                Snake_UX = -82
                Snake_UX += 10

        if Snake_LX<0:
            Snake_LX = 0
            Snake2 = SnakeUP
            Snake_LY -= 10
            if  Snake_LY < -82:
                Snake_LY = SH-82
                Snake2 = SnakeLeft
                Snake_LX = SW
                Snake_LX -= 10 
        pygame.display.update()  
        Clock.tick(60) 

        #Handling all Action
        for event in pygame.event.get():
                    
            if event.type == pygame.QUIT:
                GameEnd()  

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Game_Screen()

def Game_Screen(): # Condition defining left
    global Game_Exit
    global SnakeHead
    global Food
    # global Red
    Score = 0
    SnakeLength = 1
    Snake_X = SW/2
    Snake_Y = SH/2
    # SnakeList = [[Snake_X,Snake_Y]]
    # Fixed Velocity of Snake
    Fix_Velocity_X = 10
    Fix_Velocity_Y = 10
    Velocity_X = 0
    Velocity_Y = 0
    # Position of food
    Food_X = random.randint(26,SW-76)
    Food_Y = random.randint(26,SH-79)
    fps = 60
    # Displaying main Game
    GameScreen = ScreenTemplate(Screen, "Backgrounds\\Grass.jpg", "Sounds\\Play.mp3", 0.4, 0,0)
    Screen.blit(SnakeHead, (Snake_X, Snake_Y))
    Screen.blit(Food, (Food_X, Food_Y))
    pygame.display.update()
    while not Game_Exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameEnd()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Velocity_Y = -Fix_Velocity_Y
                    Velocity_X =0
                    SnakeHead = pygame.image.load("Contents\\SnakeHeadUp.png").convert_alpha()
                elif event.key == pygame.K_DOWN:
                    Velocity_Y = +Fix_Velocity_Y
                    Velocity_X = 0
                    SnakeHead = pygame.image.load("Contents\\SnakeHeadDown.png").convert_alpha()
                elif event.key == pygame.K_LEFT:
                    Velocity_X = -Fix_Velocity_X
                    Velocity_Y = 0
                    SnakeHead = pygame.image.load("Contents\\SnakeHeadLeft.png").convert_alpha()
                elif event.key == pygame.K_RIGHT:
                    Velocity_X = +Fix_Velocity_X
                    Velocity_Y = 0                

                    SnakeHead = pygame.image.load("Contents\\SnakeHeadRight.png").convert_alpha()    
                elif event.key == pygame.K_ESCAPE:
                    Home_Screen()
        Snake_X += Velocity_X
        Snake_Y += Velocity_Y        
        Screen.blit(pygame.image.load("Backgrounds\\Grass.jpg"),(0,0))
            
        if abs(Snake_X-Food_X)<15 and abs(Snake_Y-Food_Y)<15:
            Food_X = random.randint(26,SW-76)
            Food_Y = random.randint(26,SH-79)
            Score += 10
            SnakeLength +=1
        Screen.blit(Food, (Food_X, Food_Y))            
        Screen.blit(SnakeHead, (Snake_X, Snake_Y))
        pygame.display.update()
        Clock.tick(fps)
        if Snake_X<25 or Snake_X>(SW-85) or Snake_Y<25 or Snake_Y>(SH-85):
            # Game_Over = True
            End_Screen()
            

def End_Screen(): # Feature addition under progress
    SettingScreen = ScreenTemplate(Screen, "Backgrounds\\Grass.jpg", "Sounds\\Settings.mp3", 0.4, 0,0)
    while not Game_Exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameEnd()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Home_Screen()
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_ESCAPE:
                    Home_Screen()

def GameEnd(): # Completed! May require feature addition
    """End the Gameloop() and GameWin"""
    global Game_Exit
    Game_Exit = True

Screen.blit(pygame.image.load("Backgrounds\\Presenter.jpg"), (0,0))
pygame.display.update()
pygame.time.delay(1)
Home_Screen()
pygame.quit()
quit()

