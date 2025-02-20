from turtle import *
from typing import Literal
import random
list_action = ['forward', 'right']
color_bg = ['blue', 'black', 'green', 'red', 'yellow', 'white', 'purple', 'orange', 'cyan', 'magenta', 
            'pink', 'brown', 'gray', 'turquoise', 'silver', 'gold', 'lavender', 'coral', 'maroon', 
            'teal', 'navy', 'burgundy']

window = Screen()
title = window.title = 'Grafic'
shape('turtle')

def cuir(radius: int|float = 0.00):
    circle(radius)


def random_color():
    return color_bg[random.randint(0, 21)]

def square(radius_forward: int|float|list = 0.00, radius_right: int|float = 0.00, count: int = 4, bg_color: Literal['blue', 'black']|random_color = 'black') -> None:
    """Квадрат"""
    fillcolor(bg_color)
    begin_fill()
    if isinstance(radius_forward, list):
        for event in radius_forward:
            if isinstance(event, int) or isinstance(event, float):
               forward(event)
               right(radius_right)
            else:
                raise ValueError('Invalid Format type')
    else:
        for event in range(count):
               forward(radius_forward)
               right(radius_right) 
    end_fill()

def padding(action: Literal['forward', 'right'], gradis: int|float = 0) -> None:
    penup()
    for event in list_action:
        if event == action:
            if action == 'forward':
                forward(gradis)
            elif action == 'right':
                right(gradis)
            else:
                break
    pendown()
    

def window_create(at: int = 10) -> None:
   square(100, 90, bg_color=random_color())
   padding('forward', 110)
   square(100, 90, bg_color=random_color())
   padding('right', -90)
   padding('forward', at)
   square(100, 90, bg_color=random_color())
   padding('right', -90)
   padding('forward', at)
   square(100, 90, bg_color=random_color())

window_create()
window.exitonclick()