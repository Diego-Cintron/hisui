from Objects.vector import vector
from Objects.SHAPES2D.rectangle import rectangle
from Objects.SHAPES2D.square import square
from Objects.SHAPES2D.circle import circle
from Objects.SHAPES2D.triangle import triangle
from Objects.matrix import matrix
from HissuiClasses.HisuiLexer import HissuiLexer
from sly import Parser


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

    # Parses variables
    @_('ID')
    def expr(self, p):
        return 'id', p.ID

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

    # Function Declaration and Calling =================================================================================
    @_('FUNCTION ID "(" ")" COLON statement')
    def statement(self, p):
        return 'function_def', p.ID, p.statement

    @_('ID "(" ")"')
    def statement(self, p):
        return 'function_call', p.ID

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
    @_('ID "=" DICTIONARY "{"  expr COLON expr  { COMMA expr COLON expr } "}" ')
    def var_assign(self, p):
        dic = {p.expr0[1]: p.expr1[1]}
        lst = p.expr2
        lst2 = p.expr3
        for i in range(0, len(lst)):
            dic.update({lst[i][1]: lst2[i][1]})
        return 'var_assign', p.ID, dic

    @_('ID "." GET "(" expr ")" ')
    def expr(self, p):
        try:
            return "get", p.ID, p.expr
        except TypeError:
            print("Error variable is not a dictionary")

    @_('ID "." GKEYS "("  ")" ')
    def expr(self, p):
        try:
            return "get_keys", p.ID
        except TypeError:
            print("Error variable is not a dictionary")

    @_('ID "." GVALUES "("  ")" ')
    def expr(self, p):
        try:
            return "get_values", p.ID
        except TypeError:
            print("Error variable is not a dictionary")

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
        tr = triangle(p.expr0, p.expr1, p.expr2, p.expr3)
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

    # Matrix ==================================================================================
    @_('ID "=" MATRIX "(" "[" expr { COMMA expr } "]" COMMA "[" expr { COMMA expr } "]" COMMA "[" expr { COMMA expr } '
       '"]" ")"')
    def var_assign(self, p):
        lst = []

        row1, row2, row3 = [], [], []

        for i in range(0, len(p.expr1)):
            row1.append(p.expr1[i][1])
        row1.insert(0, p.expr0[1])
        lst.append(row1)

        for i in range(0, len(p.expr3)):
            row2.append(p.expr3[i][1])
        row2.insert(0, p.expr2[1])
        lst.append(row2)

        for i in range(0, len(p.expr5)):
            row3.append(p.expr5[i][1])
        row3.insert(0, p.expr4[1])
        lst.append(row3)

        m = matrix(lst)
        return 'var_assign', p.ID, m

    @_('ID "." PRINTMATRIX "("  ")" ')
    def expr(self, p):
        return 'printMatrix', p.ID

    @_('ID "." MADD "(" ID ")" ')
    def expr(self, p):
        return 'mADD', p.ID0, p.ID1

    @_('ID "." MSUB "(" ID ")" ')
    def expr(self, p):
        return 'mSUB', p.ID0,p.ID1

    @_('ID "." MMULT "(" ID ")" ')
    def expr(self, p):
        return 'mMult', p.ID0,p.ID1

    @_('ID "." MDIV "(" ID ")" ')
    def expr(self, p):
        return 'mDiv', p.ID0,p.ID1

    @_('ID "." MPOW "(" expr ")" ')
    def expr(self, p):
        return 'mPow', p.ID, p.expr

    @_('ID "." DETERMINANT "("  ")" ')
    def expr(self, p):
        return 'determinant', p.ID

