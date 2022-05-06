# coding= utf-8
from core.component import *
from core.pplay.sprite import *

# Adicionará sprites aos gameobjects
class SpriteComponent(Component):
    def __init__(self, spritePath):
        super().__init__()
        self.sprite = Sprite(spritePath)
    
    def _update(self):
        pass

    def draw(self):
        self.sprite.x = self.gameObject.x
        self.sprite.y = self.gameObject.y
        
        self.sprite.draw()
