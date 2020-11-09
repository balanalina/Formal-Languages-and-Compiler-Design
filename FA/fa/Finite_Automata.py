import sys
from termcolor import colored, cprint

class Finite_Automata:
    def __init__(self, file_path):
        self.file = file_path
        self.fa = []
        self.start_state = None
        self.final_states = []
        self.alphabet = None
        self.states = None
        self.transitions = {}
        self.current_state = 'A'
        self.read_file()

    def read_file(self):
        file = open(self.file, 'r')
        fa = []
        for line in file:
            line.replace("\n","")
            fa.append(line)
        self.start_state = fa[2]
        self.final_states = fa[3].split()
        self.states = fa[0].split()
        self.alphabet = fa[1].split()
        for i in range(4,len(fa)):
            self.transitions[(fa[i][0],fa[i][2])] = fa[i][6]

    def DFA_check(self, sequence):
        for char in sequence:
            if char != '0' and char != '1':
                return False
        for char in sequence:
            if not self.check_next_state(char):
                return False
        if not self.final_states.__contains__(str(self.current_state)):
            return False
        return True

    def check_next_state(self,char):
        possible_transitions = []
        for state in self.transitions.keys():
            if state[0] == self.current_state:
                possible_transitions.append(state[1])
        for trans in possible_transitions:
            if char == trans:
                old_state = self.current_state
                self.current_state = self.transitions[old_state,trans]
                return True
        return False

    def get_menu(self):
        menu = ''
        menu += '0.Exit \n'
        menu += '1.Display the set of states.\n'
        menu += '2.Display the alphabet.\n'
        menu += '3.Display all the transitions.\n'
        menu += '4.Display the set of final states.\n'
        menu += '5.Check if a sequence is accepted by the FA.\n'
        menu += 'Enter command:'
        return menu

    def menu(self):
        self.read_file()
        while True:
            print("\n")
            print(self.get_menu())
            command = int(input())
            print("\n")
            if command == 1:
                print(self.states)
            elif command == 2:
                print(self.alphabet)
            elif command == 3:
                for transition in self.transitions.keys():
                    print(str(transition) + " --> " + str(self.transitions[transition]))
            elif command == 4:
                print(self.final_states)
            elif command == 5:
                print("Enter the sequence: ")
                sequence = input()
                if self.DFA_check(sequence):
                    print(colored(sequence + " is accepted!",'green'))
                else:
                    print(colored(sequence + " is not accepted!",'red'))
            else:
                break





ok = Finite_Automata("FA.in")
ok.menu()


