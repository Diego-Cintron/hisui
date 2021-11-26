import math


class triangle:
    def __init__(self, op, adj, hyp, theta):

        if op[1] > 0:
            self.opposite = op[1]
        else:
            self.opposite = None

        if adj[1] > 0:
            self.adjacent = adj[1]
        else:
            self.adjacent = None

        if hyp[1] > 0:
            self.hypotenuse = hyp[1]
        else:
            self.hypotenuse = None

        if theta[1] > 0:
            self.theta = math.radians(theta[1])
        else:
            self.theta = None

    def area(self):
        return (1 / 2) * self.opposite * self.adjacent

    def perimeter(self):
        return self.adjacent + self.hypotenuse + self.opposite

    def findOpposite(self):
        if self.hypotenuse is not None:
            self.opposite = self.hypotenuse * math.sin(self.theta)
            return self.opposite
        self.opposite = self.adjacent * math.tan(self.theta)
        return self.opposite

    def findAdjacent(self):

        if self.hypotenuse is not None:
            self.adjacent = self.hypotenuse * math.cos(self.theta)
            return self.adjacent
        print(self.theta)
        self.adjacent = self.opposite / (math.tan(self.theta))
        return self.adjacent

    def findHypotenuse(self):
        if self.adjacent is not None:
            self.hypotenuse = self.adjacent / (math.cos(self.theta))
            return self.hypotenuse
        self.hypotenuse = self.opposite / (math.sin(self.theta))
        return self.hypotenuse
