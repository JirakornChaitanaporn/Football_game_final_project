import Object
import Footballer_Database
import turtle

class FootballerPlayer(Object.Object):
    def __init__(self, salah_data, my_turtle):
        super().__init__("Liverpool", salah_data)
        self.speed = 5
        self._pos = 11
        self.x = 50
        self.y = 180
        self.width = 40
        self.height = 40
        self.location = [self.x, self.y]
        self.screen = turtle.Screen()
        self.salah = my_turtle
        self.salah.penup()
        self.salah.setheading(180)
        self.salah.hideturtle()
    
    def draw(self):
        self.salah.color(self.color)
        self.salah.goto(self.location[0], self.location[1] - self.height/2)
        self.salah.forward(self.width/2)
        self.salah.pendown()
        self.salah.begin_fill()
        for _ in range(2):
            self.salah.left(90)
            self.salah.forward(self.height)
            self.salah.left(90)
            self.salah.forward(self.width)
        self.salah.end_fill()
        self.salah.penup()
        self.salah.goto(self.location[0], self.location[1])
        turtle.write(str('11'), align="center", font=("Arial", 12, "bold"))

    def clear(self):
        self.salah.clear()

    def set_location(self, location):
        self.location = location
        self.salah.goto(self.location[0], self.location[1])