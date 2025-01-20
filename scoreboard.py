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
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score:{self.count}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def writing(self):
        self.count+=1
        self.clear()
        self.update_scoreboard()