import pygame
from math import pi, cos, sin
from random import randrange, random

WIDTH = 900
HEIGHT = 720

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

def mapNbs (nb ,x1, y1, x2, y2):

    #adding the offset
    nb += x2-x1

    #stretching to the ratio
    nb*=(y2-x2)/(y1-x2)

    return nb

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

    if branch.size<10:
        return "LOL"
    
    B_1 = Branch(branch.end, branch.angle+angle, branch.size*0.6, branch.width-1)
    grow_branch(B_1, angle)
    B_2 = Branch(branch.end, branch.angle-angle, branch.size*0.6, branch.width-1)
    grow_branch(B_2, angle)
    B_3 = Branch(branch.end, branch.angle, branch.size*0.6, branch.width-1)
    grow_branch(B_3, angle)
    
# B = Branch((WIDTH/2, HEIGHT), 0, 100, 500)
pos = 0
add = 0
reverse = False
done = False
speed = 0.002
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEMOTION:
            pos = event.pos[0]
            pass
        elif event.type == pygame.KEYDOWN:
            if event.key == 32:
                done = True

    screen.fill((30,30,30))
    Branch.tree =[]
    B = Branch((WIDTH/2, HEIGHT), 0, size = 300, width = 10)
    grow_branch(B, mapNbs(pos, 0, WIDTH, 0, pi))

    for branche in Branch.tree:
        branche.show()
        
    pygame.display.flip()