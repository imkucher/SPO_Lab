import sys


class Lexer:
    NUMBER, ID, WHILE, DO, FOR, IF, ELSE, LB, RB, LBR, RBR, PLUS, MINUS, LESS, MORE, EQUAL, SCOL, READ, PRINT, \
    LLADD, LLREMOVE, LLGET, LLPRINT, HADD, HCONTAINS, HREMOVE, HPRINT, EOF = range(28)

    # Специальные символы языка
    SYMBOLS = {
           '{': LB,
           '}': RB,
           '=': EQUAL,
           ';': SCOL,
           '(': LBR,
           ')': RBR,
           '+': PLUS,
           '-': MINUS,
           '<': LESS,
           '>': MORE
           }

    # Ключевые слова
    WORDS = {
           'do': DO,
           'if': IF,
           'else': ELSE,
           'while': WHILE,
           'for': FOR,
           'read': READ,
           'print': PRINT,
           'addtoll': LLADD,
           'removefromll': LLREMOVE,
           'getfromll': LLGET,
           'printll': LLPRINT
           }

    ch = ' ' # текущий символ, считанный из исходника - пробел
    i = 0

    # Конструктор
    def __init__(self, source):
        self.source = source

    # Вывод ошибки и выход по ней
    def error(self, msg):
        print('Lexer error: ', msg)
        sys.exit(1)

    def getc(self):
        if len(self.source) > self.i:
            self.ch = self.source[self.i]
            self.i += 1
        else:
            self.ch = ''

    # Получаем следующий токен
    def next_token(self):
        self.value = None # Значение токена
        self.symbol = None # Атрибут токена
        while self.symbol == None:
            if len(self.ch) == 0:
                self.symbol = Lexer.EOF
            elif self.ch.isspace():
                self.getc()
            elif self.ch in Lexer.SYMBOLS:
                self.symbol = Lexer.SYMBOLS[self.ch]
                self.getc()
            elif self.ch.isdigit():
                intval = 0
                while self.ch.isdigit():
                    intval = intval * 10 + int(self.ch)
                    self.getc()
                self.value = intval
                self.symbol = Lexer.NUMBER
            elif self.ch.isalpha():
                ident = ''
                while self.ch.isalpha():
                    ident = ident + self.ch.lower()
                    self.getc()
                if ident in Lexer.WORDS:
                    self.symbol = Lexer.WORDS[ident]
                elif len(ident) == 1:
                    self.symbol = Lexer.ID
                    self.value = ord(ident) - ord('a')
                else:
                    self.error('Unknown identifier: ' + ident)
            else:
                self.error('Unexpected symbol: ' + self.ch)