import pygame 
import pygame_menu 
from clicks import *
from idle import *
from money import moneyFunctions as money
from startMenu import startMenu as menuSTART



pygame.init()
pygame.display.set_caption("Potion Clicker")

class Game():
    def __init__(self):
        self.menuLoader = True
        self.clock = pygame.time.Clock()
        self.money = money() 
        self.menu = menuSTART()
        self.clicks = clicks()
        self.idle = idle()
        self.width = 600
        self.height = 700
        self.FPS = 60
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.counter = 0

        self.canClick = True

        #Money Setup
        
        self.clicks.setAmountPerClick(1)
        self.money.setMoneyAmount(0)
        self.idleAmount = self.idle.setAmountPerIdle(0)
        self.balance = self.money.getMoneyAmount()

    def textPrinter(self, txt, size:int):
        font = pygame.font.Font('freesansbold.ttf', int(size))
        text = font.render(str(txt), True, (0,0,0))
        textRect = text.get_rect()
        return text, textRect

    def moneyPrinter(self):
        text, textRect = self.textPrinter(f"Potions {self.balance}", 32)
        textRect.center = ((self.width // 2) , self.height - (self.height // 1.15))
        self.screen.blit(text, textRect)

    def buttonMaker(self):
        self.button1 = pygame.draw.rect(self.screen, (255, 0, 0), (self.width // 4 - 50,550,100,100))
        self.button2 = pygame.draw.rect(self.screen, (255, 0, 0), (self.width // 2 - 50,550,100,100))
        self.button3 = pygame.draw.rect(self.screen, (255, 0, 0), (self.width // 2 + 100 ,550,100,100))

        buttons = [self.button1, self.button2, self.button3]
        buttonsText = ["Clicks", "Idle", "Save"]

        for i in range(len(buttons)):
            text_surface = pygame.font.SysFont('freesansbold.ttf', 28).render(buttonsText[i], True, (255,255,0))
            text_rect = text_surface.get_rect(center=buttons[i].center)
            self.screen.blit(text_surface, text_rect)


    def run(self):
        self.menu.run() #Runs The Main Menu

        #Running Main Event Loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise SystemExit
        
            #Clicking Functions
            self.mousePos = pygame.mouse.get_pos()
            self.mouseClick = pygame.mouse.get_pressed()[0]

            if self.mouseClick == False:
                self.canClick = True
            if self.mouseClick == True and self.canClick == True and not self.button1.collidepoint(self.mousePos) and not self.button2.collidepoint(self.mousePos) and not self.button3.collidepoint(self.mousePos):
                self.balance = self.balance + self.clicks.getAmountPerClick()
                self.canClick = False
            elif self.mouseClick and self.button1.collidepoint(self.mousePos) and self.canClick:
                self.canClick = False
                print("Here")

            #Screen Functions
            self.screen.fill((173,216,230))
            self.clock.tick(self.FPS)
            self.counter += 1

            #Idle Functions
            if self.counter == 60:
                self.balance = self.balance + self.idle.getAmountPerIdle()
                self.counter = 0


            #Definitions Go Here
            self.moneyPrinter()
            self.buttonMaker()

            #Last Line For Updating Display
            pygame.display.update()
    
Game().run()