import turtle
from UI import Ui
from game import Game
import time

screen = turtle.Screen()
screen.title('Breakout game')
screen.setup(height=700, width=500)
screen.bgcolor('black')

screen.tracer(0)
ui_manager = Ui()
game_manager = Game(ui_manager.user_pad, ui_manager.ball, ui_manager.blocks)
# pad movement
screen.listen()
screen.onkey(game_manager.move_right, 'Right')
screen.onkey(game_manager.move_left, 'Left')

score = 0
lifes = 3
ball_speed = 0.1
game_is_on = True
while game_is_on:
    if score == 90:
        game_is_on = False
        print("You win")
        ui_manager.score.clear()
        ui_manager.score.write(f'{score * lifes}', align='center', font=('Calibri', 50, 'italic'))
    if lifes == 0:
        game_is_on = False
    time.sleep(ball_speed)
    screen.update()
    game_manager.move()
    # COLLISION WITH WALLS
    if game_manager.ball.xcor() >= 210 or game_manager.ball.xcor() <= -215:
        game_manager.bounce_x()

    if game_manager.ball.ycor() >= 315:
        game_manager.bounce_y()

    # COLLISION WITH PAD
    if game_manager.ball.distance(game_manager.user_pad) < 30 and game_manager.ball.ycor() <= -280:
        game_manager.bounce_y()

    for block in ui_manager.blocks:
        if game_manager.ball.distance(block) < 40:
            color = block.color()[0]
            if color == 'yellow':
                score += 1
            elif color == 'green':
                score += 2
            elif color == 'orange':
                score += 3
            elif color == 'red':
                score += 4
            ui_manager.score.clear()
            if score >= 10:
                ui_manager.score.write(f'0{score}', align='center', font=('Calibri', 50, 'italic'))
            else:
                ui_manager.score.write(f'00{score}', align='center', font=('Calibri', 50, 'italic'))
            block.goto(x=1000, y=1000)
            game_manager.bounce_y()
            ball_speed *= 0.93

    if game_manager.ball.ycor() <= -300:
        lifes -= 1
        ui_manager.lifes_text.clear()
        ui_manager.lifes_text.write(f'00{lifes}', align='center', font=('Calibri', 50, 'italic'))
        ui_manager.ball.goto(x=0, y=0)
        ball_speed = 0.1

screen.exitonclick()
