%{
	#include<stdio.h>
	#include<stdlib.h>

	#define YYDEBUG 1
%}

%token mini_language 
%token do_start 
%token do_end 
%token do_do 
%token intt 
%token intts 
%token stringg
%token stringgs
%token iff
%token elsee 
%token writee 
%token readd 
%token each 
%token whilee 
%token new_line 
%token add 
%token sub 
%token mul 
%token div 
%token not_eq 
%token less 
%token less_eq 
%token eq 
%token great 
%token great_eq 
%token ass 
%token left_sq 
%token right_sq 
%token identifier
%token constant

%start program

%% 
program: mini_language do_start declist cmpdstmt do_end;

declist: declaration| declaration declist;

declaration: type identifier | type assstmt;

type: type1 | arraydecl;

type1: stringg | stringgs | intt | intts;

arraydecl: declaration left_sq "("constant | identifier")" right_sq;

cmpdstmt: do_do stmtlist do_end;

stmtlist: stmt | stmt stmtlist;

stmt: simplestmt | structstmt;
	     
simplestmt: assstmt | iostmt;

assstmt: identifier ass expression;

expression: term | expression op term;

op: add | sub | mul | div;

term: factor | term op factor;

factor: identifier | constant;

iostmt: identifier ass readd | writee "("identifier | constant")";

structstmt: cmpdstmt | ifstmt | whilestmt;

ifstmt: iff condition do_do stmt do_end elsee do_do stmt do_end | simplestmt iff condition;

condition: expression relation expression;

relation: eq | not_eq | less | less_eq | great | great_eq;

whilestmt: whilee condition do_do stmt do_end;
%%

yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
  if (argc > 1) 
    yyin = fopen(argv[1], "r");
  if ( (argc > 2) && ( !strcmp(argv[2], "-d") ) ) 
    yydebug = 1;
  if ( !yyparse() ) 
    fprintf(stderr,"\t No errors detected\n");
}