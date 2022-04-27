import pygame 
import pygame_menu



pygame.init()

class prestigeMenu():
    def __init__(self, prestige, money, clicks, idle):
        self.surface= pygame.display.set_mode((600,700))
        self.Continue = False

        self.money = money
        self.clicks = clicks
        self.idle = idle
        self.prestigeModifierFunctions = prestige

        if self.prestigeModifierFunctions.getPrestigeModifier() == 1:
            self.cost = 10000
        elif self.prestigeModifierFunctions.getPrestigeModifier() == 2:
            self.cost = 50000
        elif self.prestigeModifierFunctions.getPrestigeModifier() == 5:
            self.cost = 150000


    def start_the_game(self):
        self.Continue = True
        self.menu.disable()

    def prestige(self):
        #Conditions Go Here
        if self.prestigeModifierFunctions.getPrestigeModifier() == 1:
            if self.money.getMoneyAmount() >= self.cost:
                #Function For Increasing This Goes Where The +1 Is
                self.prestigeModifier = self.prestigeModifierFunctions.getPrestigeModifier()
                self.prestigeModifierFunctions.setPrestigeModifier(self.prestigeModifier + 1)
                self.money.setMoneyAmount(0)
                self.idle.setAmountPerIdle(0)
                self.clicks.setAmountPerClick(1)
                self.menu.disable()

        if self.prestigeModifierFunctions.getPrestigeModifier() == 2:
            if self.money.getMoneyAmount() >= self.cost:
                #Function For Increasing This Goes Where The +1 Is
                self.prestigeModifier = self.prestigeModifierFunctions.getPrestigeModifier()
                self.prestigeModifierFunctions.setPrestigeModifier(self.prestigeModifier + 3)
                self.money.setMoneyAmount(0)
                self.idle.setAmountPerIdle(0)
                self.clicks.setAmountPerClick(1)
                self.menu.disable()
        
        if self.prestigeModifierFunctions.getPrestigeModifier() == 5:
            if self.money.getMoneyAmount() >= self.cost:
                #Function For Increasing This Goes Where The +1 Is
                self.prestigeModifier = self.prestigeModifierFunctions.getPrestigeModifier()
                self.prestigeModifierFunctions.setPrestigeModifier(self.prestigeModifier + 5)
                self.money.setMoneyAmount(0)
                self.idle.setAmountPerIdle(0)
                self.clicks.setAmountPerClick(1)
                self.menu.disable()


    def run(self):
        self.menu = pygame_menu.Menu("Prestige Menu", 600, 700, theme=pygame_menu.themes.THEME_BLUE)
        self.menu.add.label("Would You Like To Prestige?")
        self.menu.add.button(f"Yes (Cost: {self.cost})", self.prestige)
        self.menu.add.button("No", self.start_the_game)
        #self.menu.add.button('Back To Game', self.start_the_game)
        self.menu.mainloop(self.surface)
