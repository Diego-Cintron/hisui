from sly import Lexer
from sly import Parser


# Creating a Lexer who inherits from sly's lexer.oy class
class HissuiLexer(Lexer):
    # Inputting the tokens that the parser will be able to use.
    # Temporarily REMOVED TOKENS:
    #   SQUARE, CIRCLE, RECTANGLE, TRIANGLE, VECTOR, MATRIX, NEW, FOR,
    #   ELSEIF, IN, COMMA, COLON, RETURN,
    # Tokens that were transferred to "literals": ASSIGN, RP, LP, RB, LB
    tokens = {ID, NUMBER, STRING, EQUAL, IF, THEN, ELSE}

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
    literals = {'+', '-', '/', '*', '^', '=', '(', ')'}

    # establishing function characters
    EQUAL = r'=='
    # COMMA = r','
    # COLON = r':'

    # implementing standard language clauses.
    ID['if'] = IF
    ID['then'] = THEN
    ID["else"] = ELSE
    # ID['elif'] = ELSEIF
    # ID['for'] = FOR
    # ID['in'] = IN
    # ID['return'] = RETURN

    # Adding different functional objects
    # ID['square'] = SQUARE
    # ID["rectangle"] = RECTANGLE
    # ID['triangle'] = TRIANGLE
    # ID['circle'] = CIRCLE
    # ID['matrix'] = MATRIX
    # ID['vector'] = VECTOR

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
        ('left', '*', '/','^',EQUAL),
        ('right', 'UMINUS'),
    )

    # Creates collection of variables
    def __init__(self):
        self.ids = {}

    # Ignores empty user inputs
    @_('')
    def statement(self, p):
        pass

    # Assigns expression to a variable
    @_('ID "=" expr')
    def statement(self, p):
        self.ids[p.ID] = p.expr

    # Assigns string value to a variable
    @_('ID "=" STRING')
    def statement(self, p):
        self.ids[p.ID] = p.STRING

    # Prints out expression once it no longer has any operations left
    @_('expr')
    def statement(self, p):
        print(p.expr)

    # Does addition
    @_('expr "+" expr')
    def expr(self, p):
        return p.expr0 + p.expr1

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

    # Parses variables
    @_('ID')
    def expr(self, p):
        try:
            return self.ids[p.ID]
        except LookupError:
            print("Undefined id '%s'" % p.ID)
            return 0

    @_('expr EQUAL expr')
    def expr(self, p):
        return p.expr0==p.expr1

    @_('expr EQUAL expr')
    def condition(self, p):
        return p.expr0 == p.expr1

    @_('IF condition THEN statement ELSE statement')
    def statement(self, p):
        if p.condition:
            return p.statement0
        else:
            return p.condition1

    # @_('FOR ID TO expr THEN statement')
    # def statement(self, ):
    #     return 'for_loop', ('for_loop_setup', p.ID, p.expr), p.statement


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
