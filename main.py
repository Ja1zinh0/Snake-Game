import turtle
from turtle import Screen
import time
import keyboard
import threading
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def start_game():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    def process_key_input(event):
        key = event.name
        if key == 'up':
            snake.move_up()
        elif key == 'down':
            snake.move_down()
        elif key == 'left':
            snake.move_left()
        elif key == 'right':
            snake.move_right()
        elif key == 'w':
            snake.move_up()
        elif key == 's':
            snake.move_down()
        elif key == 'a':
            snake.move_left()
        elif key == 'd':
            snake.move_right()

    def keyboard_listener():
        keyboard.on_press(process_key_input)

    # Iniciar a thread para receber inputs de teclado
    thread = threading.Thread(target=keyboard_listener)
    thread.start()

    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.05)
        snake.move()

        if snake.head.distance(food) < 15:
            food.new_food()
            scoreboard.increase_score()
            snake.extend()

        if (
            snake.head.xcor() > 280
            or snake.head.xcor() < -280
            or snake.head.ycor() > 280
            or snake.head.ycor() < -280
        ):
            game_on = False
            scoreboard.game_over()

        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 15:
                game_on = False
                scoreboard.game_over()

    restart_game()


def restart_game():
    turtle.Screen().clear()
    start_game()


start_game()
