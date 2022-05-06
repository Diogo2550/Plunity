# coding= utf-8
from core.components.kineticscomponent import KineticsComponent
from core.gameobject import *
from core.vector import Vector2
from core.game import *

# Classe responsável por representar a bola do Pong
class Ball(GameObject):
    def __init__(self):
        super().__init__()
        self.moveSpeedBase = 320
        pass

    def _start(self):
        # Seta o tamanho do gameobject a partir do tamanho do Sprite
        self.width = self.getComponent(SpriteComponent).sprite.width
        self.height = self.getComponent(SpriteComponent).sprite.height

        # Ajusta os parâmetros de movimentação
        self.kinetics = self.getComponent(KineticsComponent)
        self.kinetics.disableGravity()
        self.kinetics.addForce(Vector2(self.moveSpeedBase, self.moveSpeedBase))

        # Seta a posição inicial para o centro da tela
        self.setPosition(Vector2(
            Game.window.width / 2 - self.width / 2,
            Game.window.height / 2 - self.height / 2
        ))

    def _update(self):
        windowWidth = Game.window.width;
        windowHeight = Game.window.height;
        position = Vector2(self.x, self.y)
        speed = self.kinetics.velocity

        if(position.x >= windowWidth - self.width):
            speed.x = -abs(speed.x)

        if(position.x <= 0):
            speed.x = abs(speed.x)

        if(position.y >= windowHeight - self.height):
            speed.y = -abs(speed.y)

        if(position.y <= 0):
            speed.y = abs(speed.y)

        self.kinetics.velocity = speed