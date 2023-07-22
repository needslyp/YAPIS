import sys
import antlr4.error.ErrorListener
from antlr4 import *
from new_gen.fileLexer import fileLexer
from new_gen.fileParser import fileParser
from new_gen.fileListener import fileListener
from new_gen.myFileVisitor import MyFileVisitor

class MyErrorListener(antlr4.error.ErrorListener.ErrorListener):
    def __init__(self, text):
        self.text = str(text)

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        code_lines = self.text.split('\n')

        for i in range(len(code_lines)):
            if (i == line - 1):
                print(''.join('-' for _ in range(80)))
                print(code_lines[i-1])
                print(code_lines[i])
                print(''.join(' ' for _ in range(column-1)) + '^')
                print(f'Error occured! Details: "{msg}" at line {line} column {column}')


def main(argv):

    input_stream = FileStream(argv[1])
    lexer = fileLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = fileParser(stream)

    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener(input_stream))

    tree = parser.program()
    printer = fileListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    visitor = MyFileVisitor()
    output = visitor.visitProgram(tree)
    visitor.printOutput()
    visitor.writeToFile()

if __name__ == '__main__':
    main(sys.argv)
