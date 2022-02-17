from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
bob: Turtle = Turtle()
colormode(255)
side_length: float = 300


leo.penup()
leo.goto(-100, -100)
leo.pendown()
leo.color(99, 204, 250)
leo.pencolor("pink")
bob.color("black")
bob.penup()
bob.goto(-100, -100)
bob.pendown()
bob.speed(40)

leo.begin_fill()
i: int = 0 
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()

bob.begin_fill()
i: int = 0 
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i += 1
    side_length = side_length * 0.97
bob.end_fill()
done() 