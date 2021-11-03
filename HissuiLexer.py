from sly import Lexer


# Creating a Lexer who inherits from sly's lexer.oy class
class HissuiLexer(Lexer):
    # Inputting the tokens that the parser will be able to use.
    tokens = {ID, NUMBER, EQUAL, ASSIGN, FOR, IF, ELSE, ELSEIF, IN, SQUARE
        , CIRCLE, RECTANGLE, TRIANGLE, VECTOR, MATRIX, NEW, RP, LP, RB, LB, COMMA, COLON, RETURN}

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

    # stating the operators
    literals = {'+', '-', '/', '*', '^'}

    # establishing function characters
    EQUAL = r'=='
    ASSIGN = r'='
    COMMA = r','
    COLON = r':'

    # adding parenthesis and bracket recognition
    LP = r'\('
    RP = r'\)'
    LB = r'\['
    RB = r'\]'

    # implementing standard language clauses.
    ID['if'] = IF
    ID["else"] = ELSE
    ID['elif'] = ELSEIF
    ID['for'] = FOR
    ID['in'] = IN
    ID['return'] = RETURN

    # Adding different functional objects
    ID['square'] = SQUARE
    ID["rectangle"] = RECTANGLE
    ID['triangle'] = TRIANGLE
    ID['circle'] = CIRCLE
    ID['matrix'] = MATRIX
    ID['vector'] = VECTOR

    # new token for object creation
    ID['new'] = NEW

    # error handling
    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1


if __name__ == '__main__':
    lexer = HissuiLexer()
    while True:
        inp = input("Hissui> ")
        if inp:
            for tok in lexer.tokenize(inp):
                print("Type: %r Value: %r" % (tok.type, tok.value))
        else:
            break
