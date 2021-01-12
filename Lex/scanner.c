#include <stdio.h>
#include "scanner.h"

extern int yylex();
extern int line_number;
extern char* yytext;

int main(void)
{
	int token;
	token = yylex();
	while(token){
		printf("Token: %d\n", token);
        token = yylex();
	}
	
	return 0;
}
