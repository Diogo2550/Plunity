# coding= utf-8

# Classe dedicada à manipulação de vetores bi-dimensionais
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def normalize(self):
        vector = self.__normalize()
        self.x = vector.x
        self.y = vector.y

    def getNormalize(self):
        return self.__normalize()

    # Métodos privados
    def __normalize(self):
        return 1/(self.x**2 + self.y**2)**(1/2)

    def __add__(self, vector2):
        return Vector2(self.x + vector2.x, self.y + vector2.y)

    def __repr__(self):
        return f'({self.x},{self.y})'

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)