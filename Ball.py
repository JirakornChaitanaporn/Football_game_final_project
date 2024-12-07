# import turtle
# import math

# class Ball:
#     def __init__(self, x, y, vx, vy, id):
#         self.size = 5
#         self.x = x
#         self.y = y
#         self.vx = vx
#         self.vy = vy
#         self.color = (255, 255, 0)
#         self.mass = 100*self.size**2
#         self.count = 0
#         self.id = id
#         self.canvas_width = turtle.screensize()[0]
#         self.canvas_height = turtle.screensize()[1]
        

#     def draw(self):
#         # draw a circle of radius equals to size centered at (x, y) and paint it with color
#         turtle.penup()
#         turtle.color(self.color)
#         turtle.fillcolor(self.color)
#         turtle.goto(self.x, self.y-self.size)
#         turtle.pendown()
#         turtle.begin_fill()
#         turtle.circle(self.size)
#         turtle.end_fill()

#     def is_in_goal(self, team):
#         if team == "liverpool":
#             if self.x < -360 and -60 <= self.y <= 60:
#                 return True
#         elif team == "man city":
#             if self.x < -360 and -60 <= self.y <= 60:
#                 return True
#         return False

#     def bounce_off_vertical_wall(self):
#         self.vx = -self.vx
#         self.count += 1

#     def bounce_off_horizontal_wall(self):
#         self.vy = -self.vy
#         self.count += 1

#     def bounce_off(self, that):
#         dx  = that.x - self.x
#         dy  = that.y - self.y
#         dvx = that.vx - self.vx
#         dvy = that.vy - self.vy
#         dvdr = dx*dvx + dy*dvy; # dv dot dr
#         dist = self.size + that.size   # distance between particle centers at collison

#         # magnitude of normal force
#         magnitude = 2 * self.mass * that.mass * dvdr / ((self.mass + that.mass) * dist)

#         # normal force, and in x and y directions
#         fx = magnitude * dx / dist
#         fy = magnitude * dy / dist

#         # update velocities according to normal force
#         self.vx += fx / self.mass
#         self.vy += fy / self.mass
#         that.vx -= fx / that.mass
#         that.vy -= fy / that.mass
        
#         # update collision counts
#         self.count += 1
#         that.count += 1

#     def distance(self, that):
#         x1 = self.x
#         y1 = self.y
#         x2 = that.x
#         y2 = that.y
#         d = math.sqrt((y2-y1)**2 + (x2-x1)**2)
#         return d

#     def move(self, dt):
#         self.x += self.vx*dt
#         self.y += self.vy*dt

#     def time_to_hit(self, that):
#         if self is that:
#             return math.inf
#         dx  = that.x - self.x
#         dy  = that.y - self.y
#         dvx = that.vx - self.vx
#         dvy = that.vy - self.vy
#         dvdr = dx*dvx + dy*dvy
#         if dvdr > 0:
#             return math.inf
#         dvdv = dvx*dvx + dvy*dvy
#         if dvdv == 0:
#             return math.inf
#         drdr = dx*dx + dy*dy
#         sigma = self.size + that.size
#         d = (dvdr*dvdr) - dvdv * (drdr - sigma*sigma)
#         # if drdr < sigma*sigma:
#             # print("overlapping particles")
#         if d < 0:
#             return math.inf
#         t = -(dvdr + math.sqrt(d)) / dvdv

#         # should't happen, but seems to be needed for some extreme inputs
#         # (floating-point precision when dvdv is close to 0, I think)
#         if t <= 0:
#             return math.inf

#         return t

#     def time_to_hit_vertical_wall(self):
#         if self.vx > 0:
#             return (self.canvas_width - self.x - self.size) / self.vx
#         elif self.vx < 0:
#             return (self.canvas_width + self.x - self.size) / (-self.vx)
#         else:
#             return math.inf

#     def time_to_hit_horizontal_wall(self):
#         if self.vy > 0:
#             return (self.canvas_height - self.y - self.size) / self.vy
#         elif self.vy < 0:
#             return (self.canvas_height + self.y - self.size) / (-self.vy)
#         else:
#             return math.inf

#     def time_to_hit_player(self, player):
#         if (self.vy > 0) and ((self.y + self.size) > (player.location[1] - player.height/2)):
#             return math.inf
#         if (self.vy < 0) and ((self.y - self.size) < (player.location[1] + player.height/2)):
#             return math.inf

#         dt = (math.sqrt((player.location[1] - self.y)**2) - self.size - player.height/2) / abs(self.vy)
#         paddle_left_edge = player.location[0] - player.width/2
#         paddle_right_edge = player.location[0] + player.width/2
#         if paddle_left_edge - self.size <= self.x + (self.vx*dt) <= paddle_right_edge + self.size:
#             return dt
#         else:
#             return math.inf

#     def bounce_off_salah(self):
#         self.vy = -self.vy
#         self.vx = -self.vx