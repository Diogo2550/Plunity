# coding= utf-8

# Classe que representa um comportamento de um gameobject.
class Component:
    def __init__(self):
        pass

    def start(self):
        pass

    def update(self):
        self._update()
        self.afterUpdated()

    def afterUpdated(self):
        pass

    def setGameObject(self, gameObject):
        self.gameObject = gameObject
    
    def _update(self):
        raise NotImplementedError("O metodo deve ser sobrescrito")