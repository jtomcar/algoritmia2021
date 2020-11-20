'''
Created on 20/11/2013

@author: david
'''
from easycanvas import EasyCanvas

def get_bounding_box(points, margin = 0.1): # margin = 0.1 es un 10% de borde
    margin /= 2
    minx = min(p[0] for p in points)
    maxx = max(p[0] for p in points)
    miny = min(p[1] for p in points)
    maxy = max(p[1] for p in points)
    width = maxx-minx
    height = maxy-miny
    return (minx-margin*width,miny-margin*height,maxx+margin*width,maxy+margin*height)

def read_instance(filename):
    file = open(filename)
    n = int(file.readline().strip())
    points = []
    for lin in file:
        x,y =(float(n) for n in lin.strip().split())
        points.append((x,y))
    file.close()
    return points

def read_solution(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    alg1 = [int(x) for x in lines[1].strip()[1:-1].split(',')]
    alg2 = [int(x) for x in lines[3].strip()[1:-1].split(',')]
    return alg1, alg2

class TspViewer(EasyCanvas):
    def __init__(self, coords, route):
        EasyCanvas.__init__(self)
        self.canvas_width = self.root.winfo_screenwidth()*0.8
        self.canvas_height = self.root.winfo_screenheight()*0.8
        self.coords = coords
        self.route = list(route)
      
    def main(self):
        minx, miny, maxx, maxy = get_bounding_box(self.coords)
        aspect_ratio = (maxx-minx)/(maxy-miny)
        if self.canvas_width/self.canvas_height < aspect_ratio:
            self.canvas_height = self.canvas_width/aspect_ratio
        else:
            self.canvas_width = self.canvas_height*aspect_ratio
        
        # Configura la ventana del canvas
        self.easycanvas_configure(title = 'Traveling Salesman Route',
                                  background = 'white',
                                  size = (self.canvas_width, self.canvas_height), 
                                  coordinates = (minx, miny, maxx, maxy)) # al intercambiar miny y maxy hacemos que las y crezcan hacia abajo
        r = min(maxx-minx,maxy-miny)/300
        for points in self.coords:
            self.create_circle(points[0], points[1], r, 'blue')

        if len(self.route)>0:
            x1, y1 = self.coords[self.route[0]]
            for r in self.route[1:]+[self.route[0]]:
                x2, y2 = self.coords[r]
                self.create_line(x1,y1,x2,y2)
                x1, y1 = x2, y2
        self.readkey(True)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        print("Use: e2_viewer.py <-1|-2|-3> <instance.ins> <instance.sol>")
        sys.exit()

    try:
        coords = read_instance(sys.argv[2])
    except:
        print("ERROR: Bad format in instance file")
        sys.exit()

    try:
        routes = read_solution(sys.argv[3])
    except:
        print("ERROR: Bad format in solution file")
        sys.exit()

    alg = sys.argv[1]
    route = []
    if alg == '-1':
        route = routes[0]
    elif alg == '-2':
        route = routes[1]
    else:
        print("ERROR: Unknown algorithm (must be -1 or -2):", alg)
        print("Use: e2_viewer.py <-1|-2> <instance.ins> <instance.sol>")
        sys.exit()

    TspViewer(coords, route).run()
