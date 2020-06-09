class Punto():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            raise ValueError
        self._x = x

    @property
    def y(self, x):
        return self._y

    @y.setter
    def y(self, y):
        if y < 0:
            raise ValueError
        self._y = y

    def __str__(self):
        return "(%d, %d)" % (self._x, self._y)
