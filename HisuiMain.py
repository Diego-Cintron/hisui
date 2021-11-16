from HissuiClasses.HisuiLexer import HissuiLexer
from HissuiClasses.HisuiParser import HissuiParser
from HissuiClasses.HisuiInterpreter import HussuiInterpreter

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
