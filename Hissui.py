from sly import Lexer
from sly import Parser


# Creating a Lexer who inherits from sly's lexer.oy class
class HissuiLexer(Lexer):
    # Inputting the tokens that the parser will be able to use.
    # Temporarily REMOVED TOKENS:
    #   SQUARE, CIRCLE, RECTANGLE, TRIANGLE, VECTOR, MATRIX, NEW, FOR,
    #   ELSEIF, IN, COMMA, COLON, RETURN,
    # Tokens that were transferred to "literals": ASSIGN, RP, LP, RB, LB
    tokens = {ID, NUMBER, STRING, EQUAL,
              # statement tokens
              IF, THEN, ELSE,
              # Comparison tokens
              GREATEREQ, LESSEQ,

              # Shape Tokens
              SQUARE, RECTANGLE, TRIANGLE, CIRCLE,

              # Extra Structure Tokens
              MATRIX, VECTOR,
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

    # Defining strings
    STRING = r'\".*?\"'

    # stating the operators
    literals = {'+', '-', '/', '*', '^', '=', '(', ')', '<', '>', '%', '[', ']', '.'}

    # establishing function characters
    GREATEREQ = r'>='
    LESSEQ = r'<='
    EQUAL = r'=='
    # COLON = r':'

    # implementing standard language clauses.
    ID['if'] = IF
    ID['then'] = THEN
    ID["else"] = ELSE
    ID['list'] = LIST
    # ID['for'] = FOR
    # ID['to'] = TO

    # List methods
    ID['list'] = LIST
    ID['size'] = SIZE
    ID['remove'] = REMOVE
    ID['add'] = ADD
    ID['sort'] = SORT

    # Adding different functional objects
    ID['square'] = SQUARE
    ID["rectangle"] = RECTANGLE
    ID['triangle'] = TRIANGLE
    ID['circle'] = CIRCLE
    ID['matrix'] = MATRIX
    ID['vector'] = VECTOR

    # new token for object creation
    # ID['new'] = NEW

    # error handling
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

    # Creates collection of variables
    def __init__(self):
        self.ids = {}

    # Ignores empty user inputs
    @_('')
    def statement(self, p):
        pass

    # Variable Declaration ====================================================================
    # Assigns expression to a variable
    @_('ID "=" expr')
    def statement(self, p):
        self.ids[p.ID] = p.expr
        return p.ID, p.expr

    @_('ID "=" RECTANGLE')
    def statement(self, p):
        self.ids[p.ID] = p.RECTANGLE
        return p.ID, p.RECTANGLE

    @_('ID "=" SQUARE')
    def statement(self, p):
        self.ids[p.ID] = p.SQUARE
        return p.ID, p.SQUARE

    @_('ID "=" CIRCLE')
    def statement(self, p):
        self.ids[p.ID] = p.CIRCLE
        return p.ID, p.CIRCLE

    @_('ID "=" TRIANGLE')
    def statement(self, p):
        self.ids[p.ID] = p.TRIANGLE
        return p.ID, p.TRIANGLE

    @_('ID "=" MATRIX')
    def statement(self, p):
        self.ids[p.ID] = p.MATRIX
        return p.ID, p.MATRIX

    @_('ID "=" VECTOR')
    def statement(self, p):
        self.ids[p.ID] = p.VECTOR
        return p.ID, p.VECTOR

    # Prints out expression once it no longer has any operations left
    @_('expr')
    def statement(self, p):
        print(p.expr)

    # Expression Handling =======================================================================================
    # Does addition
    @_('expr "+" expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    # Does addition
    @_('expr "%" expr')
    def expr(self, p):
        return p.expr0 % p.expr1

    # Does subtraction
    @_('expr "-" expr')
    def expr(self, p):
        return p.expr0 - p.expr1

    # Does multiplication
    @_('expr "*" expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    # Does division
    @_('expr "/" expr')
    def expr(self, p):
        return p.expr0 / p.expr1

    @_('expr "<" expr')
    def expr(self, p):
        return p.expr0 < p.expr1

    @_('expr ">" expr')
    def expr(self, p):
        return p.expr0 > p.expr1

    # Does exponent
    @_('expr "^" expr')
    def expr(self, p):
        return p.expr0 ** p.expr1

    # Parses individual negative numbers
    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return -p.expr

    # Parses expressions inside parenthesis
    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    # Parses numbers
    @_('NUMBER')
    def expr(self, p):
        return p.NUMBER

    # Parses numbers
    @_('STRING')
    def expr(self, p):
        return p.STRING

    # Parses variables
    @_('ID')
    def expr(self, p):
        try:
            return self.ids[p.ID]
        except LookupError:
            print("Undefined id '%s'" % p.ID)
            return 0

    @_('expr GREATEREQ expr')
    def expr(self, p):
        return p.expr0 >= p.expr1

    @_('expr LESSEQ expr')
    def expr(self, p):
        return p.expr0 <= p.expr1

    @_('expr EQUAL expr')
    def expr(self, p):
        return p.expr0 == p.expr1

    # Condition Handling ====================================================================
    @_('expr GREATEREQ expr')
    def condition(self, p):
        return p.expr0 >= p.expr1

    @_('expr LESSEQ expr')
    def condition(self, p):
        return p.expr0 <= p.expr1

    @_('expr "<" expr')
    def condition(self, p):
        return p.expr0 < p.expr1

    @_('expr ">" expr')
    def condition(self, p):
        return p.expr0 > p.expr1

    @_('expr EQUAL expr')
    def condition(self, p):
        return p.expr0 == p.expr1

    @_('NUMBER')
    def condition(self, p):
        return p.NUMBER

    # If statements =====================================================================================

    @_('IF condition THEN statement ELSE statement')
    def statement(self, p):
        if p.condition:
            print(p.statement0[0])
            self.ids[p.statement0[0]] = p.statement0[1]
            return p.statement0[1]
        else:
            self.ids[p.statement1[0]] = p.statement1[1]
            return p.statement1[1]

    @_('IF condition THEN expr ELSE expr')
    def statement(self, p):
        if p.condition:
            print(p.expr0)
            return p.expr0
        else:
            print(p.expr1)

            return p.expr1

    # Lists===========================================================================================

    @_('ID "=" LIST "[" "]"')
    def statement(self, p):
        try:
            inp = input("Enter List Elements: ")
            if inp != "":
                lst = list(map(int, inp.split(",")))
            else:
                lst = []
            self.ids[p.ID] = lst
            return p.ID, lst
        except TypeError:
            print("Error variable is not a list")

    @_('ID "[" NUMBER "]"')
    def expr(self, p):
        try:
            index = self.ids[p.ID][p.NUMBER]
            return index
        except TypeError:
            print("Error variable is not a list")

    @_('ID "." SIZE "("  ")" ')
    def expr(self, p):
        try:
            size = len(self.ids[p.ID])
            return size
        except TypeError:
            print("Error variable is not a list")

    @_('ID "." REMOVE "(" NUMBER ")"')
    def expr(self, p):
        try:
            del self.ids[p.ID][p.NUMBER]
            return self.ids[p.ID]
        except TypeError:
            print("Error variable is not a list")

    @_('ID "." ADD "(" expr ")"')
    def expr(self, p):
        try:
            self.ids[p.ID].append(p.expr)
            return self.ids[p.ID]
        except TypeError:
            print("Error variable is not a list")

    @_('ID "[" NUMBER "]" "=" expr')
    def expr(self, p):
        try:
            self.ids[p.ID][p.NUMBER] = p.expr
            return self.ids[p.ID]
        except TypeError:
            print("Error variable is not a list")

    @_('ID "." SORT "("  ")"')
    def expr(self, p):
        try:
            self.ids[p.ID].sort()
            return self.ids[p.ID]
        except TypeError:
            print("Error variable is not a list")


if __name__ == '__main__':
    lexer = HissuiLexer()
    parser = HissuiParser()
    while True:
        try:
            text = input('Hissui > ')
        except EOFError:
            break
        if text:
            parser.parse(lexer.tokenize(text))
