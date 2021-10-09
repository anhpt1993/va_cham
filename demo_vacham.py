import turtle as tt
import time

screen = tt.Screen()
screen.tracer(0)
t = tt.Turtle()
t.hideturtle()

def draw_rectangle(pen, x, y, width, height):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    for i in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)


def draw_text(pen, x, y, text):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.write(text, font=("Arial", 30, "normal"))


# Xét theo trục Ox
# |(x1 + W1/2) - (x2 + W2/2)| ≤ |(W1 + W2)/2|
# Xét theo trục Oy
# |(y1 + H1/2) - (y2 + H2/2)| ≤ |(H1 + H2)/2|

def is_collision(rect1, rect2):
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2
    # sử dụng công thức trong bài viết
    return abs((x1 + w1/2) - (x2 + w2/2)) <= (w1 + w2)/2 and abs((y1 + h1/2) - (y2 + h2/2)) <= (h1 + h2)/2


def notify_collision(rect1, rect2):
    if is_collision(rect1, rect2):
        draw_text(t, 0, 200, "2 hình đã va chạm")
    else:
        draw_text(t, 0, 200, "2 hình đang di chuyển")

x1=-10
y1=-10
w1=100
h1=50

x2=-100
y2=-100
w2=100
h2=50

def misc():
    draw_rectangle(t, x1, y1, w1, h1)
    draw_rectangle(t, x2, y2, w2, h2)

    rect1 = (x1, y1, w1, h1)
    rect2 = (x2, y2, w2, h2)
    notify_collision(rect1, rect2)

    screen.update()


def move_up():
    global x1, y1, w1, h1, x2, y2, w2, h2
    t.clear()
    y2 += 5
    misc()

def move_down():
    global x1, y1, w1, h1, x2, y2, w2, h2
    t.clear()
    y2 -= 5
    misc()

def move_left():
    global x1, y1, w1, h1, x2, y2, w2, h2
    t.clear()
    x2 -= 5
    misc()

def move_right():
    global x1, y1, w1, h1, x2, y2, w2, h2
    t.clear()
    x2 += 5
    misc()

tt.onkeypress(move_up, "Up")
tt.onkeypress(move_down, "Down")
tt.onkeypress(move_left, "Left")
tt.onkeypress(move_right, "Right")
tt.listen()
tt.done()