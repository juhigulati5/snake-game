from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.scores = 0
        with open("data.txt") as file:
            self.high_score = file.read()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.scores} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def keep_score(self):
        self.scores += 1
        self.clear()
        self.update_scoreboard()

    def keep_high_score(self):
        with open("data.txt",mode="w") as file:
            file.write(str(self.high_score))

    def reset(self):
        if self.scores > int(self.high_score):
            self.high_score = self.scores
            self.keep_high_score()
        self.scores = 0
        self.update_scoreboard()

