class Token:
    # Token constructor
    def __init__(self, tokenType, tokenValue):
        self.tokenType = tokenType
        self.tokenValue = tokenValue


class Lexer:

    # Lexer Constructor
    def __init__(self, textString):
        self.textString = textString
        self.tokenList = []

    # Generates a token based on the input string parameter in the constructor
    def generateTokens(self):

        characterList = list(self.textString)

        for i in range(0, len(characterList)):

            value = characterList[i]
            type = self.getValyeType(value)
            if type is not None:
                self.tokenList.append(Token(type, value))
            else:
                continue

    def getValyeType(self, value):

        if value.isdigit():
            return "Val"
        elif value.isalpha():
            return "ID"

        elif value in ['*', '+', '-', '^', '/']:
            return "OP"

        elif value == '(':
            return "LP"

        elif value == ')':
            return "RP"

        elif value == '[':
            return "LB"

        elif value == ']':
            return "RB"

        else:
            return None

    # Prints out tokens in an easy to see format
    def printToken(self):
        for i in range(0, len(self.tokenList)):
            token = self.tokenList[i]
            print("(" + token.tokenType + " : " + token.tokenValue+")")
        print("\n")

# Test code
input = "A+B"
Lex = Lexer(input)
Lex.generateTokens()
Lex.printToken()

input = "A+2*98"
Lex = Lexer(input)
Lex.generateTokens()
Lex.printToken()
