from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
x_move = 0
y_move = 90
angle = 270
while (1):
    angle = 270
    clear_canvas_now()
    grass.draw_now(400,30)
    while (x_move < 780):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x_move, y_move)
        x_move = x_move + 2
        delay(0.01)
    while (y_move < 590):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x_move, y_move)
        y_move = y_move + 2
        delay(0.01)
    while (x_move > 0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x_move, y_move)
        x_move = x_move - 2
        delay(0.01)
    while (y_move > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x_move, y_move)
        y_move = y_move - 2
        delay(0.01)
    while (x_move < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x_move, y_move)
        x_move = x_move + 2
        delay(0.01)
    while (angle < 360):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x_move, y_move)
        x_move = 400 + 300 * math.cos(angle / 360 * 2 * math.pi) 
        y_move = 300 + 300 * math.sin(angle / 360 * 2 * math.pi)
        angle = angle + 1
        delay(0.01)
    angle = 0
    while (angle < 270):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x_move, y_move)
        x_move = 400 + 300 * math.cos(angle / 360 * 2 * math.pi) 
        y_move = 300 + 300 * math.sin(angle / 360 * 2 * math.pi)
        angle = angle + 1
        delay(0.01)
    x_move = 400
    y_move = 90
close_canvas()
