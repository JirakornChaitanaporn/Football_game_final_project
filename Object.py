import random
import Footballer_Database
import turtle
import math

liverpool = Footballer_Database.Footballer_Database()
opponent = Footballer_Database.Footballer_Database()

class Object:
    def __init__(self, team, player_database = None):
        # team_list = ['Alison', 'Trent', 'Van_dilk', 'Konate', 'Andy', 'Sbo', 'Mac A', 'Jones', 'Nunez', 'diaz']
        # name_i = random.randint(0,9)
        # self._name = team_list[name_i]
        self.team = team
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.pos = 0
        self.mass = 89
        self.x = 0
        self.y = 0
        self.count = 0
        self.vx = 5
        self.vy = 5
        self.isGK = False
            
        # self.is_ball_collide = False
        self.size = 20
        
        if team == "Liverpool":
            self.color = (200, 16, 46)
            while player_database.pos_is_created(self.pos) or self.pos == 0:
                self.pos = random.randint(1,10)
            if self.pos == 1:
                self.isGK = True
                self.x = 345
                self.y = -20
                self.vx = 0.1
                self.vy = 0.1
            elif 2 <= self.pos <= 5:
                self.x = 250
                self.y = (self.canvas_height*(self.pos*(-11/30))) +400
            elif 6 <= self.pos <= 8:
                self.x = 150
                self.y = (self.canvas_height*self.pos*(-1/3)) + 700
            else:
                self.x = 50
                self.y = (self.canvas_height*(self.pos * (2/5))) - 1200
        elif self.team == "Man city":
            self.color = (108, 171, 221)
            while player_database.pos_is_created(self.pos) or self.pos == 0:
                self.pos = random.randint(1,11)
                self.isGK = True
            if self.pos == 1:
                self.x = -345
                self.y = -20
                self.vx = 0.1
                self.vy = 0.1
            elif 2 <= self.pos <= 5:
                self.x = -250
                self.y = (self.canvas_height*(self.pos*(-11/30))) +400
            elif 6 <= self.pos <= 8:
                self.x = -150
                self.y = (self.canvas_height*self.pos*(-1/3)) + 700
            else:
                self.x = -50
                self.y = (self.canvas_height*(self.pos * (2/5))) - 1200
        else:
            self.size = 5
            self.x = 0
            self.y = 0
            self.vx = 0
            self.vy = 0
            self.color = (255, 255, 0)
            self.mass = 100*self.size**2
            self.count = 0
            self.id = 0

        self.location = [self.x, self.y]
            
    def draw(self):
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()
        turtle.color("black")  # Text color

    def is_in_goal(self, team):
        if team == "liverpool":
            if self.x < -360 and -60 <= self.y <= 60:
                return True
        elif team == "man city":
            if self.x < -360 and -60 <= self.y <= 60:
                return True
        return False

    def bounce_off_vertical_wall(self):
        self.vx = -self.vx
        self.count += 1

    def bounce_off_horizontal_wall(self):
        self.vy = -self.vy
        self.count += 1

    def bounce_off(self, that):
        dx  = that.x - self.x
        dy  = that.y - self.y
        dvx = that.vx - self.vx
        dvy = that.vy - self.vy
        dvdr = dx*dvx + dy*dvy; # dv dot dr
        dist = self.size + that.size   # distance between particle centers at collison

        # magnitude of normal force
        magnitude = 2 * self.mass * that.mass * dvdr / ((self.mass + that.mass) * dist)

        # normal force, and in x and y directions
        fx = magnitude * dx / dist
        fy = magnitude * dy / dist

        # update velocities according to normal force
        if self.team == "Ball":
            self.vx += fx / self.mass
            self.vy += fy / self.mass
            self.count += 1
        if that.team == "Ball":
            that.vx -= fx / that.mass
            that.vy -= fy / that.mass
            that.count += 1
        
        # update collision counts
        # self.count += 1
        # that.count += 1

    def distance(self, that):
        x1 = self.x
        y1 = self.y
        x2 = that.x
        y2 = that.y
        d = math.sqrt((y2-y1)**2 + (x2-x1)**2)
        return d

    def move(self, dt):
        self.x += self.vx*dt
        self.y += self.vy*dt

    def time_to_hit(self, that):
        if self is that:
            return math.inf
        dx  = that.x - self.x
        dy  = that.y - self.y
        dvx = that.vx - self.vx
        dvy = that.vy - self.vy
        dvdr = dx*dvx + dy*dvy
        if dvdr > 0:
            return math.inf
        dvdv = dvx*dvx + dvy*dvy
        if dvdv == 0:
            return math.inf
        drdr = dx*dx + dy*dy
        sigma = self.size + that.size
        d = (dvdr*dvdr) - dvdv * (drdr - sigma*sigma)
        # if drdr < sigma*sigma:
            # print("overlapping particles")
        if d < 0:
            return math.inf
        t = -(dvdr + math.sqrt(d)) / dvdv

        # should't happen, but seems to be needed for some extreme inputs
        # (floating-point precision when dvdv is close to 0, I think)
        if t <= 0:
            return math.inf

        return t

    def time_to_hit_vertical_wall(self):
        if self.vx > 0:
            return (self.canvas_width - self.x - self.size) / self.vx
        elif self.vx < 0:
            return (self.canvas_width + self.x - self.size) / (-self.vx)
        else:
            return math.inf

    def time_to_hit_horizontal_wall(self):
        if self.vy > 0:
            return (self.canvas_height - self.y - self.size) / self.vy
        elif self.vy < 0:
            return (self.canvas_height + self.y - self.size) / (-self.vy)
        else:
            return math.inf

    def time_to_hit_salah(self, object):
    # Y-axis collision
        if (self.vy > 0) and ((self.y + self.size) > (object.location[1] - object.height / 2)):
            return math.inf
        if (self.vy < 0) and ((self.y - self.size) < (object.location[1] + object.height / 2)):
            return math.inf

        dt_y = (math.sqrt((object.location[1] - self.y)**2) - self.size - object.height / 2) / abs(self.vy)
        paddle_left_edge = object.location[0] - object.width / 2
        paddle_right_edge = object.location[0] + object.width / 2
        if paddle_left_edge - self.size <= self.x + (self.vx * dt_y) <= paddle_right_edge + self.size:
            return dt_y

        # X-axis collision
        if (self.vx > 0) and ((self.x + self.size) > (object.location[0] - object.width / 2)):
            return math.inf
        if (self.vx < 0) and ((self.x - self.size) < (object.location[0] + object.width / 2)):
            return math.inf

        dt_x = (math.sqrt((object.location[0] - self.x)**2) - self.size - object.width / 2) / abs(self.vx)
        paddle_top_edge = object.location[1] - object.height / 2
        paddle_bottom_edge = object.location[1] + object.height / 2
        if paddle_top_edge - self.size <= self.y + (self.vy * dt_x) <= paddle_bottom_edge + self.size:
            return dt_x

        return math.inf



    def bounce_off_salah(self):
        self.vy = -self.vy
        self.vx = -self.vx
