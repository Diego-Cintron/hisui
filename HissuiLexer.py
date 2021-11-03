from sly import Lexer

class HissuiLexer(Lexer):
    tokens = {ID, NUMBER,EQUAL,ASSIGN, FOR, IF,ELSE,ELSEIF, IN,SQUARE
        , CIRCLE, RECTANGLE, TRIANGLE, VECTOR,MATRIX,NEW,RP,LP,RB,LB,COMMA,COLON,RETURN}

    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    ignore = ' \t'

    NUMBER = r'\d+'
    def NUMBER(self,t):
        t.value = int(t.value)
        return t

    literals = {'+','-','/','*','^'}

    EQUAL = r'=='
    ASSIGN = r'='

    COMMA = r','
    COLON = r':'

    LP = r'\('
    RP = r'\)'
    LB = r'\['
    RB = r'\]'


    ID['if']=IF
    ID["else"] = ELSE
    ID['elif'] = ELSEIF
    ID['for'] = FOR
    ID['in'] = IN
    ID['return'] = RETURN

    ID['square'] = SQUARE
    ID["rectangle"] = RECTANGLE
    ID['triangle'] = TRIANGLE
    ID['circle'] = CIRCLE

    ID['matrix'] = MATRIX
    ID['vector'] = VECTOR

    ID['new'] = NEW

if __name__ == '__main__':
    data = "circle c = new circle(2)" \
           "circle j = new circle(4)" \
           "if(c == j) return true"
    lexer = HissuiLexer()
    for tok in lexer.tokenize(data):
        print(tok)
