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
    def grow(self):
        self.w+=10
        self.h+=10
        self.x-=5
        self.y-=5
        pygame.draw.rect(screen, self.c,(self.x, self.y, self.w, self.h))



rects=[]

while True:
    #screen.fill(0)
    # red.w-=1
    # red.h-=1
    for i in pygame.event.get():
        print(i)
        if i.type==pygame.QUIT:
            pygame.quit()
        if i.type==pygame.MOUSEBUTTONDOWN:
            red = Box(280,280,40,40,random.choice(colors))
            rects.append(red)
        if i.type==pygame.MOUSEBUTTONUP:
            for i in rects:
                i.grow()
    
            

    
    for i in rects:
        i.display()
    pygame.display.update()
    #red.c=random.choice(colors)
    #time.sleep(2)
    
