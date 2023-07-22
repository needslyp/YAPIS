grammar file;
program
    : def* EOF
    ;

stat: TYPE ID (',' ID)* '=' expr (',' expr )*';'
    | ID (',' ID)* '=' ('(' TYPE ')')? expr (',' expr )*';'
    | expr ';'
    | if_else ';'
    | for_cycle ';'
    | while_cycle ';'
    ;

def : TYPE ID '(' (parameter (',' parameter)*)* ')' '{' stat_box return? '}' ';' ;

return: RETURN expr ';' ;

parameter : TYPE '&' ID ;

op
    : '+'
    | '-'
    | '/'
    | '*'
    ;

s_op
    : '++'
    | '--'
    ;

comp
    : '>'
    | '<'
    | '<='
    | '>='
    | '=='
    | '!='
    ;

expr: ID
    | ELEMENT
    | list
    | func
    | iter
    | expr s_op
    | 'not' expr
    | expr 'and' expr
    | expr 'or' expr
    | expr op expr
    | expr comp expr
    | ID DOT func
    ;

for_cycle: 'for' LPAREN TYPE ID '=' ELEMENT ',' ID comp expr ',' ID s_op RPAREN LCURLY stat_box RCURLY ;
while_cycle : 'while' LPAREN TYPE ID comp ELEMENT RPAREN LCURLY stat_box RCURLY ;
if_else : 'if' LPAREN  expr comp expr RPAREN LCURLY stat_box RCURLY ('else' LCURLY stat_box RCURLY)? ;
list : LSQUARE ( (ELEMENT|list) (',' (ELEMENT|list))* )? RSQUARE ;
iter : ID LSQUARE (ID | ELEMENT) RSQUARE ;
func : ID LPAREN (expr (',' expr)*)? RPAREN ;

stat_box: stat* ;

AND : 'and' ;
OR : 'or' ;
NOT : 'not' ;
EQ : '=' ;
COMMA : ',' ;
SEMI : ';' ;
LPAREN : '(' ;
RPAREN : ')' ;
LCURLY : '{' ;
RCURLY : '}' ;
LSQUARE : '[' ;
RSQUARE : ']' ;
DOT : '.' ;
LTHEN : '<' ;
MTHEN : '>' ;

PLUS : '+' ;
MINUS : '-' ;
ASTERISK : '*' ;
DIVISION : '/' ;
UMPERSANT : '&' ;
RETURN : 'return' ;

IF : 'if' ;
ELSE : 'else';

TYPE : 'list' | 'element' ;

ELEMENT : [1-9][0-9]* | '0' | '\'' [a-zA-Z_ 0-9]* '\'';
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
WS: [ \t\n\r\f]+ -> skip ;
