from PIL import Image
import math

class cc:
    w, h = 0.0, 0.0 # actual width and height (cm) of the image
    px, py = 0, 0
    im = Image.Image() # loaded image
    l = 0.0

    def __init__(self, fn, w, h):
        self.w, self.h = w, h
        self.im = Image.open(fn, 'r')
        self.px, self.py = self.im.size

    def run(self, dp=10, nt=8):
        n = 0
        rad = math.sqrt(self.px**2 + self.py**2) / 2
        np = int(rad / dp) 

        for i in range(nt):
            t = math.pi/nt * i
            for j in range(-np, np+1):
                p = dp * j
                n += self.count(t, p)    
        scale = (math.sqrt(self.w**2+self.h**2)/math.sqrt(self.px**2+self.py**2))
        self.l = n * dp * scale * (math.pi/nt) / 2
        print(self.l)

    def count(self, t, p):
        cx = int(self.px / 2 + p * math.cos(t))
        cy = int(self.py / 2 + p * math.sin(t))
        # l(s) = (cx, cy) + (-sin(t),cos(t))*s
        # cx - sin(t)*s = 0 or px-1
        # cy + cos(t)*s = 0 or py-1
        e = []
        sl = []
        if math.sin(t) != 0:
            sl.append(cx / math.sin(t))
            sl.append((cx-self.px+1) / math.sin(t))
        if math.cos(t) != 0:
            sl.append(-cy / math.cos(t))
            sl.append((self.py-1-cy) / math.cos(t))
        for s in sl:
            x = int(cx - math.sin(t)*s)
            y = int(cy + math.cos(t)*s)
            if 0 <= x < self.px and 0 <= y < self.py:
                e.append([x, y])
        if len(e) < 2:
            return 0

        dx = abs(e[0][0] - e[1][0])
        dy = abs(e[0][1] - e[1][1])
        if dx >= dy: n = dx
        else:        n = dy
        dx, dy = e[1][0] - e[0][0], e[1][1] - e[0][1]
        l = []
        for i in range(n):
            x = e[0][0] + int(float(i*dx)/float(n))
            y = e[0][1] + int(float(i*dy)/float(n))
            l.append([x, y])
        
        c = 0
        en = True
        for pt in l:
            if self.is_black(pt):
                if en:
                    en = False 
                    c += 1
            else:
                en = True
        return c

    def is_black(self, pt) -> bool:
        px, py = self.im.size
        if self.im.getpixel((pt[0], pt[1]))[0] != 255:
            return True
        return False

if __name__ == '__main__':
    c = cc('test.png', 2, 2)
    c.run(10, 8)