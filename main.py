import heapq
import random
import time
import turtle

import Footballer_Database
import FootballerPlayer
import Gamedone
import Object
import Timer
import Event
from Score import Score


class main:
    def __init__(self):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.ball = Object.Object(team="Ball")
        self.object_list = [self.ball]
        self.t = 0.0
        self.pq = []
        self.HZ = 4
        self.score = Score(self.ball)
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        print(self.canvas_width, self.canvas_height)

        self.liverpool = Footballer_Database.Footballer_Database()
        self.mancity = Footballer_Database.Footballer_Database()
        self.mancity_list = []
        for i in range(10):
            liverpool_player = Object.Object("Liverpool", self.liverpool)
            self.liverpool.add_footballer(liverpool_player)
            liverpool_player.draw()
            self.object_list.append(liverpool_player)
            if liverpool_player.isGK:
                self.lfc_gk = liverpool_player

        for i in range(11):
            mancity_player = Object.Object("Man city", self.mancity)
            self.mancity.add_footballer(mancity_player)
            mancity_player.draw()
            self.object_list.append(mancity_player)
            if mancity_player.isGK:
                self.mancity_gk = mancity_player
        self.ball.draw()
        tom = turtle.Turtle()
        salah_data = Footballer_Database.Footballer_Database()
        self.my_salah = FootballerPlayer.FootballerPlayer(salah_data, tom)

        self.screen = turtle.Screen()

    # updates priority queue with all new events for a_ball
    def __predict_ball(self, a_ball):
        if a_ball is None:
            return

        # particle-particle collisions
        for i in range(len(self.object_list)):
            dt = a_ball.time_to_hit(self.object_list[i])
            # insert this event into pq
            heapq.heappush(self.pq, Event.Event_ball_to_player(
                self.t + dt, a_ball, self.object_list[i], None))

        # particle-wall collisions
        dtX = a_ball.time_to_hit_vertical_wall()
        dtY = a_ball.time_to_hit_horizontal_wall()
        heapq.heappush(self.pq, Event.Event_ball_to_player(
            self.t + dtX, a_ball, None, None))
        heapq.heappush(self.pq, Event.Event_ball_to_player(
            self.t + dtY, None, a_ball, None))

    def __draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2*self.canvas_width)
            turtle.left(90)
            turtle.forward(2*self.canvas_height)
            turtle.left(90)

    def __redraw(self):
        turtle.clear()
        self.my_salah.clear()
        self.__draw_border()
        self.my_salah.draw()
        for i in range(len(self.object_list)):
            self.object_list[i].draw()
        self.ball.draw()
        turtle.update()
        heapq.heappush(self.pq, Event.Event_ball_to_player(
            self.t + 1.0/self.HZ, None, None, None))

    # move_left and move_right handlers update paddle positions
    def move_left(self):
        if (self.my_salah.location[0] - self.my_salah.width/2 - self.my_salah.speed) >= -self.canvas_width:
            self.my_salah.set_location(
                [self.my_salah.location[0] - self.my_salah.speed, self.my_salah.location[1]])
            for player in self.object_list:  # make other player move along as salah is moving
                if player.team == "Liverpool" and\
                (self.my_salah.location[0] - self.my_salah.width/2 - 80)\
                >= -self.canvas_width and\
                (self.my_salah.location[0] + self.my_salah.width/2 + 220)\
                <= self.canvas_width\
                        and player.pos != 1:
                    player.x -= player.vx

    # move_left and move_right handlers update paddle positions
    def move_right(self):
        if (self.my_salah.location[0] + self.my_salah.width/2 + self.my_salah.speed)\
            <= self.canvas_width:
            self.my_salah.set_location(
            [self.my_salah.location[0] + self.my_salah.speed,\
            self.my_salah.location[1]])
            for player in self.object_list:  # make other player move along as salah is moving
                if player.team == "Liverpool" and\
                (self.my_salah.location[0] + self.my_salah.width/2 + 205)\
                <= self.canvas_width and\
                (self.my_salah.location[0] - self.my_salah.width/2 - 105)\
                >= -self.canvas_width\
                and player.pos != 1:
                    player.x += player.vx

    def move_up(self):
        if (self.my_salah.location[1] + self.my_salah.height/2 + 5)\
            <= self.canvas_height:
            self.my_salah.set_location(
                [self.my_salah.location[0], self.my_salah.location[1] + 5])
            for player in self.object_list:  # make other player move along as salah is moving
                if player.team == "Liverpool" and\
                    (self.my_salah.location[1] + self.my_salah.height/2 + 40)\
                    <= self.canvas_height and\
                    (self.my_salah.location[1] - self.my_salah.height/2 - 300)\
                    >= -self.canvas_height\
                    and player.pos != 1:
                    player.y += player.vy

    # move_left and move_right handlers update paddle positions
    def move_down(self):
        if (self.my_salah.location[1] - self.my_salah.height/2 - 5)\
            >= -self.canvas_height:
            self.my_salah.set_location(
                [self.my_salah.location[0], self.my_salah.location[1] - 5])
            for player in self.object_list:  # make other player move along as salah is moving
                if player.team == "Liverpool" and\
                    (self.my_salah.location[1] - self.my_salah.height/2 - 300)\
                    >= -self.canvas_height and\
                    (self.my_salah.location[1] + self.my_salah.height/2 + 40)\
                    <= self.canvas_height\
                        and player.pos != 1:
                    player.y -= player.vy

    def _is_near(self, player):
        if abs(self.ball.x - player.x) < 200 and\
                abs(self.ball.y - player.y) < 80:
            return True
        return False

    def mancity_pressing(self, player):
        if random.randint(1, 2) == 1:
            if player.x > self.ball.x + self.ball.size * 2 and\
                    self._is_near(player):
                player.x -= player.vx
            elif player.x < self.ball.x - self.ball.size * 2 and\
                    self._is_near(player):
                player.x += player.vx
            if player.y > self.ball.y + self.ball.size * 2 and\
                    self._is_near(player):
                player.y -= player.vy
            elif player.y < self.ball.y - self.ball.size * 2 and\
                    self._is_near(player):
                player.y += player.vy

    def man_city_move(self):
        self.mancity_list = self.mancity.footballer_database
        for player in self.mancity_list:
            if random.randint(1, 10) == 1 and player.pos != 1:
                self.mancity_pressing(player)
            else:
                player.vx = random.randint(-3, 3)
                player.vy = random.randint(-3, 3)

    def ball_speed_control(self):
        if self.ball.vx > 40:
            self.ball.vx = 40
        elif self.ball.vx < -40:
            self.ball.vx = -40
        elif self.ball.vy > 40:
            self.ball.vy = 40
        elif self.ball.vy < -40:
            self.ball.vy = -40

    def reset_pos(self):  # occur when a goal is scored
        for player in self.object_list:
            if player.team == "Liverpool":
                if 2 <= player.pos <= 5:
                    player.x = 250
                    player.y = (self.canvas_height*(player.pos*(-11/30))) + 400
                elif 6 <= player.pos <= 8:
                    player.x = 150
                    player.y = (self.canvas_height*player.pos*(-1/3)) + 700
                elif 9 <= player.pos <= 10:
                    player.x = 50
                    player.y = (self.canvas_height*(player.pos * (2/5))) - 1200
            elif player.team == "Mancity":
                if 2 <= player.pos <= 5:
                    player.x = -250
                    player.y = (self.canvas_height*(player.pos*(-11/30))) + 400
                elif 6 <= player.pos <= 8:
                    player.x = -150
                    player.y = (self.canvas_height*player.pos*(-1/3)) + 700
                else:
                    player.x = -50
                player.y = (self.canvas_height*(player.pos * (2/5))) - 1200
        self.ball.x = 0
        self.ball.y = 0
        self.ball.vx = 0
        self.ball.vy = -6
        self.my_salah.set_location([50, 150])
        # self.pq.clear()

    def is_collision_salah(self, ball, salah):
        ball_left = ball.x - ball.size / 2
        ball_right = ball.x + ball.size / 2
        ball_top = ball.y + ball.size / 2
        ball_bottom = ball.y - ball.size / 2

        salah_left = salah.location[0] - salah.width / 2
        salah_right = salah.location[0] + salah.width / 2
        salah_top = salah.location[1] + salah.height / 2
        salah_bottom = salah.location[1] - salah.height / 2

        return not (
            ball_right < salah_left or
            ball_left > salah_right or
            ball_top < salah_bottom or
            ball_bottom > salah_top
        )

    def run(self):
        # initialize pq with collision events and redraw event
        for i in range(len(self.object_list)):
            self.__predict_ball(self.object_list[i])
        heapq.heappush(
            self.pq, Event.Event_ball_to_player(0, None, None, None))

        # listen to keyboard events and activate move_left and move_right handlers accordingly
        self.screen.listen()
        self.screen.onkeypress(self.move_left, "a")
        self.screen.onkeypress(self.move_right, "d")
        self.screen.onkeypress(self.move_up, "w")
        self.screen.onkeypress(self.move_down, "s")
        start_time = time.time()
        timer = Timer.Timer()  # initiate timer

        # game main loop
        while (True):
            e = heapq.heappop(self.pq)
            self.pq.pop()
            if not e.is_valid():
                continue

            is_scored = False
            is_scored = self.score.do_score()
            if is_scored:
                self.reset_pos()

            self.score.write_score()

            object_a = e.a
            object_b = e.b
            salah_a = e.salah

            # update positions, and then simulation clock
            self.ball.move(e.time - self.t)
            for mancity in self.mancity_list:
                mancity.move(e.time - self.t)
            self.t = e.time
            self.score.draw_goals()

            self.man_city_move()
            self.ball_speed_control()

            if (object_a is not None) and (object_b is not None) and (salah_a is None):
                object_b.bounce_off(object_a)
            elif (self.ball.x >= 365 or self.ball.x <= -365) and (object_a is not None):
                object_a.bounce_off_vertical_wall()
                if self.ball.x >= 365:
                    self.ball.x = 355
                elif self.ball.x < -365:
                    self.ball.x = -355
            elif (self.ball.y >= 280 or self.ball.y <= -280) and (object_b is not None):
                object_b.bounce_off_horizontal_wall()
                if self.ball.y >= 280:
                    self.ball.y = 270
                elif self.ball.y <= -280:
                    self.ball.y = -270
            elif (object_a is None) and (object_b is None) and (salah_a is None):
                self.__redraw()
            elif self.is_collision_salah(self.ball, self.my_salah):
                self.ball.vx = -20

            self.__predict_ball(object_a)
            self.__predict_ball(object_b)

            # regularly update the prediction for the paddle as its position may always be changing due to keyboard events

            if timer.is_over(start_time, 100):
                print("done")
                gameover = Gamedone.Gamedone(
                    self.score.lfc_score, self.score.mancity_score)
                gameover.do_gameover()
                turtle.done()

        turtle.done()


# main part code
my_simulator = main()
my_simulator.run()
