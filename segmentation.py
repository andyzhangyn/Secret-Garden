from PIL import Image, ImageFilter
import numpy
import random
import queue as queue
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Segments:

    def __init__(self, image_name, file_name):
        f = open(file_name, 'w')
        self.segments = []
        self.name = image_name
        self.file_name = file_name
        self.image = Image.open(image_name)
        self.pix = self.image.load()
        self.height = self.image.height
        self.width = self.image.width
        self.visited = numpy.zeros(shape = (self.width, self.height))
        self.num = 1
        for w in range(self.width):
            for h in range(self.height):
                if not self.visited[w][h] and self.pix[w, h] == WHITE:
                    r = Region()
                    q = queue.Queue()
                    self.bfs(w, h, r, q)
                    self.segments.append(r)
                    self.save_to_file(r)
                    print('checkpoint', self.num)
                    self.num += 1
        print('Segmentation is completed!')
        f.close()

    def bfs(self, x, y, region, q):
        q.put([x, y])
        self.visited[x][y] = True
        while(not q.empty()):
            pixel = q.get()
            x = pixel[0]
            y = pixel[1]
            region.add_pixel(x, y)
            if x+1 < self.width and not self.visited[x+1][y] and self.pix[x+1, y] == WHITE:
                q.put([x+1, y])
                self.visited[x+1][y] = True
            if x-1 >= 0 and not self.visited[x-1][y] and self.pix[x-1, y] == WHITE:
                q.put([x-1, y])
                self.visited[x-1][y] = True
            if y+1 < self.height and not self.visited[x][y+1] and self.pix[x, y+1] == WHITE:
                q.put([x, y+1])
                self.visited[x][y+1] = True
            if y-1 >= 0 and not self.visited[x][y-1] and self.pix[x, y-1] == WHITE:
                q.put([x, y-1])
                self.visited[x][y-1] = True

    def save_to_file(self, region):
        f = open(self.file_name, 'a')
        for x, y in region.pixels:
            f.write(str(x) + ' ' + str(y) + ' ')
        f.write('checkpoint')

class Region:

    def __init__(self, color=WHITE):
        self.color = color
        self.pixels = []
        self.size = 0

    def add_pixel(self, x, y):
        self.pixels.append([x, y])
        self.size += 1