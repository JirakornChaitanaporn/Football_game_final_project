class Event_ball_to_player:
    def __init__(self, time, player_a, ball_b, salah):
        self.time = time
        self.a = player_a
        self.b = ball_b
        self.salah = salah

        if player_a is not None:
            self.count_a = player_a.count
        else:
            self.count_a = -1
        if ball_b is not None:
            self.count_b = ball_b.count
        else:
            self.count_b = -1

    def __lt__(self, that):
        return self.time < that.time

    def is_valid(self):
        if (self.a is not None) and (self.a.count != self.count_a):
            return False
        if (self.b is not None) and (self.b.count != self.count_b):
            return False
        return True

    def __str__(self):
        return f"{self.time}     {self.a}     {self.b}    {self.salah}"