class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def cross(self,v2):
        x = self.x
        y = self.y
        z = self.z
        x2 = v2.x
        y2 = v2.y
        z2 = v2.z

        newx = (y*z2-z*y2)
        newy = (z*x2-x*z2)
        newz = (x*y2-y*x2)
        return vector(newx,newy,newz)

    def dot(self, v2):
        x = self.x
        y = self.y
        z = self.z
        x2 = v2.x
        y2 = v2.y
        z2 = v2.z
        return (x * x2) + (y * y2) + (z * z2)

    def magnitude(self):
        power = (self.x ** 2) + (self.y ** 2) + (self.z ** 2)
        return power ** (1 / 2)
