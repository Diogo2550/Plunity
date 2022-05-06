# coding= utf-8
from core.pplay.window import *
from core.components.spritecomponent import *
from core.pplay.gameimage import *


class Game:

    # Configurações da janela
    WINDOW_TITLE = 'Pong'
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 600

    SPEED_MULTIPLIER = 1

    window = None

    def __init__(self):
        self.gameObjects = []
        self.player = None
        self.__bootstrap()

    def addGameObject(self, gameObject):
        self.gameObjects.append(gameObject)

    def setBackground(self, backgroundPath):
        self.background = GameImage(backgroundPath)

    def setPlayer(self, player):
        self.player = player

    def start(self):
        for gameObject in self.gameObjects:
            gameObject.start()

        while(True):
            # Inputs


            # Update
            for gameObject in self.gameObjects:
                gameObject.update()

            # Desenho
            try:
                self.background.draw()
            except Exception:
                Game.window.set_background_color((0, 0, 0))                

            for gameObject in self.gameObjects:
                spriteComponent = gameObject.getComponent(SpriteComponent)
                if(spriteComponent != None):
                    spriteComponent.draw()

            Game.window.update()

    def getKeyboard():
        return Game.window.get_keyboard()

    def getMouse():
        return Game.window.get_mouse()

    def __bootstrap(self):
        window = Window(Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT)
        window.set_title(Game.WINDOW_TITLE)

        Game.window = window
