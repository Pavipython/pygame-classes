import pygame, pyautogui, time, random
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Object oriented programming using pygame")

colors=["blue", "white", "yellow", "green"]

class Box:
    def __init__(self, x, y, w, h, c):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.c=c
    def display(self):
        pygame.draw.rect(screen, self.c,(self.x, self.y, self.w, self.h))

red = Box(100,100,200,100,"red")

while True:
    screen.fill(0)
    # red.w-=1
    # red.h-=1
    red.display()
    pygame.display.update()
    red.c=random.choice(colors)
    time.sleep(2)
    
