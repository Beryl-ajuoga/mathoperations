class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area (self):
        return self.radius**2*3.142  


    def circumference(self):
        return self.radius *3.142

class Square:
    def __init__(self,side):
        self.side=side

    def Area(self):
        return self.side**2  

    def perimeter(self):
        return 4 *  self.side  


class Rectangular:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        w=2*(self.length * self.width)
        return w
    def perimeter(self):
        h=  2*(self.length + self.width)  
        return h

class Sphere:
    def __init__(self,radius):
         self.radius=radius

    def calculate_area(self):
        Area=4*3.142*self.radius**2
        return Area

    def Volume(self):
        volumes=(4/3)*3.142* self.radius*self.radius
        return volumes  


