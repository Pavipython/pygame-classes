import pygame, random, time
pygame.init()
screen=pygame.display.set_mode((600,600))

colors=["blue", "red", "green", "yellow"]
size=(100, 450, 200, 175)

class Ball:
    def __init__ (self, x, y, r ):
        self.x=x
        self.y=y
        self.r=r
        self.c=random.choice(colors)
    def display(self):
        pygame.draw.circle(screen, self.c, (self.x, self.y), self.r)
    
py = Ball(100,200,10)

while True:
    screen.fill(0)
    py.display()
    pygame.display.update()
    py.r=random.choice(size)
    py.x=random.randint(20,400)
    py.c=random.choice(colors)
    #time.sleep(1)