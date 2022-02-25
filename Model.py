from abc import ABC, abstractmethod


class AbstractModel(ABC):
    @abstractmethod
    def get_system(self):
        pass


class LSystemModel(AbstractModel):
    def __init__(self):
        self.systems = []
        fractal_binary_tree = LSystem(name='Fractal Binary Tree', axiom='0', rules={'0': '1[-0]+0', '1': '11'},
                                      char_map={'0': 'F', '1': 'F'}, starting_angle=90, angle=45, depth=7)

        koch_snowflake = LSystem(name='Koch Curve', axiom='F', rules={'F': 'F+F-F-F+F'},
                                 char_map={}, starting_angle=0, angle=90, depth=4)

        flake = LSystem(name='Koch Snowflake', axiom='F++F++F', rules={'F': 'F-F++F-F'},
                        char_map={}, starting_angle=90, angle=60, depth=4)

        dragon = LSystem(name='Dragon Curve', axiom='FX', rules={'X': 'X+YF+', 'Y': '-FX-Y'},
                         char_map={'X': '', 'Y': ''}, starting_angle=90, angle=90, depth=10)

        sierpinski_triangle = LSystem(name='Sierpinski Triangle', axiom='A', rules={'A': 'B-A-B', 'B': 'A+B+A'},
                                      char_map={'A': 'F', 'B': 'F'}, starting_angle=90, angle=60, depth=5)

        moore = LSystem(name='Moore', axiom='LFL+F+LFL', rules={'L': '-RF+LFL+FR-', 'R': '+LF-RFR-FL+'},
                        char_map={'L': '', 'R': ''}, starting_angle=90, angle=90, depth=4)

        levy = LSystem(name='Levy', axiom='F', rules={'F': '+F--F+'},
                            char_map={}, starting_angle=0, angle=45, depth=9)

        hilbert = LSystem(name='Hilbert Curve', axiom='A', rules={'A': '-BF+AFA+FB-', 'B': '+AF-BFB-FA+'},
                          char_map={'A': '', 'B': ''}, starting_angle=90, angle=90, depth=5)

        gosper = LSystem(name='Gosper Curve', axiom='X', rules={'X': 'X+YF++YF-FX--FXFX-YF+', 'Y': '-FX+YFYF++YF+FX--FX-Y'},
                         char_map={'X': '', 'Y': ''}, starting_angle=90, angle=60, depth=4)

        minkowsky = LSystem(name='Minkiwski sausage', axiom='F', rules={'F': 'F+F-F-FF+F+F-F'},
                            char_map={}, starting_angle=90, angle=90, depth=3)

        peano = LSystem(name='Peano Curve', axiom='F', rules={'F': 'F+F-F-F-F+F+F+F-F'},
                        char_map={}, starting_angle=90, angle=90, depth=3)

        sierpinski_sieve = LSystem(name='Sierpinski Sieve', axiom='YF', rules={'X': 'YF+XF+Y', 'Y': 'XF-YF-X'},
                                   char_map={'X': '', 'Y': ''}, starting_angle=90, angle=60, depth=5)

        koch_antisnowflake = LSystem(name='Koch Antisnowflake', axiom='F++F++F', rules={'F': 'F+F--F+F'},
                                     char_map={}, starting_angle=90, angle=60, depth=4)

        koch_island = LSystem(name='Quadratic Koch Island', axiom='F+F+F+F', rules={'F': 'F+F-F-FF+F+F-F'},
                              char_map={}, starting_angle=90, angle=90, depth=3)

        sierpinski_curve = LSystem(name='Sierpinski Curve', axiom='F+XF+F+XF', rules={'X': 'XF-F+F-XF+F+XF-F+F-X'},
                                   char_map={'X': ''}, starting_angle=90, angle=90, depth=4)

        terdragon = LSystem(name='Terdragon', axiom='F', rules={'F': 'F+F-F'},
                            char_map={}, starting_angle=90, angle=120, depth=7)

        crystal = LSystem(name='Crystal', axiom='F', rules={'F': 'F+F--X+F-F++X-F', 'X': 'XXX'},
                          char_map={'X': 'F'}, starting_angle=90, angle=90, depth=4)

        island_and_lakes = LSystem(name='Island and Lakes', axiom='F+F+F+F', rules={'F': 'F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF', 'f': 'ffffff'},
                                   char_map={}, starting_angle=90, angle=90, depth=2)

        pentadentrite = LSystem(name='Pentadentrite', axiom='F', rules={'F': 'F+F-F--F+F+F'},
                                char_map={}, starting_angle=90, angle=72, depth=4)

        sierpinski_carpet = LSystem(name='Sierpinski Carpet', axiom='F', rules={'F': 'F+F-F-FF-F-F-fF', 'f': 'fff'},
                                    char_map={}, starting_angle=90, angle=90, depth=4)

        custom_flower = LSystem(name='Flower', axiom='F-F-F-F-F-F', rules={'F': 'F+F+F-F-F-F+F+F'},
                                char_map={}, starting_angle=90, angle=60, depth=0)

        custom_flower2 = LSystem(name='Flower', axiom='F-F-F-F-F-F', rules={'F': 'F+F+F-F-F-F+F+F'},
                                 char_map={}, starting_angle=90, angle=60, depth=1)

        custom_flower3 = LSystem(name='Flower', axiom='F-F-F-F-F-F', rules={'F': 'F+F+F-F-F-F+F+F'},
                                 char_map={}, starting_angle=90, angle=60, depth=2)

        custom_flower4 = LSystem(name='Flower', axiom='F-F-F-F-F-F', rules={'F': 'F+F+F-F-F-F+F+F'},
                                 char_map={}, starting_angle=90, angle=60, depth=3)

        fractal_plant = LSystem(name='Fractal Plant', axiom='X', rules={'X': 'F+[[X]-X]-F[-FX]+X', 'F': 'FF'},
                                char_map={}, starting_angle=90, angle=25, depth=3)

        fractal_plant1 = LSystem(name='Fractal Plant', axiom='X', rules={'X': 'F+[[X]-X]-F[-FX]+X', 'F': 'FF'},
                                 char_map={}, starting_angle=90, angle=25, depth=6)

        fractal_thing = LSystem(name='Fractal Thing', axiom='[f+F+F+F+F+F+F+F+F+F+F]', rules={'F': 'FF', 'f': 'ff'},
                                char_map={}, starting_angle=90, angle=36, depth=5)

        self.systems.append(fractal_binary_tree)
        self.systems.append(koch_snowflake)
        self.systems.append(flake)
        self.systems.append(koch_antisnowflake)
        self.systems.append(koch_island)
        self.systems.append(island_and_lakes)
        self.systems.append(dragon)
        self.systems.append(terdragon)
        self.systems.append(sierpinski_triangle)
        self.systems.append(sierpinski_sieve)
        self.systems.append(sierpinski_curve)
        self.systems.append(sierpinski_carpet)
        self.systems.append(moore)
        self.systems.append(levy)
        self.systems.append(hilbert)
        self.systems.append(gosper)
        self.systems.append(minkowsky)
        self.systems.append(peano)
        self.systems.append(crystal)
        self.systems.append(pentadentrite)
        self.systems.append(fractal_plant)
        self.systems.append(fractal_plant1)

    def get_system(self):
        try:
            return self.systems.pop(0)
        except Exception:
            return None


class LSystem:
    def __init__(self, name, axiom, rules, char_map, starting_angle, angle, depth):
        self.name = name
        self.axiom = axiom
        self.rules = rules
        self.char_map = char_map
        self.starting_angle = starting_angle
        self.angle = angle
        self.depth = depth
        self.str = self.str_system(self.axiom, self.depth)

    def str_system(self, axiom, depth):
        if depth > 0:
            result = ''
        else:
            result = axiom
            # apply char_map to remove irrelevant characters for drawing
            for key, mapping in self.char_map.items():
                result = result.replace(key, mapping)
        while depth > 0:
            for c in axiom:
                # indicates weather a rule for c has been found or not
                rule_exists = False
                # apply rules
                for key, substitute in self.rules.items():
                    if c == key:
                        # set found flag, append substitute and leave loop
                        rule_exists = True
                        result += substitute
                        break
                if not rule_exists:
                    # if there is no rule, simply copy the character
                    result += c
            depth -= 1
            return self.str_system(result, depth)
        return result
