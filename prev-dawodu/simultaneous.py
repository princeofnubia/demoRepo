import turtle
class Simultaneous_equation:
    # a typical simultaneous equation
    # 2x + 3y = 4
    # 4x + 5y = -1
    # ax + by = c  ---- m = -a/b  c= c/b
    # dx + ey = f  ---- m = -d/e  c = f/e
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self._x_axis_neg = -50
        self._x_axis_pos = 50
        self.m1 = -a/b
        self.c1 = c/b
        self.m2 = -d/e
        self.c2 = f/e
        
        self.solve()

    def solveX(self):
        self.x = (self.f * self.b - self.e * self.c)/(self.b * self.d - self.e * self.a)
        return self.x

    def solveY(self):
        self.y = (self.c * self.d - self.a * self.f)/(self.b * self.d - self.e * self.a)
        return self.y

    def solve(self):
        self.solveX()
        self.solveY()

    def print_solution(self):
        print('X is {0}, Y is {1}'.format(self.x, self.y))

    def draw_coordinates(self):
        # y axis first -negative 
        self.pen.penup()
        self.pen.goto(0, 100)
        self.pen.pendown()
        self.pen.goto(0, -100)
        # x axis
        self.pen.penup()
        self.pen.goto(-100, 0)
        self.pen.pendown()
        self.pen.goto(100, 0)
        self.pen.penup()
        
    def draw_equation(self, m, c):
        #y = mx + c
        self.pen.penup()
        y100 =  m * (-100) + c
        self.pen.goto(-100,y100)
        self.pen.pendown()
        for x in range (-99, 100):
            y = m * x + c
            self.pen.goto(x, y)
        self.pen.write('y = {0}x + {1}'.format(m, c))
        self.pen.penup()

    def draw_solution_graph(self):
        self.pen = turtle.Pen()
        self.draw_coordinates()
        # draw first equation graph
        self.draw_equation(self.m1, self.c1)
        # draw second equation graph
        self.draw_equation(self.m2, self.c2)
