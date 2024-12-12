import turtle

class Score:
    def __init__(self, ball_):
        self.lfc_score = 0
        self.mancity_score = 0
        self.ball_ = ball_  # Use the ball object passed from main
        self.score_writer = turtle.Turtle()

    def write_score(self):
        """Writes the current score on the screen."""
        self.score_writer.clear()
        self.score_writer.penup()
        self.score_writer.goto(0, 200)
        self.score_writer.write(
            f"Man City {self.mancity_score} : {self.lfc_score} Liverpool",
            align="center",
            font=("Arial", 16, "bold"),
        )

    def draw_goals(self):
        self._draw_rectangle(-365, 60, -400, -60)
        self._draw_rectangle(365, 60, 400, -60)

    def _draw_rectangle(self, x1, y1, x2, y2):
        t = turtle.Turtle()
        t.hideturtle
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y1)
        t.goto(x2, y2)
        t.goto(x1, y2)
        t.goto(x1, y1)

    def do_score(self):
        if self.ball_.is_in_goal("liverpool"):
            self.lfc_score += 1
            return True
        elif self.ball_.is_in_goal("man city"):
            self.mancity_score += 1
            return True
        return False