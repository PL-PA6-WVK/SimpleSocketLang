from http.server import HTTPServer
import ply.yacc as yacc
import scanner
import server
import sockets

# COMMANDS
# specify posible commands

# Dictionay of IDS=s
ids = {}


class Parser(object):
    tokens = scanner.tokens

    # assignment statement: <statement> -> ID = <expression>
    def p_statement_assign(p):
        'statement : ID EQUALS expression'
        ids[p[1]] = p[3]

    # expression statement: <statement> -> <expression>
    def p_statement_expr(p):
        'statement : expression'
        p[0]

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
            print("Server connected successfully!")
            server.local_server()
        elif p[1] == "external_server":
            print("Server connected successfully!")
            print("'localhost:8000' is open, enter that address in browser.")
            server.local_site()
        elif p[1] == "give_a_fact":
            sockets.client()
        else:
        # attempt to lookup variable in current dictionary, throw error if not found
            try:
                return ids[p[1]]
            except LookupError:
                p[0] = 0
                print("Undefined id '%s'" % p[1])

    # handle parsing errors
    def p_error(p):
        print("Syntax error at '%s'" % p)

    if __name__ == '__main__':
        parser = yacc.yacc()

        while True:
            try:
                text = input('SocketLang ~ ')
            except EOFError:
                break
            if text == "exit":
                print("user has exited")
                break
            if text:
                parser.parse(text)