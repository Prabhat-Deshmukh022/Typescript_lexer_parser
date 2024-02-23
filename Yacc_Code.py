import ply.yacc as yacc
# Get the token map from the lexer
from Lexer_Code import tokens
# Grammar rules
def p_statement(p):
    '''statement : function_call
    | return_statement
    | throw_statement
    | try_catch_statement'''
    p[0] = p[1]

def p_function_call(p):
    'function_call : FUNCTION ID LPAREN params RPAREN SEMICOLON'
    p[0] = ('function_call', p[1], p[3])

def p_params(p):
    '''params : param
    | params COMMA param'''
    if len(p) > 2:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_param(p):
    'param : ID COLON ID'
    p[0] = ('param', p[1])

def p_return_statement(p):
    'return_statement : RETURN ID DIV ID'
    p[0] = ('return_statement', p[2])

def p_throw_statement(p):
    'throw_statement : THROW NEW ERROR LPAREN quote NUMBER quote RPAREN SEMICOLON'
    p[0] = ('throw_statement', p[5])

def p_quote(p):
    '''quote : QUOTE'''
    p[0] = ('quote', p[1])

def p_try_catch_statement(p):
    '''try_catch_statement : TRY LBRACE try_block catch_block RBRACE'''
    p[0] = ('try_catch_statement', p[3], p[4])

def p_try_block(p):
    'try_block : block'
    p[0] = ('try_block', p[1])
        
def p_catch_block(p):
    'catch_block : CATCH LPAREN ID RPAREN LBRACE block RBRACE'
    p[0] = ('catch_block', p[3], p[6])
    
def p_block(p):
    '''block : statement
    | if_statement
    | return_divide
    | block statement'''
    if len(p) > 2:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_if_statement(p):
    'if_statement : IF LPAREN ID TRIP_EQ NUMBER RPAREN LBRACE THROW NEW ERROR LPAREN QUOTE STRING QUOTE RPAREN SEMICOLON'
    p[0] = ('if_statement', p[3], p[5], p[14])

def p_return_divide(p):
    'return_divide : RETURN NUMBER DIV NUMBER'
    p[0] = ('return_divide', p[2], p[4])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!", p)

def p_for_loop(p):
    '''for_loop : FOR LPAREN declaration SEMICOLON expression SEMICOLON increment
    RPAREN LBRACE statements RBRACE'''
    print("For Loop")

def p_declaration(p):
    'declaration : LET ID EQ NUMBER'
    print("Declaration:", p[2])

def p_expression(p):
    'expression : ID LEQ NUMBER'
    print("Expression:", p[1], p[2], p[3])

def p_increment(p):
    '''increment : ID PLUS PLUS'''
    print("Increment:", p[1])

def p_statements(p):
    '''statements : statements statement
    | statement'''

def p_statement(p):
    '''statement : CONSOLE PERIOD LOG LPAREN ID RPAREN SEMICOLON'''
    print("Statement:", p[1])

# Define the grammar rules using Yacc syntax
def p_function_declaration(p):
    '''function_declaration : FUNCTION ID LPAREN parameter_list RPAREN COLON
    data_type LBRACE statements RBRACE'''

# Define actions here or return the parsed structure
def p_parameter_list(p):
    '''parameter_list : ID COLON data_type
    | ID COLON data_type COMMA parameter_list'''

# Define actions here or return the parsed structure
def p_data_type(p):
    '''data_type : ID
    | NUMBER
    | data_type PERIOD ID''' # For handling nested types like
    'number.string'

# Define actions here or return the parsed structure
def p_statements(p):
    '''statements : statement
    | statement statements'''

# Define actions here or return the parsed structure
def p_statement(p):
    '''statement : RETURN expression SEMICOLON
    | ID COLON data_type SEMICOLON
    | function_declaration
    | assignment_statement
    | arithmetic_expression SEMICOLON'''

# Define actions here or return the parsed structure
def p_assignment_statement(p):
    '''assignment_statement : ID EQ expression SEMICOLON'''

# Define actions here or return the parsed structure
def p_expression(p):
    '''expression : ID
    | NUMBER
    | arithmetic_expression'''

# Define actions here or return the parsed structure
def p_arithmetic_expression(p):
    '''arithmetic_expression : expression PLUS expression
    | expression MINUS expression
    | expression STAR expression
    | expression DIV expression
    | LPAREN arithmetic_expression RPAREN'''

    # Define actions here or return the parsed structure
def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN statement
    | IF LPAREN expression RPAREN statement elif_statements'''

def p_elif_statements(p):
    '''elif_statements : ELSE_IF LPAREN expression RPAREN statement
    | ELSE_IF LPAREN expression RPAREN statement
    elif_statements
    | ELSE statement'''

def p_statement(p):
    '''statement : LBRACE STATEMENT
    | statements'''

def p_statements(p):
    '''statements : IDENTIFIERs SEMICOLON
    | IDENTIFIER DUB_EQ SEMICOLON
    | IDENTIFIER DUB_MIN SEMICOLON
    | IDENTIFIER PLUS PLUS
    | IDENTIFIER EQ expression SEMICOLON'''

def p_STATEMENT(p):
    '''STATEMENT : IDENTIFIER SEMICOLON STATEMENT
    | IDENTIFIER DUB_EQ SEMICOLON STATEMENT
    | IDENTIFIER DUB_MIN SEMICOLON STATEMENT
    | IDENTIFIER EQ assignment SEMICOLON STATEMENT
    | RBRACE'''

def p_assignment(p):
    '''assignment : assignment PLUS assignment
    | assignment MINUS assignment
    | assignment STAR assignment
    | assignment DIV assignment
    | NUMBER
    | IDENTIFIER'''

def p_IDENTIFIERs(p):
    '''IDENTIFIERs : IDENTIFIER IDENTIFIERs
    | IDENTIFIER '''

def p_expression(p):
    '''expression : EXCLAIM expression
    | IDENTIFIER DUB_EQ IDENTIFIER
    | IDENTIFIER DUB_EQ NUMBER
    | IDENTIFIER GEQ IDENTIFIER
    | IDENTIFIER GEQ NUMBER
    | IDENTIFIER LEQ IDENTIFIER
    | IDENTIFIER LEQ NUMBER
    | IDENTIFIER GREATER IDENTIFIER
    | IDENTIFIER GREATER NUMBER
    | IDENTIFIER LESSER IDENTIFIER
    | IDENTIFIER LESSER NUMBER
    | IDENTIFIER EXCLAIM EQ IDENTIFIER
    | IDENTIFIER EXCLAIM EQ NUMBER
    | NUMBER
    | IDENTIFIER'''

def p_array_statement(p):
    '''
    array_statement : LET IDENTIFIER EQ LSQUARE nums RSQUARE SEMICOLON
    | LET IDENTIFIER COLON IDENTIFIER LSQUARE RSQUARE EQ LSQUARE nums RSQUARE
    SEMICOLON
    '''
    p[0] = 'Valid TypeScript array declaration statement'

def p_nums(p):
    '''
    nums : NUMBER
    | nums COMMA nums
    '''
    pass

# Build the parser
parser = yacc.yacc()
# Example TypeScript code
typescript_code = '''
let numbers: number[] = [1, 2, 3, 4, 5]; // Initializing the 'numbers' array with
values
'''
result = parser.parse(typescript_code)
print(result)