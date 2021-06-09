import pygame
import random
import time
pygame.mixer.init()
pygame.init()

# Initializing Display Screen
Screen_Width = 900
Screen_Height = 600
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("SNAKE AND FRUIT")
pygame.display.update()
Clock = pygame.time.Clock()
SnakeHead = pygame.image.load("SnakeHeadRight.png").convert_alpha()
Body = pygame.image.load("BodyHor.png").convert_alpha()
Tail = pygame.image.load("TailRight.png").convert_alpha()
Food = pygame.image.load("Apple.png").convert_alpha()
# Global Variable
Game_Exit = False
# Black = (0, 0, 0)
Red = (255, 0, 0)

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
    Plane = pygame.image.load("HomeScreen.png")
    SnakeLeft = pygame.image.load("HomeSnakeLeft.png")
    SnakeRight = pygame.image.load("HomeSnakeRight.png")
    SnakeUP = pygame.image.load("HomeSnakeUP.png")
    SnakeDown = pygame.image.load("HomeSnakeDown.png")
    Snake1 = SnakeRight
    Snake2 = SnakeLeft
    Snake_UX = -82
    Snake_LX = Screen_Width
    Snake_UY = 0
    Snake_LY = Screen_Height-82
    HomeScreen = ScreenTemplate(Screen, "HomeScreen.png", "HomeMusic.mp3", 0.4 , 0,0)
    # Home Screen Decoration
    while not Game_Exit:
        Screen.blit(Plane, (0,0))
        Screen.blit(Snake1, (Snake_UX,Snake_UY))
        Screen.blit(Snake2, (Snake_LX, Snake_LY))
        Snake_UX += 10
        Snake_LX -= 10
        if Snake_UX>Screen_Width-82:
            Snake_UX = Screen_Width-82
            Snake1 = SnakeDown
            Snake_UY += 10
            if Snake_UY>Screen_Height:
                Snake_UY = 0
                Snake1 = SnakeRight
                Snake_UX = -82
                Snake_UX += 10

        if Snake_LX<0:
            Snake_LX = 0
            Snake2 = SnakeUP
            Snake_LY -= 10
            if  Snake_LY < -82:
                Snake_LY = Screen_Height-82
                Snake2 = SnakeLeft
                Snake_LX = Screen_Width
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
    global Body
    global Tail
    global Food
    global Red
    Score = 0
    SnakeLength = 1
    Snake_X = Screen_Width/2
    Snake_Y = Screen_Height/2
    SnakeList = [[Snake_X,Snake_Y]]
    # Body_X = Snake_X-20
    # Body_Y = Snake_Y + 10 
    # Tail_X = Body_X-41
    # Tail_Y = Body_Y
    # Fixed Velocity of Snake
    Fix_Velocity_X = 10
    Fix_Velocity_Y = 10
    Velocity_X = 0
    Velocity_Y = 0
    # Position of food
    Food_X = random.randint(26,Screen_Width-76)
    Food_Y = random.randint(26,Screen_Height-79)
    fps = 60
    # Displaying main Game
    GameScreen = ScreenTemplate(Screen, "Grass.jpg", "Play.mp3", 0.4, 0,0)
    # Screen.blit(Body, (Body_X, Body_Y))
    # Screen.blit(Tail, (Tail_X, Tail_Y))
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
                    SnakeHead = pygame.image.load("SnakeHeadUp.png").convert_alpha()
                    # Tail = pygame.image.load("TailUp.png").convert_alpha()
                    # Body = pygame.image.load("BodyVer.png").convert_alpha() 
                elif event.key == pygame.K_DOWN:
                    Velocity_Y = +Fix_Velocity_Y
                    Velocity_X = 0
                    # Body = pygame.image.load("BodyVer.png").convert_alpha()
                    # Tail = pygame.image.load("TailDown.png").convert_alpha() 
                    SnakeHead = pygame.image.load("SnakeHeadDown.png").convert_alpha()
                elif event.key == pygame.K_LEFT:
                    Velocity_X = -Fix_Velocity_X
                    Velocity_Y = 0
                    # Body = pygame.image.load("BodyHor.png").convert_alpha()
                    # Tail = pygame.image.load("TailLeft.png").convert_alpha()
                    SnakeHead = pygame.image.load("SnakeHeadLeft.png").convert_alpha()
                elif event.key == pygame.K_RIGHT:
                    Velocity_X = +Fix_Velocity_X
                    Velocity_Y = 0                
                    # Body = pygame.image.load("BodyHor.png").convert_alpha()
                    # Tail = pygame.image.load("TailRight.png").convert_alpha()
                    SnakeHead = pygame.image.load("SnakeHeadRight.png").convert_alpha()    
                elif event.key == pygame.K_ESCAPE:
                    Home_Screen()
        Snake_X += Velocity_X
        Snake_Y += Velocity_Y        
        Screen.blit(pygame.image.load("Grass.jpg"),(0,0))
            
        if abs(Snake_X-Food_X)<15 and abs(Snake_Y-Food_Y)<15:
            Food_X = random.randint(26,Screen_Width-76)
            Food_Y = random.randint(26,Screen_Height-79)
            Score += 10
            SnakeLength +=1
        Screen.blit(Food, (Food_X, Food_Y))            
        Screen.blit(SnakeHead, (Snake_X, Snake_Y))
        pygame.display.update()
        Clock.tick(fps)
        if Snake_X<25 or Snake_X>(Screen_Width-85) or Snake_Y<25 or Snake_Y>(Screen_Height-85):
            # Game_Over = True
            End_Screen()
            

def End_Screen(): # Feature addition under progress
    SettingScreen = ScreenTemplate(Screen, "Grass 1.jpg", "Settings.mp3", 0.4, 0,0)
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

Screen.blit(pygame.image.load("Presenter.jpg"), (0,0))
pygame.display.update()
# time.sleep(1)
Home_Screen()
pygame.quit()
quit()

