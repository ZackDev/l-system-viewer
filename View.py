from abc import ABC, abstractmethod
import tkinter
import turtle


class AbstractView(ABC):
    @abstractmethod
    def add_menu_entry(name):
        pass

    @abstractmethod
    def update_view(self, name, depth, str):
        pass


class LSystemView(AbstractView):
    def __init__(self, controller):
        self.controller = controller
        self.root = tkinter.Tk()
        self.root.title('l-system-viewer')
        maxsize = self.root.maxsize()

        # canvas
        self.canvas = tkinter.Canvas(
            self.root,
            width=maxsize[0] - 50,
            height=maxsize[1] - 100
        )
        self.canvas.pack()

        # scrollbars
        hscroll = tkinter.Scrollbar(
            self.root,
            orient='horizontal'
        )
        hscroll.pack(
            side='bottom',
            fill='x'
        )
        hscroll.config(command=self.canvas.xview)

        vscroll = tkinter.Scrollbar(
            self.root,
            orient='vertical'
        )
        vscroll.pack(
            side='right',
            fill='y'
        )
        vscroll.config(command=self.canvas.yview)

        self.canvas.config(
            xscrollcommand=hscroll.set,
            yscrollcommand=vscroll.set
        )

        # turtle
        self.pen = turtle.RawTurtle(self.canvas)

        # menu
        self.menucategory = tkinter.Menu(self.root)
        self.menuitems = tkinter.Menu(self.menucategory, tearoff=0)
        self.menucategory.add_cascade(
            label='l-systems',
            menu=self.menuitems
        )
        self.root.config(menu=self.menucategory)

        self.color_palette = [
            (102, 255, 155),
            (0, 204, 255),
            (0, 153, 255),
            (0, 70, 255)
            ]
        self.update_scrollregion()
        self.controller.on_view_init_complete(self)
        self.root.mainloop()

    def add_menu_entry(self, name):
        self.menuitems.add_command(
            label=name,
            command=lambda: self.controller.get_system_by_name(name)
        )

    def update_view(self, name, depth, str, starting_angle, angle):
        self.pen.reset()
        self.name = name
        self.depth = depth
        self.str = str
        self.angle = angle

        self.root.title(f'Name: {self.name} - Depth: {self.depth}')

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
                    self.pen.pencolor(r/255, g/255, b/255)
                    self.pen.pendown()
                    self.pen.forward(10)
                    index += 1
                    self.update_scrollregion()
                case 'f':
                    self.pen.penup()
                    self.pen.forward(10)
                case '+':
                    self.pen.left(self.angle)
                case '-':
                    self.pen.right(self.angle)
                case '[':
                    pen_position = self.pen.pos()
                    pen_heading = self.pen.heading()
                    turtle_stack.append((pen_position, pen_heading))
                case ']':
                    turtle_state = turtle_stack.pop(-1)
                    pen_position = turtle_state[0]
                    pen_heading = turtle_state[1]
                    self.pen.penup()
                    self.pen.setposition(pen_position)
                    self.pen.setheading(pen_heading)
                    self.pen.pendown()

    def update_scrollregion(self):
        self.canvas.config(scrollregion=self.canvas.bbox('all'))
