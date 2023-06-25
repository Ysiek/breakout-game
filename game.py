class Game:
    def __init__(self, user_pad, ball, blocks):
        self.user_pad = user_pad
        self.ball = ball
        self.blocks = blocks
        self.new_x = 5
        self.new_y = -5

    def move_right(self):
        actual_position = self.user_pad.position()[0]
        if not actual_position >= 190:
            self.user_pad.setx(actual_position + 10)

    def move_left(self):
        actual_position = self.user_pad.position()[0]
        if not actual_position <= -200:
            self.user_pad.setx(actual_position - 10)

    def move(self):
        new_x = self.ball.xcor() + self.new_x
        new_y = self.ball.ycor() + self.new_y
        self.ball.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.new_y *= -1

    def bounce_x(self):
        self.new_x *= -1
