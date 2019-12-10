from http.server import HTTPServer
import ply.yacc as yacc
import scanner

# COMMANDS
# specify posible commands

ids = {}
class parser(object):
    tokens = scanner.tokens

    # assignment statement: <statement> -> ID = <expression>
    def p_statement_assign(p):
        'statement : ID EQUALS expression'
        ids[p[1]] = p[3]

    # expression statement: <statement> -> <expression>
    def p_statement_expr(p):
        'statement : expression'
        print(p[1])

    # parenthesis group expression: <expression> -> ( <expression> )
    def p_expression_group(p):
        'expression : LPAREN expression RPAREN'
        p[0] = p[2]

    # number literal expression: <expression> -> NUMBER
    def p_expression_number(p):
        'expression : NUMBER'
        p[0] = p[1]

    # variable id literal expression: <expression> -> ID
    def p_expression_id(p):
        'expression : ID'
        p[0] = p[1]
        if p[1] == "local_server":
            #httpd = HTTPServer(('localhost', 8080), Server)
            #httpd.handle_request()
           print("Server connected successfully!")
        elif p[1] == "external_server":
            #connect to external server
            print("Server connected successfully!")
        else:
        # attempt to lookup variable in current dictionary, throw error if not found
            try:
                return ids[p[1]]
            except LookupError:
                p[0] = 0
                print("Undefined id '%s'" % p[1])

    # boolean
    # def p_boolean(p):
    #     ''' boolean : TRUE
    #                 | FALSE
    #     '''
    #     p[0] = p[1]

    ##Add empty expression

    # handle parsing errors
    def p_error(p):
        print("Syntax error at '%s'" % p.value)

    if __name__ == '__main__':
        parser = yacc.yacc()

        while True:
            try:
                text = input('SocketLang ~ ')
            except EOFError:
                break
            if text == "exit":
                print("User has exited")
                break
            if text:
                parser.parse(text)