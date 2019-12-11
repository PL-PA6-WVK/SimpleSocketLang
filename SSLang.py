import ply.yacc as yacc
import scanner
import server
import sockets

# COMMANDS (on terminal)
# fact_server: creates random facts giving local server
# fact_client: creates random facts receiving client server
# host_server: creates a external host to our SSLang's web page
# chat_server: creates a server side of a chat room
# chat_client: creates a client side of a chat room
# exit: to exit SSLang

# Dictionay of IDs
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
        if p[1] == "fact_server":
            print("Server connected successfully!")
            print("A random fact has been sent!")
            server.local_server()
        elif p[1] == "fact_client":
            sockets.fact_client()
        elif p[1] == "host_server":
            print("Server connected successfully!")
            print("'localhost:8000' is open, enter that address in browser.")
            server.local_site()
        elif p[1] == "chat_server":
            sockets.server_chat()
        elif p[1] == "chat_client":
            sockets.client_chat()
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
                text = input('SSLang ~ ')
            except EOFError:
                break
            if text == "exit":
                print("SSLang has been closed")
                break
            if text:
                parser.parse(text)