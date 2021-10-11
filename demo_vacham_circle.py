import turtle as t
import math

screen = t.Screen()
screen.tracer(0)
pen = t.Turtle()
pen.hideturtle()

def draw_circle(pen, x, y, radius):
    pen.penup()
    pen.goto(x, y-radius)
    pen.pendown()
    pen.pensize(3)
    pen.pencolor("orange")
    pen.circle(radius)


def draw_text(pen, x, y, text):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.pencolor("red")
    pen.write(text, font=("Comic Sans MS", 30, "normal"), align="center")

def is_collision(rect1, rect2):
    x1, y1, r1 = rect1
    x2, y2, r2 = rect2
    # sử dụng công thức trong bài viết
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2) <= r1 + r2

def notify_impact(rect1, rect2):
    if is_collision(rect1, rect2):
        draw_text(pen, 0, 300, "2 hình đã va chạm")
    else:
        draw_text(pen, 0, 300, "2 hình đang di chuyển")

def update_circle():
    draw_circle(pen, x1, y1, r1)
    draw_circle(pen, x2, y2, r2)

    rect1 = (x1, y1, r1)
    rect2 = (x2, y2, r2)
    notify_impact(rect1, rect2)

    screen.update()


def move_up():
    global x1, y1, r1, x2, y2, r2
    pen.clear()
    y2 += 5
    update_circle()

def move_down():
    global x1, y1, r1, x2, y2, r2
    pen.clear()
    y2 -= 5
    update_circle()

def move_left():
    global x1, y1, r1, x2, y2, r2
    pen.clear()
    x2 -= 5
    update_circle()

def move_right():
    global x1, y1, r1, x2, y2, r2
    pen.clear()
    x2 += 5
    update_circle()

x1 = -10
y1 = -10
r1 = 50

x2 = -100
y2 = -100
r2 = 75

draw_circle(pen, x1, y1, r1)
draw_circle(pen, x2, y2, r2)

update_circle()
t.onkeypress(move_up, "Up")
t.onkeypress(move_down, "Down")
t.onkeypress(move_left, "Left")
t.onkeypress(move_right, "Right")
t.listen()
t.done()