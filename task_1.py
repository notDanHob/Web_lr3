from math import pi

class Sphere:
    def __init__(self,radius = 1,x= 0,y = 0,z = 0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z 
    def get_volume_(self):  return 4/3*pi*self.radius**3
    def get_square_(self):  return 4*pi*self.radius**2
    def get_radius_(self):  return self.radius
    def get_center_(self):  return (self.x,self.y,self.z)
    def set_radius_(self, r):  self.radius = r
    def set_center (self, x, y, z):  
        self.x, self.y, self.z = x, y, z
    def is_point_inside_(self, x, y, z):
        return (x**2 + y**2 + z **2) < self.radius**2
https://www.youtube.com/watch?v=mvqUu2fZixI&ab_channel=IssaBreh
