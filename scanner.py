# Author: Victor Nazario Morales (843-15-4984)
# Scanner implementation for the PySocket Language

import ply
tokens = (
     'NAME', 'NUMBER',
     'ELSE', 'IF', 'AND', 'OR', 'EQUALS',
     'LPAREN', 'RPAREN',
    )

# Reserved keywords for the language

reserved_keywords = {
    'if': 'IF',
    'else': 'ELSE',
}

# Tokens

t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ELSE = r'\else'
t_IF = r'\if'
t_AND = r'\&'
t_OR = r'\|'
t_EQUALS = r'\='
t_LPAREN = r'\('
t_RPAREN = r'\)'
