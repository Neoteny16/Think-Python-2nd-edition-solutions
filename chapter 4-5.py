import turtle, math
"""solution"""
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    # print(arc_length,'yg')
    n = int(arc_length/2) + 1
    # print(n)
    step_length = arc_length / n
    step_angle = angle / n
    # print(step_length,step_angle)
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        # raise Exception

def circle(t, r):
    arc(t, r, 360)



def draw_spiral(t, n, length=30, a=0.1, b=0.0002):
    """Draws an Archimedian spiral starting at the origin.
    Args:
      n: how many line segments to draw
      length: how long each segment is
      a: how loose the initial spiral starts out (larger is looser)
      b: how loosly coiled the spiral is (larger is looser)
    http://en.wikipedia.org/wiki/Spiral
    """
    theta = 0.0

    for i in range(n):
        t.fd(length)
        dtheta = 1 / (a + b * theta)
        t.fd(length)
        t.lt(90)
        t.fd(length)
        t.lt(90)
        arc(bob, length, 45)
        t.lt(dtheta)

        theta += dtheta


# create the world and bob
bob = turtle.Turtle()
draw_spiral(bob, n=1000)

turtle.mainloop()