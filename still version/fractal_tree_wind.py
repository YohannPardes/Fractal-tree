import pygame, time
from math import pi, cos, sin
from random import randrange, random

WIDTH = 600
HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Branch:

    tree = []
    random_seed = []
    def __init__(self, startPoint, angle, size, width):

        self.width = width
        self.size = size
        self.start = startPoint
        self.angle = angle
        self.end = self.findEndPoint()

        self.childs = []

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
        branch.childs.append(B_1)

    if random()>0.1:
        B_2 = Branch(branch.end, branch.angle - (angle+ 0.4*angle*randrange(-1,2)), branch.size*(randrange(45,101)/100), branch.width-1)
        grow_branch(B_2, angle)
        branch.childs.append(B_2)

    if random()>0.5:
        B_3 = Branch(branch.end, branch.angle - (angle+ 0.6*angle*randrange(-1,2)), branch.size*(randrange(50,101)/100), branch.width-1)
        grow_branch(B_3, angle)
        branch.childs.append(B_3)


def rotate(branch, direction = 1, depth = 0, loop = 0):

    for child in branch.childs:

        child.start = branch.end
        if branch.size >=8:
            speed_coef = (50-loop)/50
            child.angle += pi/1000*direction*depth*speed_coef
        child.end = child.findEndPoint()
        for chil in child.childs:
            chil.start = child.end
            chil.end = chil.findEndPoint()
            rotate(chil, direction, depth + 1) 

B = Branch((WIDTH/2, HEIGHT), 0, 100, 10)
grow_branch(B, pi/9)
screen.fill((30, 30, 30))
for branche in Branch.tree:
    branche.show()
pygame.display.flip()

done = False
loop = 0
direction = 1
while not done:
    loop += 1
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == 32:
                screen.fill((30, 30, 30))
                for branche in Branch.tree:
                    branche.show()
                Branch.tree = []
                B = Branch((WIDTH/2, HEIGHT), 0, 100, 10)
                grow_branch(B, pi/9)
            pygame.display.flip()

    if (loop/50)%1 == 0:

        print(loop)
        direction *= -1

    rotate(Branch.tree[0], direction, loop = loop)


    for branche in Branch.tree:
        branche.show()

    pygame.display.flip()