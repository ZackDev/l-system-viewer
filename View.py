from abc import ABC, abstractmethod
import turtle


class AbstractView(ABC):
    @abstractmethod
    def update_view(self, name, depth, str):
        pass


class LSystemView(AbstractView):
    def __init__(self, controller):
        self.controller = controller
        self.window = turtle.Screen()
        # self.window._root.state('normal')
        self.window.setup(width=1.0, height=0.9)
        self.window.screensize(10000, 10000)
        self.window.colormode(255)
        self.window.bgcolor(51, 51, 51)
        self.window.tracer(1, 0)
        self.color_palette = [(102, 255, 155), (0, 204, 255), (0, 153, 255), (0, 70, 255)]
        self.pen = turtle.Turtle()
        self.controller.on_view_init_complete(self)
        self.controller.get_data()
        self.window.mainloop()

    def onmouse(self, btn, add):
        self.controller.get_data()

    def update_view(self, name, depth, str, starting_angle, angle):
        self.window.onscreenclick(None)
        self.pen.reset()
        self.name = name
        self.depth = depth
        self.str = str
        self.angle = angle

        self.window.title(f'Name: {self.name} - Depth: {self.depth}')

        self.pen.hideturtle()
        self.pen.speed('fastest')
        self.pen.pensize(2)
        self.pen.setheading(starting_angle)

        # draw function:
        # 'F' move pen forward and draw
        # 'f' move pen forward, don't draw,
        # '+' turn pen left by angle
        # '-' turn pen right by angle
        # '[' store current pen state
        # ']' restore last stored pen state

        index = 0   # index to change color every step forward 'F'
        turtle_stack = []
        for c in self.str:
            match c:
                case 'F':
                    color = self.color_palette[index % len(self.color_palette)]
                    r, g, b = color[0], color[1], color[2]
                    self.pen.pencolor(r, g, b)
                    self.pen.forward(10)
                    index += 1
                case 'f':
                    self.pen.penup()
                    self.pen.forward(10)
                    self.pen.pendown()
                case '+':
                    self.pen.left(self.angle)
                case '-':
                    self.pen.right(self.angle)
                case '[':
                    pen_position = self.pen.position()
                    pen_heading = self.pen.heading()
                    turtle_stack.append((pen_position, pen_heading))
                case ']':
                    turtle_state = turtle_stack.pop(-1)
                    pen_position = turtle_state[0]
                    pen_heading = turtle_state[1]
                    self.pen.penup()
                    self.pen.setposition(pen_position)
                    self.pen.setheading(pen_heading)
                    self.pen.down()
        self.window.onscreenclick(self.onmouse, btn=1, add=None)
