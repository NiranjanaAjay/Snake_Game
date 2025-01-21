from mimetypes import inited
from turtle import Turtle
ALIGNMENT="center"
FONT=('Courier', 12, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.count=0
        self.high_score=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score:{self.count} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.count>self.high_score:
            self.high_score=self.count
        self.count=0
        self.update_scoreboard()

    def writing(self):
        self.count+=1
        self.update_scoreboard()