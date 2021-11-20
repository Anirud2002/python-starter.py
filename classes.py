# classes use Pascal naming convention
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('Move')

    def draw(self):
        print('draw')


# constructor is a function that gets called at the time of creating a object
point = Point(10, 20)
print(point.x)