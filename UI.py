import turtle

class Ui:
    def __init__(self):
        self.ball = None
        self.user_pad = None
        self.blocks = []
        self.lifes_text = None
        self.score = None
        self.create_border()
        self.create_pad()
        self.create_blocks()
        self.create_score()
        self.create_lifes()
        self.create_ball()

    def create_ball(self):
        self.ball = turtle.Turtle('circle')
        self.ball.penup()
        self.ball.color('white')
        self.ball.st()

    def create_score(self):
        self.score = turtle.Turtle()
        self.score.color('grey')
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(x=-120, y=210)
        self.score.write('000', align='center', font=('Calibri', 50, 'italic'))

    def create_lifes(self):
        self.lifes_text = turtle.Turtle()
        self.lifes_text.color('grey')
        self.lifes_text.penup()
        self.lifes_text.hideturtle()
        self.lifes_text.goto(x=120, y=210)
        self.lifes_text.write('003', align='center', font=('Calibri', 50, 'italic'))

    def create_border(self):
        for num in range(0, 3):
            if num == 0:
                self.border(-235)
            if num == 1:
                self.border(228)
            if num == 2:
                border = turtle.Turtle('square')
                border.color('grey')
                border.penup()
                border.sety(330)
                border.turtlesize(stretch_len=23)
                border.st()

    def border(self, x):
        border = turtle.Turtle('square')
        border.color('grey')
        border.penup()
        border.setheading(90)
        border.setx(x)
        border.turtlesize(stretch_len=35)
        border.st()

    def create_pad(self):
        self.user_pad = turtle.Turtle('square')
        self.user_pad.color('lightblue')
        self.user_pad.penup()
        self.user_pad.sety(-300)
        self.user_pad.turtlesize(stretch_len=3)
        self.user_pad.st()

    def create_blocks(self):
        color = None
        for num in range(100, 191, 30):
            if num == 100:
                color = 'yellow'
            elif num == 130:
                color = 'green'
            elif num == 160:
                color = 'orange'
            elif num == 190:
                color = 'red'
            self.create_layer(y=num, color=color)


    def create_layer(self, y, color):
        for num in range(0, 450, 50):
            block = turtle.Turtle('square')
            block.color(color)
            block.penup()
            block.goto(x=-205+num, y=y)
            block.turtlesize(stretch_len=2)
            block.st()
            self.blocks.append(block)
