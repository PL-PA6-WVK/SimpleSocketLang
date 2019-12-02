# Author: Victor Nazario Morales (843-15-4984)
# Scanner implementation for the PySocket Language

import ply

tokens = (
    'ID', 'NUMBER',
    'ELSE', 'IF', 'AND', 'OR', 'EQUALS',
    'LPAREN', 'RPAREN', 'COMMA', 'SEMICOLON',
    'DOT', 'LT', 'LTE', 'GT', 'GTE',
)

# Reserved keywords for the language

reserved_keywords = {
    'if': 'IF',
    'else': 'ELSE',
}

# Tokens
t_ignore = '\t'
t_NUMBER = '\d+'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ELSE = r'\else'
t_IF = r'\if'
t_AND = r'\&'
t_OR = r'\|'
t_EQUALS = r'\='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_SEMICOLON = ';'
t_DOT = '\.'
t_LT = '<'
t_LTE = '<='
t_GT = '>'
t_GTE = '>='

# This will allow for tokenizing on all relevant tokens.
tokens = tokens + tuple(reserved_keywords.values())


# This will recognize an ID for the language given the RegEx.

def t_ID(t):
    r"""[a-zA-Z_][a-zA-Z0-9_]*"""
    if t.value.upper() in reserved_keywords:
        t.value = t.value.upper()
        t.type = t.value
    return t


# Identifies a comment
# A comment is defined as a symbol
# followed by any combination of alphanumeric characters
def t_COMMENT(t):
    r"""\#.*"""
    pass  # as soon as a comment is detected, it's obviated by the system.

# Will tokenize a sequence identified by the RegEx as a number

def t_NUMBER(t):
    r"""\d+"""
    t.value = int(t.value)
    return t

# Function to output when an error has been found in the tokenizing progress


def t_ERROR(t):
    print("The character is illegal '%s'" % t.value[0])
    t.lexer.skip(1)
