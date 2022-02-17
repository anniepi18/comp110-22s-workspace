"""Creates a beautiful landscape."""

__author__ = "730502223"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    bob: Turtle = Turtle()
    bob.speed(50)
    draw_sun(bob, -250, 150, 60)
    draw_cloud(bob, 30, -100, 150)
    draw_cloud(bob, 35, 150, 140)
    draw_tree(bob, 0, 20)
    
    done()


def draw_tree(name: Turtle, x: float, y: float) -> None:
    """Draws a tree given the top left of trunk located at x,y and calls the leaves function."""
    name.penup()
    name.goto(x, y)
    name.setheading(0.0)
    name.pendown()
    name.color(139, 71, 38)
    name.begin_fill()
    name.forward(60)
    name.right(90)
    name.forward(250)
    name.right(90)
    name.forward(60)
    name.right(90)
    name.forward(250)
    name.end_fill()
    tree_leaves(name, 50)
    name.forward(50)
    i: int = 0
    while i < 4:
        tree_leaves(name, 50)
        name.right(90)
        i += 1


def tree_leaves(name: Turtle, size: float) -> None:
    """Creates leaves to put ontop of trunk."""
    name.penup()
    name.pendown()
    name.pencolor(48, 128, 20)
    name.fillcolor(48, 128, 20)
    name.begin_fill()
    name.circle(size)
    name.end_fill()

    
def draw_sun(name: Turtle, x: float, y: float, rad: float) -> None:
    """Draws a yellow sun with the given radius and the base located at x, y. I am attempting the try something fun part by using circle(), which wasn't discussed in the tutorial."""
    name.penup()
    name.goto(x, y)
    name.setheading(0.0)
    name.pendown()
    name.pencolor("black")
    name.fillcolor("yellow")
    name.begin_fill()
    name.circle(rad)
    name.end_fill()


def draw_cloud(name: Turtle, size: float, x: float, y: float) -> None:
    """Draws a grey cloud and fills it in."""
    name.penup()
    name.goto(x, y)
    name.pendown()
    filled_circle(name, size)
    name.forward(size)
    i: int = 0
    while i < 4:
        filled_circle(name, size)
        name.right(90)
        i += 1
    

def filled_circle(name: Turtle, size: float) -> None:
    """Creates a filled white circle which will be used to create clouds."""
    name.penup()
    name.pendown()
    name.pencolor(224, 238, 238)
    name.fillcolor(224, 238, 238)
    name.begin_fill()
    name.circle(size)
    name.end_fill()


if __name__ == "__main__":
    main()