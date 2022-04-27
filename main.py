import pygame 
import pygame_menu 
from clicks import *
from idle import *
from money import moneyFunctions as money
from prestige import prestigeFunctions as prestige
from startMenu import startMenu as menuSTART
from clicksMenu import clicksMenu
from idleMenu import idleMenu
from prestigeMenu import prestigeMenu
import json



pygame.init()
pygame.display.set_caption("Potion Clicker")

class Game():
    def __init__(self):
        self.pathToData = r'data.json'
        self.prestige = prestige()
        self.clock = pygame.time.Clock()
        self.money = money() 
        self.menu = menuSTART()
        self.clicks = clicks()
        self.idle = idle()
        self.prestigeMenu = prestigeMenu(self.prestige, self.money, self.clicks, self.idle)
        self.clicksMenu = clicksMenu(self.clicks, self.money)
        self.idleMenu = idleMenu(self.idle, self.money)
        self.width = 600
        self.height = 700
        self.FPS = 60
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.imageCounter = 4
        self.imageDisplayCounter = 0
        self.counter = 0

        

        self.canClick = True

        #Money Setup
        
        self.clicks.setAmountPerClick(1)
        self.money.setMoneyAmount(0)
        self.idleAmount = self.idle.setAmountPerIdle(0)
        self.balance = self.money.getMoneyAmount()

    def textPrinter(self, txt, size:int):
        try:
            font = pygame.font.Font('freesansbold.ttf', int(size))
        except Exception as e:
            font = pygame.font.Font(r'freesansbold.tff', int(size))
        text = font.render(str(txt), True, (0,0,0))
        textRect = text.get_rect()
        return text, textRect

    def moneyPrinter(self):
        text, textRect = self.textPrinter(f"Potions {self.balance}", 32)
        textRect.center = ((self.width // 2) , self.height - (self.height // 1.15))
        self.screen.blit(text, textRect)
    
    def clicksAmountPrinter(self):
        text, textRect = self.textPrinter(f"Potions Per Click {self.clicks.getAmountPerClick()}", 26)
        textRect.center = ((self.width // 2) , self.height - (self.height // 1.15) + 30)
        self.screen.blit(text, textRect)

    def idleAmountPrinter(self):
        text, textRect = self.textPrinter(f"Potions Per Second {self.idle.getAmountPerIdle()}", 26)
        textRect.center = ((self.width // 2) , self.height - (self.height // 1.15) + 60)
        self.screen.blit(text, textRect)


    def buttonMaker(self):
        self.button1 = pygame.draw.rect(self.screen, (255, 0, 0), (self.width // 4 - 50,550,100,100))
        self.button2 = pygame.draw.rect(self.screen, (255, 0, 0), (self.width // 2 - 50,550,100,100))
        self.button3 = pygame.draw.rect(self.screen, (255, 0, 0), (self.width // 2 + 100 ,550,100,100))

        buttons = [self.button1, self.button2, self.button3]
        buttonsText = ["Clicks", "Idle", "Prestige"]

        for i in range(len(buttons)):
            try:
                font, size = 'freesansbold.ttf', 28
            except Exception as e:
                font, size = r'freesansbold.tff', 28
            text_surface = pygame.font.SysFont(font, size).render(buttonsText[i], True, (255,255,0))
            text_rect = text_surface.get_rect(center=buttons[i].center)
            self.screen.blit(text_surface, text_rect)


    def saveFunction(self):
        with open(self.pathToData, 'r') as f:
            jsondata = json.load(f)
            data = {1:[self.money.getMoneyAmount(), self.clicks.getAmountPerClick(), self.idle.getAmountPerIdle(), self.prestige.getPrestigeModifier()]}
        with open(self.pathToData, 'w') as f:
            json.dump(data,f)

    def loadFunction(self):
        try:
            with open(self.pathToData, 'r') as f:
                jsondata = json.load(f)
            if (jsondata != {}):
                self.money.setMoneyAmount(jsondata["1"][0])
                self.clicks.setAmountPerClick(jsondata["1"][1])
                self.idle.setAmountPerIdle(jsondata["1"][2])
                self.prestige.setPrestigeModifier(jsondata["1"][3])
        except FileNotFoundError as e:
            with open(self.pathToData, 'w') as f:
                f.write("{}")
            


    def run(self):
        self.menu.run() #Runs The Main Menu
        self.loadFunction()
        #Running Main Event Loop
        while True:
            self.balance = self.money.getMoneyAmount()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.saveFunction()
                    raise SystemExit
        
            #Clicking Functions
            self.mousePos = pygame.mouse.get_pos()
            self.mouseClick = pygame.mouse.get_pressed()[0]

            if self.mouseClick == False:
                self.canClick = True
            if self.mouseClick == True and self.canClick == True and not self.button1.collidepoint(self.mousePos) and not self.button2.collidepoint(self.mousePos) and not self.button3.collidepoint(self.mousePos):
                self.balance = self.balance + self.clicks.getAmountPerClick() * self.prestige.getPrestigeModifier()
                self.money.setMoneyAmount(self.balance)
                self.canClick = False
            elif self.mouseClick and self.button1.collidepoint(self.mousePos) and self.canClick:
                self.canClick = False
                self.clicksMenu.run()
            elif self.mouseClick and self.button2.collidepoint(self.mousePos) and self.canClick:
                self.canClick = False
                self.idleMenu.run()
            elif self.mouseClick and self.button3.collidepoint(self.mousePos) and self.canClick:
                self.canClick = False
                self.prestigeMenu.run()
                

            #Screen Functions
            self.screen.fill((173,216,230))
            self.clock.tick(self.FPS)
            self.counter += 1
            self.imageCounter += 1

            #Idle Functions
            if self.imageCounter == 5:
                imagesToLoad = [r'potionGif\frame0.png',r'potionGif\frame1.png',r'potionGif\frame2.png',r'potionGif\frame3.png',r'potionGif\frame4.png',r'potionGif\frame5.png',r'potionGif\frame6.png',r'potionGif\frame7.png',r'potionGif\frame8.png']
                #print(self.imageDisplayCounter)
                image = pygame.image.load(imagesToLoad[self.imageDisplayCounter])
                

                if self.imageDisplayCounter == 8:
                    self.imageDisplayCounter = 0
                else:
                    self.imageDisplayCounter += 1
                self.imageCounter = 0
            self.screen.blit(image, (self.width//2 - 85 ,250))

            if self.counter == 60:
                self.balance = self.balance + self.idle.getAmountPerIdle() * self.prestige.getPrestigeModifier()
                self.money.setMoneyAmount(self.balance)
                self.counter = 0


            #Definitions Go Here
            self.moneyPrinter()
            self.clicksAmountPrinter()
            self.idleAmountPrinter()
            self.buttonMaker()

            #Last Line For Updating Display
            pygame.display.update()
    
Game().run()