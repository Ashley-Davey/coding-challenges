import pygame
from random import uniform
from pygame.gfxdraw import filled_circle, line


'''
    ----------------------------------------------
    Coding Challenge #1: Star Field in Processing:
    ----------------------------------------------
    
    This is a python version of the coding challenge from Daniel Shiffman on The Coding Train
    
    Original coding challenge: 
        https://www.youtube.com/watch?v=17WoOqgXsRM&list=PLRqwX-V7Uu6ZiZxtDDRCi6uhfTH4FilpH

'''

def lerp(x, a, b, c, d):
    constrained = min(b,max(x,a))
    return int(c + (d - c) * (constrained - a) / (b - a))


class Star():
    def __init__(self, w, h, rand = True):
        self.x = uniform(-w, w)
        self.y = uniform(-h, h)
        self.z = uniform(0, w) if rand else w
        self.pz = self.z
        
    def update(self, w, h, s):
        self.z -= s
        if self.z < 1:
            self.__init__(w, h, False)
    
    def show(self, w, h, surface):
        

        sx = lerp(self.x / self.z, -1, 1, -w, w) + int(w / 2)
        sy = lerp(self.y / self.z, -1, 1, -h, h) + int(h / 2)
        r =  lerp(self.z, 0, w, 8, 0)
        filled_circle(surface, sx, sy, r, (255,255,255))
        
        px = lerp(self.x / self.pz, -1, 1, -w, w) + int(w / 2)
        py = lerp(self.y / self.pz, -1, 1, -h, h) + int(h / 2)
        line(surface, px, py, sx, sy, (255,255,255))
        self.pz = self.z
        
        
def main():
    pygame.init()
    clock = pygame.time.Clock()
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    
    stars = [Star(width,height) for _ in range(800)]
    
    
    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                return
        screen.fill((0,0,0))
        mouseX = pygame.mouse.get_pos()[0]
        speed = mouseX * 50 / width
        for star in stars:
            star.update(width, height, speed)
            star.show(width, height, screen) 
        

        
        pygame.display.flip()
    
if __name__ == '__main__':
    main()