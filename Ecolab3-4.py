class Colored(Point):

    colors = ["red","blue", "green", "yellow", "purple", "yellow", "purple"]

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        if color in self.COLORS:
            self.color = color
        else:
            raise Exception(f"that is an invalid color. Accepted colors are {self.COLORS}")


    def __str__(self):
        return f"{self.color}({self.x}, {self.y})"

p1 = ColoredPoint(10,10, "red")
p2 = ColoredPoint(5,5, "poker")


for _ in range(5):
    colored_points.append(
        ColoredPoint(random.randint(-100, 100),
                     random.randint(-100, 100),
                     random.randint(ColoredPoint.COLORS),
                     )
    )
print(colored_points)

p1.add_extra_color("orange")
p2 = ColoredPoint( 5, 5, "orange")
print(p2)


@classmethod
def add_extra_color(cls, color):
    cls.COLORS.append(color)

@property
def distance_origin(self):
    result = self.x**2 + self.y**2)**0.5
    if result == int(result):
        return int(result)
else:
return result