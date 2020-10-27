import copy

from symbol_table.hash_table import *
from PIF.pif_table import *
import string
import re


class Scanner:
    def __init__(self,file_path):
        self.symbol_table = HashTable()
        self.pif = PIF()
        self.file = file_path
        self.reserved_words = ['mini-language', 'start', 'end', 'do', 'int', 'ints', 'string', 'strings', 'if',
        'else', 'write', 'read', 'each', 'NEW_LINE', 'while']
        self.operators = ['+', '-', '*', '!=', '==', '<', '>', '<=', '>=', '=']
        self.separators = ['[', ']','.']

    # return a list with the chars of the line
    def char_split(self, word):
        return [char for char in word]

    def scan(self):
        line_no = 0
        file = open(self.file,'r')
        for line in file:
            line_no += 1
            tokens = self.detect(line)
            for token in tokens:
                if token in self.operators or token in self.separators or token in self.reserved_words:
                    self.pif.insert(token,0)
                elif token != 'error':
                    if self.symbol_table.look_up(token) == 0:
                        index = self.symbol_table.insert(token)
                    if self.is_constant(token):
                        self.pif.insert('CONST',index)
                    else:
                        self.pif.insert('ID',index)
                else:
                    print("Lexical error at line number " + str(line_no) + "!")
        file.close()

    def is_constant(self, token):
        if re.search('^[1-9][0-9]*$',token) != None:
            return True
        elif token[0] == '"' and token[len(token)-1] == '"':
            return True
        return False

    def detect(self,line):
        seen = False
        index = -1
        result_tokens = []
        tokens = line.split()
        for token in tokens:
            if seen:
                if index > tokens.index(token):
                    continue
                else:
                    seen = False
            elif token in self.reserved_words:
                result_tokens.append(token)
            #elif self.check_operator(token):
                #self.split_operands(token,tokens)
            elif token.find('"') != -1:
                seen = True
                const, index = self.find_constant(tokens,token)
                result_tokens.append(const)
            elif token in self.operators:
                result_tokens.append(token)
            elif token in self.separators:
                result_tokens.append(token)
            elif re.search("^[1-9][0-9]*$",token) != None:
                result_tokens.append(token)
            else:
                if token[0] not in string.ascii_letters:
                    result_tokens.append('error')
                else:
                    result_tokens.append(token)
        return result_tokens

    def pretty_print(self):
        s = open(self.file+"_ST.out",'w')
        s.write('Symbol table:\n')
        s.write(self.symbol_table.pretty_print())
        s.close()
        p = open(self.file+"_PIF.out", 'w')
        p.write('PIF: \n')
        p.write(self.pif.pretty_print())
        p.close()

    def find_constant(self, tokens, token):
        start_index = token.find('"')
        const = token[start_index:]
        index = tokens.index(token) + 1
        while index < len(tokens):
            if tokens[index].find('"') != -1:
                substr_index = tokens[index].find('"')
                const += " "+tokens[index][0:substr_index+1]
                return const, index
            else:
                const += " "+tokens[index]
            index+=1
        return "error",index

    def split_operands(self,token, tokens):
        index = tokens.index(token)
        op = self.get_operator(token)
        new_tokens = token.split(op)
        for new_token in new_tokens:
            index += 1
            tokens.insert(index, new_token)
            index += 1
            tokens.insert(index, op)

    def check_operator(self, token):
        if token in self.reserved_words:
            return False
        for operator in self.operators:
            if token.find(operator) != -1:
                return True
        return False

    def get_operator(self, token):
        for operator in self.operators:
            if token.find(operator) != -1:
                return operator


ok = Scanner('p1.txt')
ok.scan()
ok.pretty_print()






