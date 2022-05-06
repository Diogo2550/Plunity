# coding= utf-8
from core.pplay.gameobject import GameObject as GameObjectP
from core.component import *

# Classe customizada para manipula��o de gameobjects
class GameObject(GameObjectP):
    def __init__(self):
        super().__init__()
        self.components = []

    def addComponent(self, component):
        if(isinstance(component, Component)):
            component.setGameObject(self)
            self.components.append(component)
        else:
            raise Exception(f"Instancia da classe {component.__class__} nao pertence ao tipo Component.")

    def getComponent(self, componentType):
        for component in self.components:
            if(isinstance(component, componentType)):
                return component

    def start(self):
        for component in self.components:
            component.start()
        self._start()

    def update(self):
        for component in self.components:
            component.update()

        self._update()
        self._afterUpdated()

    def setPosition(self, position):
        self.x = position.x
        self.y = position.y

    def _afterUpdated(self):
        pass

    def _update(self):
        pass

    def _start(self):
        pass