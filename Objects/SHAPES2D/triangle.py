import math
class triangle:
    def __init__(self, op, adj, hyp,theta):

        try:
            self.opposite = op[1]
        except:
            self.opposite = None

        try:
            self.adjacent = adj[1]
        except:
            self.adjacent = None

        try:
            self.hypotenuse = hyp[1]
        except:
            self.hypotenuse = None

        try:
            self.theta = theta[1]
        except:
            self.theta = None

    def area(self):
        return (1/2)*self.opposite*self.adjacent

    def perimeter(self):
        return self.adjacent+self.hypotenuse+self.opposite

    def findOpposite(self):
        if self.hypotenuse is not None:
            self.opposite = self.hypotenuse*math.sin(self.theta)
            return self.opposite
        self.opposite = self.adjacent * math.tan(self.theta)
        return self.opposite

    def findAdjacent(self):
        if self.hypotenuse is not None:
            self.adjacent = self.hypotenuse * math.cos(self.theta)
            return self.adjacent
        self.adjacent = self.opposite/(math.tan(self.theta))
        return self.adjacent

    def findHypotenuse(self):
        if self.adjacent is not None:
            self.hypotenuse = self.adjacent/(math.cos(self.theta))
            return self.hypotenuse
        self.hypotenuse = self.opposite/(math.sin(self.theta))
        return self.hypotenuse
