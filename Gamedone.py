import turtle

class Gamedone:
    def __init__(self, lfc_score, mancity_score):
        self.lfc_score = lfc_score
        self.mancity_score = mancity_score

    def do_gameover(self):
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(0, 0)
        if self.lfc_score > self.mancity_score:
            writer.write(f"YOU WIN", align="center", font=("Arial", 24, "normal"))
        elif self.lfc_score < self.mancity_score:
            writer.write(f"YOU LOST", align="center", font=("Arial", 24, "normal"))
        else:
            writer.write(f"DRAW!", align="center", font=("Arial", 24, "normal"))