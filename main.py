# coding= utf-8

from core.components.kineticscomponent import *
from core.game import *
from gameobjects.ball import Ball

game = Game()

gameObjects = []

# Instanciação de gameobjects
ball = Ball()
ballSprite = SpriteComponent('assets/images/ball.png')
ballKinetics = KineticsComponent()

ball.addComponent(ballSprite)
ball.addComponent(ballKinetics)

# Inserção dos gameobjects no jogo
game.addGameObject(ball)

# Iniciação do game loop
game.start()