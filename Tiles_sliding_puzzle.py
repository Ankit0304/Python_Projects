import turtle
from random import *
from freegames import floor,vector

tiles={}
neighbors=[
    vector(100,0),
    vector(-100,0),
    vector(0,100),
    vector(0,-100),
]

def load():
    "Load tiles and scramble."
    count=1
    for y in range(-200,200,100):
        for x in range(-200,200,100):
            mark=vector(x,y)
            tiles[mark]=count
            count+=1
    tiles[mark]=None

    for count in range(1000):
        neighbor=choice(neighbors)
        spot=mark+neighbor

        if spot in tiles:
            number=tiles[spot]
            tiles[spot]=None
            tiles[mark]=number
            mark=spot

def move_tile(spot, tiles, mark):
    if spot in tiles:
        number = tiles[spot]
        tiles[spot] = None
        tiles[mark] = number
        mark = spot
    return mark

def square(mark, number):
    "Draw white square with black outline and number."
    turtle.up()
    turtle.goto(mark[0], mark[1])
    turtle.down()

    turtle.color('black', 'white')
    turtle.begin_fill()
    
    for count in range(4):
        turtle.forward(99)
        turtle.left(90)
    turtle.end_fill()

    if number is not None:
        turtle.up()
        turtle.goto(mark[0] + 30, mark[1] + 20)
        turtle.color('black')
        turtle.write(number, font=('Arial', 36, 'normal'))

def tap(x,y):
    "Swap tile and empty square."
    x=floor(x,100)
    y=floor(y,100)
    mark=vector(x,y)

    for neighbor in neighbors:
        spot=mark+neighbor

        if spot in tiles and tiles[spot] is None:
            tiles[spot]=tiles[mark]
            square(spot,tiles[spot])
            tiles[mark]=None
            square(mark,None)
            
def draw():
    "Draw all tiles."
    for mark in tiles:
        square(mark,tiles[mark])
    turtle.update()

# Initialize turtle
turtle.speed(0)
turtle.hideturtle()

turtle.setup(420,420,370,0)
# turtle.hideturtle()
turtle.tracer(False)
load()
draw()
turtle.onscreenclick(tap)
turtle.done()
