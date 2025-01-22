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
        with open("data.txt") as file:
            self.high_score=int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score:{self.count} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.count>self.high_score:
            self.high_score=self.count
            with open("data.txt","w") as file:
                file.write(str(self.count))
        self.count=0
        self.update_scoreboard()

    def writing(self):
        self.count+=1
        self.update_scoreboard()