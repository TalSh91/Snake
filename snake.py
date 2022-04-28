from turtle import Turtle,Screen
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake = []
        self.crate_snake()
        self.head = self.snake[0]



    def crate_snake(self):
        for _ in range(1, 4):
            self.add_snake()

    def add_snake(self):
        x = 0
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(x, 0)
        x -= 20
        self.snake.append(square)

    def extend(self):
        square = Turtle("square")
        square.color("white")
        square.penup()
        self.snake.append(square)

    def move(self):
        for snake_num in range(len(self.snake)-1, 0, -1):
            snake_pos = self.snake[snake_num-1].position()
            self.snake[snake_num].goto(snake_pos)
        self.head.forward(20)

    def change_dir(self):
        screen = Screen()
        screen.listen()
        screen.onkey(self.snake[0].right, "w")

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)






