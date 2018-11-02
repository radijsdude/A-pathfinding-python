infinity = 'INFINITY'
class Node:
    def __init__(self,name,value,pos):
        self.name = name
        self.value = value
        self.pos = pos
        self.neighbours = []
        self.parent = None
        self.distance_local = infinity
        self.distance_global = infinity
        self.obstacle = False
        self.visited = False
    def __repr__(self):
        s = ''
        s += 'name:' + str(self.name) + ' '
        s += 'goal:' + str(self.distance_global)
        s += 'parent:' + str(self.parent) + ' '
        s += 'neighbours:' + str(self.neighbours) + ' '
        return s
def Astar(nodes,startnodename,endnodename,distance_local,distance_global):
    print('astar')
    for s in nodes:
        nodes[s].distance_local = infinity
        nodes[s].distance_global = infinity
        nodes[s].parent = None
        nodes[s].visited = False
    nodes[startnodename].distance_local = 0
    nodes[startnodename].distance_global = distance_global(nodes[startnodename],nodes[endnodename])
    untestednodes = [nodes[startnodename]]
    currentnode = untestednodes[0]
    while untestednodes != [] and currentnode.name != endnodename:
        untestednodes = sorted(untestednodes,key=lambda x: x.distance_global)
        if untestednodes != []:
            while untestednodes[0].visited:
                untestednodes.pop(0)
                if untestednodes == []:
                    break
        if untestednodes == []:
            break
        currentnode = untestednodes[0]
        currentnode.visited = True
        for neighbourname in currentnode.neighbours:
            if not nodes[neighbourname].visited and not nodes[neighbourname].obstacle:
                untestednodes.append(nodes[neighbourname])
            possiblelowest = currentnode.distance_local + distance_local(currentnode,nodes[neighbourname])
            if nodes[neighbourname].distance_global != infinity:
                if possiblelowest < nodes[neighbourname].distance_local:
                    nodes[neighbourname].parent = currentnode.name
                    nodes[neighbourname].distance_local = possiblelowest
                    global_distance = possiblelowest + distance_global(nodes[neighbourname],nodes[endnodename])
                    nodes[neighbourname].distance_global = global_distance
            else:
                nodes[neighbourname].parent = currentnode.name
                nodes[neighbourname].distance_local = possiblelowest
                global_distance = possiblelowest + distance_global(nodes[neighbourname],nodes[endnodename])
                nodes[neighbourname].distance_global = global_distance

    name = endnodename
    path = [endnodename]
    t = 0
    while name != startnodename:
        if name == None:
            print('No path found')
            break
        name = nodes[name].parent
        path.append(name)
        t += 1
        if t > 5000:
            print('while loop break')
            break
    return path
