__author__ = 'yanev'

from math import sqrt
from operator import attrgetter


class Node:
    x = 0
    y = 0
    f_score = 0
    g_score = 0
    walkable = True

    def __str__(self):
        return "[ " + str(self.x) + ", "+ str(self.y) + " " + str(self.walkable) + " ]"

def heuristicScore(a, b):
    return sqrt(pow((a.x - b.x), 2) + (pow((a.y - b.y), 2)))



path = []
def r_path(dic, point):
    if point in dic:
        if isinstance(r_path(dic, dic[point]), Node):
            path.append(r_path(dic, dic[point]))
        path.append(point)
        return path
    else:
        return point


def isWalkable(a):
    return a.walkable


def neigh_nodes(a, grid):
    nodes = []
    if a.x + 1 < len(grid[0]):
        if isWalkable(grid[a.y][a.x + 1]):
            nodes.append(grid[a.y][a.x + 1])

    if a.x - 1 > -1:
        if isWalkable(grid[a.y][a.x - 1]):
            nodes.append(grid[a.y][a.x - 1])

    if a.y + 1 < len(grid):
        if isWalkable(grid[a.y + 1][a.x]):
            nodes.append(grid[a.y + 1][a.x])

    if a.y - 1 > -1:
        if isWalkable(grid[a.y - 1][a.x]):
            nodes.append(grid[a.y - 1][a.x])

    return nodes

def __aStar(start, end, grid):
    # print "NODES"
    # for nodes in grid:
    #     for node in nodes:
    #         print node,
    #     print
    closed_set = set([])
    open_set = set([start])
    dic = {}
    start.g_score = 0
    start.f_score = start.g_score + heuristicScore(start, end)

    while len(open_set) > 0:
        current = min(open_set, key=attrgetter("f_score"))
        if current == end:
            path = r_path(dic, end)
            return path
        open_set.remove(current)
        closed_set.add(current)
        # neigs = neigh_nodes(current, grid)
        # print '---------------'
        # print "Neighs for", current
        # for n in neigs:
        #     print n.x, n.y
        # print '---------------'
        for a in neigh_nodes(current, grid):
            if a in closed_set:
                continue
            t_g_score = current.g_score + 1

            if a not in open_set or t_g_score < current.g_score:
                dic[a] = current
                a.g_score = t_g_score
                a.f_score = a.g_score + heuristicScore(a, end)
                if a not in open_set:
                    open_set.add(a)

    return [] # no path was found from start to end

def aStar(gri, start=None, end=None):
    grid = createMatrix(gri)
 #   for line in grid:
 #       for node in line:
 #           print node,
 #       print
    #print "grid3", grid
    if(start == None and end == None):
        start = grid[0][0]
        end = grid[len(grid) - 1][-1]
#        print "END:", end
    return __aStar(start, end, grid)

def createMatrix(lines):
    grid = []
    y = 0
    for line in lines:
        if isinstance(line, str) or isinstance(line, unicode):
            line = line.strip()
        line = [int(x) for x in line]
        temp = []
        for x in range(len(line)):
            n = Node()
            n.x = x
            n.y = y
            n.walkable = (line[x] == 1)
            temp += [n]
 #           print n.x, n.y
        grid += [temp]
        y += 1
    return grid


if __name__ == "__main__":

    lines = []
    f = open("grid3x4", 'rb')
    lines = f.readlines()
    f.close()

    #grid = createMatrix(lines)

    wayOut = aStar(lines)
    if (not wayOut):
        print "NO WAY OUT MUHAHAHA u suck"
        exit (1)
    print "Exit found in:", len(wayOut), "moves"
    for el in wayOut:
        print (el.x, el.y),

