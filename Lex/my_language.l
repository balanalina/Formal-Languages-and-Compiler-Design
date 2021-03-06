%{
	#include<math.h>
	#include<stdio.h>
	#include "scanner.h"
	int line_number = 0
%}

digit           [0-9]
non_zero_digit  [1-9]
number          [1-9][0-9]*|0
identifier      [a-zA-Z][a-zA-Z0-9]*
string          ["]([ _a-zA-Z0-9])*["]
constant        {number}|{string}

%%
"mini-language"                 {printf("reserved word: %s \n", yytext); return mini_language;}
"start"				{printf("reserved word: %s \n", yytext); return do_start;}
"end"				{printf("reserved word: %s \n", yytext); return do_end;}
"do"				{printf("reserved word: %s \n", yytext); return do_do;}
"int"				{printf("reserved word: %s \n", yytext); return intt;}
"ints"				{printf("reserved word: %s \n", yytext); return intts;}
"string"			{printf("reserved word: %s \n", yytext); return stringg;}
"strings"			{printf("reserved word: %s \n", yytext); return stringg;}
"if"				{printf("reserved word: %s \n", yytext); return iff;}
"else"				{printf("reserved word: %s \n", yytext); return elsee;}
"write"				{printf("reserved word: %s \n", yytext); return writee;}
"read"				{printf("reserved word: %s \n", yytext); return readd;}
"each"				{printf("reserved word: %s \n", yytext); return each;}
"while"				{printf("reserved word: %s \n", yytext); return whilee;}
"new_line"			{printf("reserved word: %s \n", yytext); return new_line;}
"+"				{printf("Operator: %s\n", yytext); return add;}
"-"				{printf("Operator: %s\n", yytext); return sub;}
"*"				{printf("Operator: %s\n", yytext); return mul;}
"/"				{printf("Operator: %s\n", yytext); return div;}
"!="				{printf("Operator: %s\n", yytext); return not_eq;}
"<"				{printf("Operator: %s\n", yytext); return less;}
"<="				{printf("Operator: %s\n", yytext); return less_eq;}
"=="				{printf("Operator: %s\n", yytext); return eq;}
">"				{printf("Operator: %s\n", yytext); return great;}
">="				{printf("Operator: %s\n", yytext); return great_eq;}
"="				{printf("Separator: %s\n", yytext); return ass;}
"["				{printf("Separator: %s\n", yytext); return left_sq;}
"]"				{printf("Separator: %s\n", yytext); return right_sq;}

[ \t]+          {}
[\n]            {++line_number;}
.               {printf("Illegal symbol: %s at line %u", yytext, line_number+1); return -1;}  
%%


int yywrap(void)
{
	return 1;
}