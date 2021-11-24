from sly import Lexer
# Sly required, to install sly type: pip3 install sly on the terminal.

# For Language syntax,methods and creation please read "Documentation.txt"

# Hisui Lexer Class, This class takes the input from the user and then divides it into tokens for the parser to then
# use.
class HisuiLexer(Lexer):

    # Parser Token List.
    tokens = {ID, NUMBER, STRING, EQUAL, COLON,
              # statement tokens
              IF, THEN, ELSE, FOR, TO, WHILE,

              # Comparison tokens
              GREATEREQ, LESSEQ, COMMA,

              # Vectors Tokens
              VECTOR, DOT, CROSS, XCOMP, YCOMP, ZCOMP, MAGNITUDE, COMPONENTS,

              # Dictionary Tokens
              DICTIONARY, GVALUES, GKEYS, GET,

              # Matrix Tokens
              MATRIX, PRINTMATRIX, MADD, MSUB, MMULT, MDIV, MPOW, DETERMINANT,

              # Shapes Tokens
              RECTANGLE, SQUARE, AREA, PERIMETER, CIRCLE, DIAMETER, CIRCUMFERENCE,
              TRIANGLE, OPPOSITE, ADJACENT, HYPOTENUSE,

              # List Tokens
              LIST, SIZE, REMOVE, ADD, SORT,

              # Function Tokens
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
    literals = {'+', '-', '/', '*', '^', '=', '(', ')', '<', '>', '%', '[', ']', '.', "{", "}"}

    # establishing function characters
    GREATEREQ = r'>='
    LESSEQ = r'<='
    EQUAL = r'=='
    COMMA = r','
    COLON = r':'

    # Statements token remap
    ID['if'] = IF
    ID['then'] = THEN
    ID["else"] = ELSE
    ID['list'] = LIST
    ID['for'] = FOR
    ID['to'] = TO
    ID['while'] = WHILE

    # List token remap
    ID['list'] = LIST
    ID['size'] = SIZE
    ID['remove'] = REMOVE
    ID['add'] = ADD
    ID['sort'] = SORT

    # Vector token remap
    ID['vector'] = VECTOR
    ID['cross'] = CROSS
    ID['dot'] = DOT
    ID['xc'] = XCOMP
    ID['yc'] = YCOMP
    ID['zc'] = ZCOMP
    ID['magnitude'] = MAGNITUDE

    #Dictionary token remap
    ID['dictionary'] = DICTIONARY
    ID['get'] = GET
    ID['gValues'] = GVALUES
    ID['gKeys'] = GKEYS

    # Matrix token remap
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
