import pygame, pyautogui, time
pygame.init()
w,h=pyautogui.size()
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption("The Rocket")
bg=pygame.image.load("Space.png")
bg=pygame.transform.scale(bg,(w,h))
rocket=pygame.transform.scale(pygame.image.load("Rocket.png"),(300,300))
print(rocket)
rx,ry=w/2,h/2
while ry > 0 and ry < h and rx > 0 and rx < h:
    ry+=0.5
    for i in pygame.event.get():
        print(i)
        if i.type==pygame.QUIT:
            pygame.quit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_UP:
                ry=ry-40
                
    screen.blit(bg,(0,0))
    screen.blit(rocket,(rx,ry))
    pygame.display.update()