from vpython import *

ball = sphere(pos=vector(0, .1, 0), radius=0.05, color=color.yellow, make_trail=True)
print(ball.pos)

ground = box(pos=vector(0,0,0), size=vector(2.5, 0.02, 0.05))

g1 = graph(xtitle="t [s]", ytitle="y [m]")
f1 = gcurve(color=color.blue)

g = vector(0, -9.8, 0)
ball.m = 0.05
v0 = 3.5 #starts with velocity of 3.5m/s
theta = 73 * pi / 180
ball.v = v0 * vector(cos(theta), sin(theta), 0)
vscale = .1
varrow = arrow(pos=ball.pos, axis=vscale*ball.v, color=color.cyan)

t = 0
dt = 0.01

while ball.pos.y >= ground.pos.y + ball.radius + ground.size.y:
    rate(100)
    F = ball.m * g
    a = F / ball.m
    ball.v = ball.v + a * dt
    ball.pos = ball.pos + ball.v * dt
    varrow.pos = ball.pos
    varrow.axis = vscale * ball.v
    t = t + dt
    f1.plot(t, ball.pos.y)