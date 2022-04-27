import pygame 
import pygame_menu


pygame.init()

class idleMenu():
    def __init__(self,idle,money ):
        self.idle = idle
        self.money = money
        self.surface= pygame.display.set_mode((600,700))
        self.Continue = False

        self.costOne = 25 
        self.costFive = 100
        self.costTwentyFive = 1000

    def start_the_game(self):
        self.Continue = True
        self.menu.disable()

    def upgradeBy1(self):
        if (self.money.getMoneyAmount() - self.costOne < 0):
            return
        self.money.purchaseUpgrade(self.costOne)
        self.costOne *= 2
        self.currentAmountPerIdle = self.idle.getAmountPerIdle()
        self.currentAmountPerIdle += 1
        self.idle.setAmountPerIdle(self.currentAmountPerIdle)
        self.menu.disable()
    
    def upgradeBy5(self):
        if (self.money.getMoneyAmount() - self.costFive < 0):
            return
        self.money.purchaseUpgrade(self.costFive)
        self.costFive *= 2
        self.currentAmountPerIdle = self.idle.getAmountPerIdle()
        self.currentAmountPerIdle += 5
        self.idle.setAmountPerIdle(self.currentAmountPerIdle)
        self.menu.disable()
    
    def upgradeBy25(self):
        if (self.money.getMoneyAmount() - self.costTwentyFive < 0):
            return
        self.money.purchaseUpgrade(self.costTwentyFive)
        self.costTwentyFive *= 2
        self.currentAmountPerIdle = self.idle.getAmountPerIdle()
        self.currentAmountPerIdle += 25
        self.idle.setAmountPerIdle(self.currentAmountPerIdle)
        self.menu.disable()



    def run(self):
        self.menu = pygame_menu.Menu("Upgrade Potions Earned Per Seconds", 600, 700, theme=pygame_menu.themes.THEME_BLUE)
        self.menu.add.button(f'Upgrade By 1 (Cost: {self.costOne})', self.upgradeBy1)
        self.menu.add.button(f'Upgrade By 5 (Cost: {self.costFive})', self.upgradeBy5)
        self.menu.add.button(f'Upgrade By 25 (Cost: {self.costTwentyFive})', self.upgradeBy25)
        self.menu.add.button('Back To Game', self.start_the_game)
        self.menu.mainloop(self.surface)
