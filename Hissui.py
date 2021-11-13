from sly import Lexer
from sly import Parser
from Objects.vector import vector
from Objects.SHAPES2D.rectangle import rectangle
from Objects.SHAPES2D.square import square
from Objects.SHAPES2D.circle import circle
from Objects.SHAPES2D.triangle import triangle


# Creating a Lexer who inherits from sly's lexer.oy class
class HissuiLexer(Lexer):
    # Inputting the tokens that the parser will be able to use.
    # Temporarily REMOVED TOKENS:
    #   SQUARE, CIRCLE, RECTANGLE, TRIANGLE, VECTOR, MATRIX, NEW,
    #   ELSEIF, IN, COMMA, COLON, RETURN,
    tokens = {ID, NUMBER, STRING, EQUAL, COLON,
              # statement tokens
              IF, THEN, ELSE, FOR, TO, WHILE,

              # Comparison tokens
              GREATEREQ, LESSEQ, COMMA,

              # Vectors
              VECTOR, DOT, CROSS, XCOMP, YCOMP, ZCOMP, MAGNITUDE, COMPONENTS,

              # Dictionary
              DICTIONARY,

              # Shapes
              RECTANGLE, SQUARE, AREA, PERIMETER, CIRCLE, DIAMETER, CIRCUMFERENCE,
              TRIANGLE,OPPOSITE,ADJACENT,HYPOTENUSE,

              # List Tokens
              LIST, SIZE, REMOVE, ADD, SORT}

    # Lexer can read letters and combinations of letters and numbers
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    # ignore whitespaces or tabs.
    ignore = ' \t'

    # Reads single digits or multiple digits.
    NUMBER = r'\d+'

    # making the values inside the token integers
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    #
    # Defining strings
    STRING = r'\".*?\"'

    # stating the operators
    literals = {'+', '-', '/', '*', '^', '=', '(', ')', '<', '>', '%', '[', ']', '.'}

    # establishing function characters
    GREATEREQ = r'>='
    LESSEQ = r'<='
    EQUAL = r'=='
    COMMA = r','
    COLON = r':'

    # implementing standard language clauses.
    ID['if'] = IF
    ID['then'] = THEN
    ID["else"] = ELSE
    ID['list'] = LIST
    ID['for'] = FOR
    ID['to'] = TO
    ID['while'] = WHILE

    # List methods
    ID['list'] = LIST
    ID['size'] = SIZE
    ID['remove'] = REMOVE
    ID['add'] = ADD
    ID['sort'] = SORT

    ID['vector'] = VECTOR
    ID['cross'] = CROSS
    ID['dot'] = DOT
    ID['xc'] = XCOMP
    ID['yc'] = YCOMP
    ID['zc'] = ZCOMP
    ID['magnitude'] = MAGNITUDE

    ID['dictionary'] = DICTIONARY

    # Adding different functional objects
    ID['square'] = SQUARE
    ID["rectangle"] = RECTANGLE
    ID['area'] = AREA
    ID['perimeter'] = PERIMETER
    ID['circumference'] = CIRCUMFERENCE
    ID['diameter'] = DIAMETER
    ID['triangle'] = TRIANGLE
    ID['circle'] = CIRCLE
    ID['hypotenuse'] = HYPOTENUSE
    ID['opposite'] = OPPOSITE
    ID['adjacent'] = ADJACENT
    # ID['matrix'] = MATRIX

    # new token for object creation
    # ID['new'] = NEW

    # Error handling
    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1


class HissuiParser(Parser):
    tokens = HissuiLexer.tokens

    # Tells code to use proper order of operation while doing math operations
    precedence = (
        ('left', '+', '-'),
        ('left', '%', '*', '/', '^', GREATEREQ, LESSEQ, '<', '>', EQUAL),
        ('right', 'UMINUS'),
    )

    def __init__(self):
        self.env = {}

    # Ignores whitespace
    @_('')
    def statement(self, p):
        pass

    # @_('FUN ID "(" ")" ARROW statement')
    # def statement(self, p):
    #     return ('fun_def', p.ID, p.statement)

    # @_('ID "(" ")"')
    # def statement(self, p):
    #     return ('fun_call', p.ID)

    # Variable Declaration =============================================================================================

    # Assigns value to a variable
    @_('var_assign')
    def statement(self, p):
        return p.var_assign

    @_('ID "=" expr')
    def var_assign(self, p):
        return 'var_assign', p.ID, p.expr

    @_('ID "=" STRING')
    def var_assign(self, p):
        return 'var_assign', p.ID, p.STRING

    # @_('ID "=" MATRIX')
    # def statement(self, p):
    #     self.ids[p.ID] = p.MATRIX
    #     return p.ID, p.MATRIX
    #

    # Prints out expression once it no longer has any operations left
    @_('expr')
    def statement(self, p):
        return p.expr

    # Expression Handling ==============================================================================================

    # Does addition
    @_('expr "+" expr')
    def expr(self, p):
        return 'add', p.expr0, p.expr1

    # Does subtraction
    @_('expr "-" expr')
    def expr(self, p):
        return 'sub', p.expr0, p.expr1

    # Does multiplication
    @_('expr "*" expr')
    def expr(self, p):
        return 'mul', p.expr0, p.expr1

    # Does division
    @_('expr "/" expr')
    def expr(self, p):
        return 'div', p.expr0, p.expr1

    # Does module
    @_('expr "%" expr')
    def expr(self, p):
        return 'mod', p.expr0, p.expr1

    # Does exponent
    @_('expr "^" expr')
    def expr(self, p):
        return 'exp', p.expr0, p.expr1

    # Parses individual negative numbers
    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return p.expr

    # Parses expressions inside parenthesis
    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    # Parses numbers
    @_('NUMBER')
    def expr(self, p):
        return 'num', p.NUMBER

    # # Parses strings
    @_('STRING')
    def expr(self, p):
        return 'str', p.STRING

    # Parses variables
    @_('ID')
    def expr(self, p):
        return 'var', p.ID

    # Condition Handling ===============================================================================================

    # Parses the EQUAL token
    @_('expr EQUAL expr')
    def condition(self, p):
        return 'equal', p.expr0, p.expr1

    # Parses greater-than or equal token.
    @_('expr GREATEREQ expr')
    def condition(self, p):
        return 'greater_eq', p.expr0, p.expr1

    # Parses less-than or equal token.
    @_('expr LESSEQ expr')
    def condition(self, p):
        return 'less_eq', p.expr0, p.expr1

    # Parses greater-than token.
    @_('expr ">" expr')
    def condition(self, p):
        return 'greater', p.expr0, p.expr1

    # Parses less-than token.
    @_('expr "<" expr')
    def condition(self, p):
        return 'less', p.expr0, p.expr1

    # If-statements ====================================================================================================

    @_('IF condition THEN statement ELSE statement')
    def statement(self, p):
        return 'if_stmt', p.condition, ('branch', p.statement0, p.statement1)

    @_('IF condition THEN expr ELSE expr')
    def statement(self, p):
        return 'if_stmt', p.condition, ('branch', p.expr0, p.expr1)

    # Loops ============================================================================================================

    @_('WHILE condition THEN statement')
    def statement(self, p):
        return 'while_loop', p.condition, p.statement

    @_('FOR var_assign TO expr THEN statement')
    def statement(self, p):
        return 'for_loop', ('for_loop_setup', p.var_assign, p.expr), p.statement

    @_('FOR var_assign TO expr THEN expr')
    def statement(self, p):
        return 'for_loop', ('for_loop_setup', p.var_assign, p.expr0), p.expr1

    # Lists ============================================================================================================
    @_('ID "=" LIST "[" [ expr ] { COMMA expr } "]" ')
    def var_assign(self, p):
        lst2 = []
        if p.expr0 is None:
            lst = []
        else:
            lst = p.expr1
            lst.insert(0, p.expr0)
        for i in range(0, len(lst)):
            lst2.append(lst[i][1])
        return 'var_assign', p.ID, lst2

    @_('ID "[" NUMBER "]"')
    def expr(self, p):
        try:
            return 'index', p.ID, p.NUMBER
        except TypeError:
            print("Error variable is not a list")

    @_('ID "[" ID "]"')
    def expr(self, p):
        try:
            return 'index_ID', p.ID0, p.ID1
        except TypeError:
            print("Error variable is not a list")

    @_('ID "." SIZE "("  ")" ')
    def expr(self, p):
        try:
            return "size", p.ID
        except TypeError:
            print("Error variable is not a list")

    @_('ID "." REMOVE "(" NUMBER ")"')
    def expr(self, p):
        try:
            return "delete", p.ID, p.NUMBER
        except TypeError:
            print("Error variable is not a list")

    @_('ID "." ADD "(" expr ")"')
    def expr(self, p):
        try:
            return "lst_add", p.ID, p.expr
        except TypeError:
            print("Error variable is not a list")

    @_('ID "[" NUMBER "]" "=" expr')
    def expr(self, p):
        try:
            return "index_change", p.ID, p.NUMBER, p.expr
        except TypeError:
            print("Error variable is not a list")

    @_('ID "." SORT "("  ")"')
    def expr(self, p):
        try:
            return "sort", p.ID
        except TypeError:
            print("Error variable is not a list")

    # Vectors =====================================================================================================
    @_('ID "=" VECTOR "(" expr COMMA expr [ COMMA expr ] ")" ')
    def var_assign(self, p):
        if p.expr2 is None:
            v = vector(p.expr0[1], p.expr1[1], 0)
        else:
            v = vector(p.expr0[1], p.expr1[1], p.expr2[1])
        return "var_assign", p.ID, v

    @_('ID "." XCOMP "(" ")" ')
    def expr(self, p):
        return 'xcomp', p.ID

    @_('ID "." YCOMP "(" ")" ')
    def expr(self, p):
        return 'ycomp', p.ID

    @_('ID "." ZCOMP "(" ")" ')
    def expr(self, p):
        return 'zcomp', p.ID

    @_('ID "." MAGNITUDE "(" ")" ')
    def expr(self, p):
        return 'magnitude', p.ID

    @_('ID "." DOT "(" ID ")" ')
    def expr(self, p):
        return 'dot', p.ID0, p.ID1

    @_('ID "." CROSS "(" ID ")" ')
    def expr(self, p):
        return 'cross', p.ID0, p.ID1

    @_('ID "." COMPONENTS "("  ")" ')
    def expr(self, p):
        return 'components', p.ID

    # Dictionaries ==================================
    @_('ID "=" DICTIONARY "{" expr COLON expr "}" ')
    def var_assign(self, p):
        dic = {}
        dic[p.expr0] = p.expr1
        return 'var_assign', p.ID, dic

    # Shapes =================================================
    @_('ID "=" RECTANGLE "(" expr COMMA expr ")" ')
    def var_assign(self, p):
        rect = rectangle(p.expr0[1], p.expr1[1])
        return 'var_assign', p.ID, rect

    @_('ID "=" SQUARE "(" expr ")" ')
    def var_assign(self, p):
        sq = square(p.expr[1])
        return 'var_assign', p.ID, sq

    @_('ID "=" CIRCLE "(" expr ")" ')
    def var_assign(self, p):
        circ = circle(p.expr[1])
        return 'var_assign', p.ID, circ

    @_('ID "." AREA "("  ")" ')
    def expr(self, p):
        return 'area', p.ID

    @_('ID "." PERIMETER "("  ")" ')
    def expr(self, p):
        return 'perimeter', p.ID

    @_('ID "." DIAMETER "("  ")" ')
    def expr(self, p):
        return 'diameter', p.ID

    @_('ID "." CIRCUMFERENCE "("  ")" ')
    def expr(self, p):
        return 'circumference', p.ID

    @_('ID "=" TRIANGLE "(" [ expr ] COMMA [  expr ] COMMA [  expr ] COMMA [ expr ] ")" ')
    def var_assign(self, p):
        tr = triangle(p.expr0,p.expr1,p.expr2,p.expr3)
        return 'var_assign', p.ID, tr

    @_('ID "." OPPOSITE "("  ")" ')
    def expr(self, p):
        return 'opposite', p.ID

    @_('ID "." ADJACENT "("  ")" ')
    def expr(self, p):
        return 'adjacent', p.ID

    @_('ID "." HYPOTENUSE "("  ")" ')
    def expr(self, p):
        return 'hypotenuse', p.ID


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
        # if node[0] == 'fun_def':
        #     self.env[node[1]] = node[2]
        #
        # if node[0] == 'fun_call':
        #     try:
        #         return self.walkTree(self.env[node[1]])
        #     except LookupError:
        #         print("Undefined function '%s'" % node[1])
        #         return 0

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
            return self.walkTree(node[1]) == self.walkTree(node[2])
        elif node[0] == 'greater_eq':
            return self.walkTree(node[1]) >= self.walkTree(node[2])
        elif node[0] == 'less_eq':
            return self.walkTree(node[1]) <= self.walkTree(node[2])
        elif node[0] == 'greater':
            return self.walkTree(node[1]) > self.walkTree(node[2])
        elif node[0] == 'less':
            return self.walkTree(node[1]) < self.walkTree(node[2])

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


if __name__ == '__main__':
    lexer = HissuiLexer()
    parser = HissuiParser()
    env = {}
    while True:
        try:
            text = input('Hissui > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            HussuiInterpreter(tree, env)
