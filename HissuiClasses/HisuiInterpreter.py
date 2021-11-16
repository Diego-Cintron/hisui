from Objects.vector import vector
from Objects.SHAPES2D.rectangle import rectangle
from Objects.SHAPES2D.square import square
from Objects.SHAPES2D.circle import circle
from Objects.SHAPES2D.triangle import triangle
from Objects.matrix import matrix


class HussuiInterpreter:

    def __init__(self, tree, env):
        self.env = env
        result = self.walkTree(tree)

        if result is not None and isinstance(result, float):
            print(result)

        if result is not None and isinstance(result, int):
            print(result)

        if isinstance(result, str) and result[0] == '"':
            print(result)

        if isinstance(result, list):
            print(result)

        if isinstance(result, vector):
            print(result)

        if isinstance(result, rectangle):
            print(result)

        if isinstance(result, square):
            print(result)

        if isinstance(result, circle):
            print(result)

        if isinstance(result, triangle):
            print(result)

        if isinstance(result, matrix):
            print(result)

        if isinstance(result, dict):
            print(result)

    def walkTree(self, node):

        # Node base cases ======================================================================================

        # Reached node with number value
        if isinstance(node, int):
            return node

        # Reached node with a floating-point number
        if isinstance(node, float):
            return node

        # Reached node with string value
        if isinstance(node, str):
            return node

        # Reached node with a list
        if isinstance(node, list):
            return node

        # Reached node with a vector
        if isinstance(node, vector):
            return node

        if isinstance(node, rectangle):
            return node

        if isinstance(node, square):
            return node

        if isinstance(node, circle):
            return node

        if isinstance(node, triangle):
            return node

        if isinstance(node, matrix):
            return node

        if isinstance(node, dict):
            return node

        # Reached empty node
        if node is None:
            return None

        # Tree algorithms =======================================================================================

        # Goes down the tree nodes
        if node[0] == 'program':
            if node[1] is None:
                self.walkTree(node[2])
            else:
                self.walkTree(node[1])
                self.walkTree(node[2])

        # User input number on the console
        if node[0] == 'num':
            return node[1]

        # User input string on the console. (TO BE REMOVED)
        if node[0] == 'str':
            return node[1]

        # Handles the creation of user functions:
        if node[0] == 'function_def':
            self.env[node[1]] = node[2]

        if node[0] == 'function_call':
            try:
                return self.walkTree(self.env[node[1]])
            except LookupError:
                print("Undefined function '%s'" % node[1])
                return 0

        # Math operations ======================================================================================
        if node[0] == 'add':
            return self.walkTree(node[1]) + self.walkTree(node[2])
        elif node[0] == 'sub':
            return self.walkTree(node[1]) - self.walkTree(node[2])
        elif node[0] == 'mul':
            return self.walkTree(node[1]) * self.walkTree(node[2])
        elif node[0] == 'div':
            return self.walkTree(node[1]) / self.walkTree(node[2])
        elif node[0] == 'mod':
            return self.walkTree(node[1]) % self.walkTree(node[2])
        elif node[0] == 'exp':
            return self.walkTree(node[1]) ** self.walkTree(node[2])

        # Assigns value to variables ===========================================================================
        if node[0] == 'var_assign':
            self.env[node[1]] = self.walkTree(node[2])
            return node[1]

        if node[0] == 'var':
            try:
                return self.env[node[1]]
            except LookupError:
                print("Undefined variable '" + node[1] + "' found!")
                return 0

        # Handles comparisons =====================================================================================
        if node[0] == 'equal':
            return node[1] == node[2]
        elif node[0] == 'greater_eq':
            return node[1] >= node[2]
        elif node[0] == 'less_eq':
            return node[1] <= node[2]
        elif node[0] == 'greater':
            return node[1] < node[2]
        elif node[0] == 'less':
            return node[1] > node[2]

        # If-statements algorithm ==============================================================================
        if node[0] == 'if_stmt':
            result = self.walkTree(node[1])
            if result:
                return self.walkTree(node[2][1])
            return self.walkTree(node[2][2])

        # While loop algorithm ===================================================================================
        if node[0] == 'while_loop':
            while self.walkTree(node[1]):
                res = self.walkTree(node[2])

        # For loop algorithm =======================d=============================================================
        if node[0] == 'for_loop':
            if node[1][0] == 'for_loop_setup':
                loop_setup = self.walkTree(node[1])

                loop_count = self.env[loop_setup[0]]
                loop_limit = loop_setup[1]

                for i in range(loop_count + 1, loop_limit + 1):
                    res = self.walkTree(node[2])
                    self.env[loop_setup[0]] = i

                del self.env[loop_setup[0]]

        if node[0] == 'for_loop_setup':
            return self.walkTree(node[1]), self.walkTree(node[2])

        # List operations =======================================================================================
        if node[0] == 'index':
            lst = self.env[node[1]]
            return lst[node[2]]

        if node[0] == 'size':
            return len(self.env[node[1]])

        if node[0] == 'delete':
            self.env[node[1]].pop(node[2])
            return self.env[node[1]]

        if node[0] == 'lst_add':
            self.env[node[1]].append(node[2][1])
            return self.env[node[1]]

        if node[0] == 'index_change':
            self.env[node[1]][node[2]] = node[3][1]
            return self.env[node[1]]

        if node[0] == 'sort':
            self.env[node[1]].sort()
            return self.env[node[1]]

        if node[0] == 'index_ID':
            lst = self.env[node[1]]
            return self.env[node[1]][self.env[node[2]]]

        # Matrix operations ======================================================================================
        if node[0] == 'xcomp':
            xcomp = self.env[node[1]].x
            return xcomp

        if node[0] == 'ycomp':
            ycomp = self.env[node[1]].y
            return ycomp

        if node[0] == 'zcomp':
            zcomp = self.env[node[1]].z
            return zcomp

        if node[0] == 'magnitude':
            v = self.env[node[1]]
            return v.magnitude()

        if node[0] == 'dot':
            v = self.env[node[1]]
            v2 = self.env[node[2]]
            return v.dot(v2)

        if node[0] == 'cross':
            v = self.env[node[1]]
            v2 = self.env[node[2]]
            return v.cross(v2)

        if node[0] == 'area':
            shape = self.env[node[1]]
            return shape.area()

        if node[0] == 'perimeter':
            shape = self.env[node[1]]
            return shape.perimeter()

        if node[0] == 'diameter':
            shape = self.env[node[1]]
            return shape.diameter

        if node[0] == 'circumference':
            shape = self.env[node[1]]
            return shape.circumference()

        if node[0] == 'adjacent':
            shape = self.env[node[1]]
            return shape.findAdjacent()

        if node[0] == 'hypotenuse':
            shape = self.env[node[1]]
            return shape.findHypotenuse()

        if node[0] == 'opposite':
            shape = self.env[node[1]]
            return shape.findOpposite()

        if node[0] == 'rowADD':
            m = self.env[node[1]]
            return m.addRow(node[2])

        if node[0] == 'printMatrix':
            m = self.env[node[1]]
            return m.printMatrix()

        if node[0] == 'colADD':
            m = self.env[node[1]]
            return m.addCol(node[2])

        if node[0] == 'mADD':
            m = self.env[node[1]]
            return m.addMatrix(node[2])

        if node[0] == 'mSUB':
            m = self.env[node[1]]
            return m.subtractMatrix(node[2])

        if node[0] == 'mMult':
            m = self.env[node[1]]
            return m.multiplyMatrix(node[2])

        if node[0] == 'mDiv':
            m = self.env[node[1]]
            return m.divideMatrix(node[2])

        if node[0] == 'mPow':
            m = self.env[node[1]]
            return m.powMatrix(node[2][1])

