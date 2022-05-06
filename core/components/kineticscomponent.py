# coding= utf-8
from core.vector import *
from core.game import *

# Possibilitará a presença de cinética dentro de um gameobject
class KineticsComponent(Component):
    def __init__(self):
        super().__init__()
        self.velocity = Vector2(0, 0)
        self.setGravity()
        self.gravityActivated = True

    def setGravity(self, gravityForce = 9.8):
        self.gravityForce = Vector2(0, gravityForce * 100)

    def disableGravity(self):
        self.gravityActivated = False

    def enableGravity(self):
        self.gravityActivated = True

    def addForce(self, force):
        self.velocity += force

    def _update(self):
        position = Vector2(self.gameObject.x, self.gameObject.y)

        if(self.gravityActivated):
            self.velocity += self.gravityForce * Game.window.delta_time()

        self.gameObject.setPosition(position + self.velocity * Game.window.delta_time())