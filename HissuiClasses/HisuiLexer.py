from sly import Lexer


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
              DICTIONARY,GVALUES,GKEYS,GET,

              # Matrix
              MATRIX, PRINTMATRIX, MADD, MSUB, MMULT, MDIV, MPOW,DETERMINANT,

              # Shapes
              RECTANGLE, SQUARE, AREA, PERIMETER, CIRCLE, DIAMETER, CIRCUMFERENCE,
              TRIANGLE, OPPOSITE, ADJACENT, HYPOTENUSE,

              # List Tokens
              LIST, SIZE, REMOVE, ADD, SORT,

              #Function token
              FUNCTION,
              }

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
    literals = {'+', '-', '/', '*', '^', '=', '(', ')', '<', '>', '%', '[', ']', '.',"{","}"}

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
    ID['get'] = GET
    ID['gValues'] = GVALUES
    ID['gKeys'] = GKEYS

    # Matrix
    ID['matrix'] = MATRIX
    ID['printMatrix'] = PRINTMATRIX
    ID['mAdd'] = MADD
    ID['mSub'] = MSUB
    ID['mMult'] = MMULT
    ID['mDiv'] = MDIV
    ID['mPow'] = MPOW
    ID['determinant'] = DETERMINANT

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

    # Function definition
    ID['function'] = FUNCTION

    # Error handling
    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
