/* A Bison parser, made by GNU Bison 2.7.  */

/* Bison interface for Yacc-like parsers in C
   
      Copyright (C) 1984, 1989-1990, 2000-2012 Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Enabling traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     mini_language = 258,
     do_start = 259,
     do_end = 260,
     do_do = 261,
     intt = 262,
     intts = 263,
     stringg = 264,
     stringgs = 265,
     iff = 266,
     elsee = 267,
     writee = 268,
     readd = 269,
     each = 270,
     whilee = 271,
     new_line = 272,
     add = 273,
     sub = 274,
     mul = 275,
     div = 276,
     not_eq = 277,
     less = 278,
     less_eq = 279,
     eq = 280,
     great = 281,
     great_eq = 282,
     ass = 283,
     left_sq = 284,
     right_sq = 285,
     identifier = 286,
     constant = 287
   };
#endif
/* Tokens.  */
#define mini_language 258
#define do_start 259
#define do_end 260
#define do_do 261
#define intt 262
#define intts 263
#define stringg 264
#define stringgs 265
#define iff 266
#define elsee 267
#define writee 268
#define readd 269
#define each 270
#define whilee 271
#define new_line 272
#define add 273
#define sub 274
#define mul 275
#define div 276
#define not_eq 277
#define less 278
#define less_eq 279
#define eq 280
#define great 281
#define great_eq 282
#define ass 283
#define left_sq 284
#define right_sq 285
#define identifier 286
#define constant 287



#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;

#ifdef YYPARSE_PARAM
#if defined __STDC__ || defined __cplusplus
int yyparse (void *YYPARSE_PARAM);
#else
int yyparse ();
#endif
#else /* ! YYPARSE_PARAM */
#if defined __STDC__ || defined __cplusplus
int yyparse (void);
#else
int yyparse ();
#endif
#endif /* ! YYPARSE_PARAM */

#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
