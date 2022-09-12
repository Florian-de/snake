from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.highscore = 0
        with open("high_scores.txt") as file:
            file_read = file.read()
            self.highscore = int(file_read)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore} ", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_scores.txt", mode="w") as file:
                file_write = str(self.highscore)
                file.write(file_write)
        self.score = 0
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
