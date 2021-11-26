from HisuiClasses.HisuiLexer import HisuiLexer
from HisuiClasses.HisuiParser import HisuiParser
from HisuiClasses.HisuiInterpreter import HisuiInterpreter
# Sly required, to install sly type: pip3 install sly on the terminal.

# For Language syntax,methods and creation please read "Documentation.txt"

# Hisui Main class, this class takes user input and passes it to the Lexer then the Lexer generates tokens and
# sends it to the Parser then the Parser formats it accordingly and then it's finally sent to the interpreter where
# it's executed according to the execution tree generated.
if __name__ == '__main__':
    lexer = HisuiLexer()
    parser = HisuiParser()
    env = {}
    while True:
        try:
            text = input('Hisui > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            HisuiInterpreter(tree, env)
