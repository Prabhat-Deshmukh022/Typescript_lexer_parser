from ply import lex

# Tokens for the first set of rules
reserved = {
'for': 'FOR',
'var': 'VAR',
'let': 'LET',
'const': 'CONST',
'id': 'ID',
'try': 'TRY',
'catch': 'CATCH',
'finally': 'FINALLY',
'throw': 'THROW',
'function': 'FUNCTION',
'number': 'NUMBER',
'if': 'IF',
'else': 'ELSE',
'return': 'RETURN',
'Error': 'ERROR',
'new': 'NEW',
'quote': 'QUOTE',
'else if' : 'ELSE_IF',
'console' : 'CONSOLE',
'log' : 'LOG'
}

tokens = [
'IDENTIFIER',
'LPAREN',
'RPAREN',
'LBRACE',
'RBRACE',
'SEMICOLON',
'OPERATOR',
'NUMBER',
'PERIOD',
'PLUS',
'MINUS',
'STAR',
'DIV',
'EQ',
'DUB_EQ',
'GREATER',
'LESSER',
'GEQ',
'LEQ',
'COMMA',
'COLON',
'TRIP_EQ',
'QUOTE',
'STRING',
'LET',
'LSQUARE',
'RSQUARE',
'DOLLAR',
'EXCLAIM',
'TILD',
'DUB_MIN'
] + list(reserved.values())

# Regular expression rules for simple tokens
t_SEMICOLON = r';'
t_PERIOD = r'\.'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_STAR = r'\*'
t_DIV = r'/'
t_EQ = r'='
t_DUB_EQ = r'=='
t_GREATER = r'>'
t_LESSER = r'<'
t_GEQ = r'>='
t_LEQ = r'<='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_COLON = r':'
t_TRIP_EQ = r'==='
t_QUOTE = r'"'
t_STRING = r'(\'[^\']\'|\"[^\"]\")'
t_OPERATOR = r'[>\-]'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_DOLLAR = r'\$'
t_EXCLAIM = r'\!'
t_TILD = r'\`'
t_DUB_MIN = r'--'

# A regular expression rule for identifying an identifier
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# A regular expression rule for identifying a number
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# A string containing ignored characters (spaces, tabs, and newlines)
t_ignore_comment = r'\#'
t_ignore = ' \t\n'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()