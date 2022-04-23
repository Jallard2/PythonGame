import pygame 
import pygame_menu 
from clicks import *
from idle import *
from money import moneyFunctions as money
from mainMenu import mainMenu as menu



pygame.init()
pygame.display.set_caption("Potion Clicker")

class Game():
    def __init__(self):
        self.menuLoader = True

        self.money = money() 
        self.menu = menu()
        self.width = 600
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.balance = self.money.getMoneyAmount()
    
    def run(self):
        self.menu.run()

        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise SystemExit

            self.screen.fill((60,25,60))
            pygame.display.update()
    
Game().run()