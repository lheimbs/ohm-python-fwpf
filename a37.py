#!/usr/bin/env python

class Shape:
    id=0
    def __init__(self):
        self.id = Shape.id
        Shape.id += 1

    def draw(self, painter):
        return (x0, y0, w, h)

    def moveBy(self, dx, dy):
        self.start[0]+=dx
        self.start[1]+=dy
        self.size[0]+=dx
        self.size[1]+=dy

class Group(Shape):
    def __init__(self):
        self.objs = []

    def draw(self, painter):
        if painter is None:
            print(f"group: id #{self.id:d} num_shapes={len(self.objs):d}")
        for obj in self.objs:
            obj.draw(painter)

    def moveBy(self, dx, dy):
        for obj in self.objs:
            obj.moveBy(dx, dy)

    def addShape(self, obj):
        self.objs.append(obj)

    def __iadd__(self, obj):
        self.objs.append(obj)
        return self

class Rect(Shape):
    def __init__(self, x0, y0, w, h):
        super().__init__()
        self.start = [x0, y0]
        self.size   = [w, h]

    def moveBy(self, dx, dy):
        self.start[0] += dx
        self.start[1] += dy
    
    def draw(self, painter):
        if painter is None:
            print(f"rect: id #{self.id:d} x={self.start[0]:d}, y={self.start[1]:d}, w={self.size[0]:d}, h={self.size[1]:d}")
        else:
            painter.drawRect(*self.start,*self.size)


class Line(Shape):
    def __init__(self, x0, y0, x1, y1):
        super().__init__()
        self.start = [x0, y0]
        self.size   = [x1, y1]

    def draw(self, painter):
        if painter is None:
            print(f"line: id #{self.id:d} x={self.start[0]:d}, y={self.start[1]:d}, w={self.size[0]:d}, h={self.size[1]:d}")
        else:
            painter.drawLine(*self.start,*self.size)


if __name__ == "__main__":
    """s1 = Rect(0, 0, 10, 50) 
    s2 = Line(0, 0, 50, 10) 
    
    painter = None 
    s1.draw(painter)
    s2.draw(painter)
    
    s2.moveBy(5, 10) 
    s2.draw(painter)"""

    s1 = Rect(0, 0, 10, 50) 
    s2 = Line(0, 0, 50, 10) 
    s3 = Group() 
    s3.addShape(s1) 
    s3 += s2 
    
    painter = None 
    s2.draw(painter)
    s3.moveBy(5, 10) 
    s3.draw(painter)