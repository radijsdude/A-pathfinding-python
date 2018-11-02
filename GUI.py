
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30,30)

import pygame
from Field import *

pygame.font.init()
fontscale = 15
myfont1 = pygame.font.SysFont('Comic Sans MS', fontscale)

wit = (255, 255, 255)
zwart = (0, 0, 0)
rood = (255, 0, 0)
groen = (0, 255, 0)
blauw = (0, 0, 255)
geel = (255, 255, 0)
oranje = (255, 160, 0)
grijs = (190, 200, 200)
cyanide = (0, 250, 250)
paars = (250, 0, 250)

display_breedte = 800
display_lengte = 600

padding_right = 30
padding_up = 30


class game_lus():
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((display_breedte, display_lengte))
        pygame.display.set_caption('Main')
        self.clock = pygame.time.Clock()
        self.size = 50
        self.field = Field(self.size)
        self.scale = int(display_lengte/(2.1 * self.size))
        self.startnode = '0_{}'.format(str(int(self.size/2)))
        self.endnode = '{}_{}'.format(str(int(self.size-1)),str(int(self.size/2)))
        self.path = []


    def get_position(self,x,y):
        rx = int((x - padding_right)/(2*self.scale))
        ry = int((y - padding_up)/(2*self.scale))
        return str(rx) + '_' + str(ry)

    def run(self):


        stop = False
        currentsquare = None
        while not stop:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    stop = True
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        os.system('cls')
                        self.path = Astar(self.field.field,self.startnode,self.endnode,Distance_Cartesian,Distance_Cartesian)
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

                buttons = pygame.mouse.get_pressed()
                if buttons[0] == 1:
                    mx,my = pygame.mouse.get_pos()
                    s = self.get_position(mx,my)
                    if s in self.field.field and s != currentsquare:
                        self.field.field[s].obstacle = not self.field.field[s].obstacle
                        currentsquare = s
                else:
                    currentsquare = None
                if buttons[2] == 1:
                    mx, my = pygame.mouse.get_pos()
                    s = self.get_position(mx, my)
                    if s in self.field.field:
                        print(self.field.field[s])





            self.display.fill(grijs)
            pygame.draw.rect(self.display,zwart,[0,0,display_breedte,display_lengte],1)

            textsurface = myfont1.render(str(len(self.path)), False, zwart)
            self.display.blit(textsurface, [display_breedte - 3 * fontscale, display_lengte - 2 * fontscale])




            for s in self.field.field:
                sx,sy = s.split('_')
                x,y = int(sx),int(sy)
                kleur = wit
                if s in self.path:
                    kleur = blauw
                if s == self.startnode:
                    kleur = rood

                if self.field.field[s].obstacle:
                    kleur = zwart
                if s == self.endnode:
                    kleur = rood
                rect = [x * 2 * self.scale + padding_right, y * 2 * self.scale + padding_up, self.scale,self.scale]
                pygame.draw.rect(self.display,kleur,rect)
                pygame.draw.rect(self.display,zwart,rect,1)





            pygame.display.update()

            self.clock.tick(40)


game = game_lus()
game.run()