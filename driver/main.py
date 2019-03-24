import turtle
import sys


def main(board, CELL_SIZE):
    scr = turtle.Screen()
    xsize, ysize = scr.screensize()
    turtle.setworldcoordinates(0, 0, xsize, ysize)

    turtle.hideturtle()
    turtle.speed('fastest')
    turtle.tracer(0, 0)
    turtle.penup()

    board.animate_life()

    turtle.onkey(sys.exit, 'q')

    turtle.listen()
    turtle.mainloop()