from Astar import *

def Distance_Cartesian(node1,node2):
    x1,y1 = node1.pos
    x2,y2 = node2.pos
    d = ((x1-x2)**2 + (y1-y2)**2) **(1/2)
    return d

class Field:
    def __init__(self,size):
        self.size = size
        self.field = {}
        for i in range(size):
            for j in range(size):
                s = str(i) + '_' + str(j)
                self.field[s] = Node(s,0,[i,j])
        for s in self.field:
            x,y = self.field[s].pos
            if x > 0:
                nx = x - 1
                ny = y
                ss = str(nx) + '_' + str(ny)
                self.field[s].neighbours.append(ss)
                if y > 0:
                    nx = x - 1
                    ny = y - 1
                    ss = str(nx) + '_' + str(ny)
                    self.field[s].neighbours.append(ss)
            if x < self.size - 1:
                nx = x + 1
                ny = y
                ss = str(nx) + '_' + str(ny)
                self.field[s].neighbours.append(ss)
                if y < self.size - 1:
                    nx = x + 1
                    ny = y + 1
                    ss = str(nx) + '_' + str(ny)
                    self.field[s].neighbours.append(ss)
            if y > 0:
                nx = x
                ny = y - 1
                ss = str(nx) + '_' + str(ny)
                self.field[s].neighbours.append(ss)
                if x < self.size - 1:
                    nx = x + 1
                    ny = y - 1
                    ss = str(nx) + '_' + str(ny)
                    self.field[s].neighbours.append(ss)
            if y < self.size - 1:
                nx = x
                ny = y + 1
                ss = str(nx) + '_' + str(ny)
                self.field[s].neighbours.append(ss)
                if x > 0:
                    nx = x - 1
                    ny = y + 1
                    ss = str(nx) + '_' + str(ny)
                    self.field[s].neighbours.append(ss)
