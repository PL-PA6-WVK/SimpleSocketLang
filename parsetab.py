
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND COMMA DOT ELSE EQUALS GT GTE ID IF LPAREN LT LTE NUMBER OR RPAREN SEMICOLONstatement : ID EQUALS expressionstatement : expressionexpression : LPAREN expression RPARENexpression : NUMBERexpression : ID'
    
_lr_action_items = {'ID':([0,4,6,],[2,8,8,]),'LPAREN':([0,4,6,],[4,4,4,]),'NUMBER':([0,4,6,],[5,5,5,]),'$end':([1,2,3,5,8,9,10,],[0,-5,-2,-4,-5,-1,-3,]),'EQUALS':([2,],[6,]),'RPAREN':([5,7,8,10,],[-4,10,-5,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,4,6,],[3,7,9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> ID EQUALS expression','statement',3,'p_statement_assign','parser.py',18),
  ('statement -> expression','statement',1,'p_statement_expr','parser.py',23),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',28),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',33),
  ('expression -> ID','expression',1,'p_expression_id','parser.py',38),
]