import pygame, tkinter, ctypes, time
from math import pi, cos, sin
from random import randrange, random

root = tkinter.Tk()
os_size = root.winfo_screenwidth(), root.winfo_screenheight() 

SPI_SETDESKWALLPAPER = 20
path = "C:/Users/parde/OneDrive/Programmation/Python/Projets/PY-Game/Visuel/Fractal tree/Tree.png"

screen = pygame.Surface(os_size)

class Branch:
 
    tree = []
    def __init__(self, startPoint, angle, size, width):

        self.width = width
        self.size = size
        self.start = startPoint
        self.angle = angle
        self.end = self.findEndPoint()

        Branch.tree.append(self)
    
    def findEndPoint(self):

        x = self.size*cos(pi/2-self.angle)
        y = self.size*sin(pi/2-self.angle)

        endpoint = (self.start[0] + x, self.start[1] - y)

        return endpoint

    def show(self):

        if self.width<=0:
            self.width = 1

        pygame.draw.line(screen, (200, 200, 200), (self.start[0], self.start[1]), (self.end[0], self.end[1]), self.width)

def grow_branch(branch, angle):

    if branch.size<5:
        return "LOL"
    
    if random()>0.1:
        B_1 = Branch(branch.end, branch.angle + (angle+ 0.2*angle*randrange(-1,2)), branch.size*(randrange(45,101)/100), branch.width-1)
        grow_branch(B_1, angle)

    if random()>0.1:
        B_2 = Branch(branch.end, branch.angle - (angle+ 0.4*angle*randrange(-1,2)), branch.size*(randrange(45,101)/100), branch.width-1)
        grow_branch(B_2, angle)

    if random()>0.5:
        B_3 = Branch(branch.end, branch.angle - (angle+ 0.6*angle*randrange(-1,2)), branch.size*(randrange(50,101)/100), branch.width-1)
        grow_branch(B_3, angle)

done = False
while not done:
    
    screen.fill((30,30,30))

    B = Branch((os_size[0]/2, os_size[1]), 0, 120, 10)
    grow_branch(B, pi/9)
    for branche in Branch.tree:
        branche.show()
    pygame.image.save(screen, path)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)
    # time.sleep(600)
    Branch.tree = []
    done = True