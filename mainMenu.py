import pygame 
import pygame_menu

pygame.init()

class mainMenu():
    def __init__(self):
        self.surface= pygame.display.set_mode((600,700))
        self.Continue = False

    def start_the_game(self):
        self.Continue = True
        self.menu.disable()

    def run(self):
        self.menu = pygame_menu.Menu("Welcome", 600, 700, theme=pygame_menu.themes.THEME_BLUE)
        self.menu.add.button('Play', self.start_the_game)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.surface)
        
