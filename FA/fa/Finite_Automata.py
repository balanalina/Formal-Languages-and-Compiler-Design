import sys
from termcolor import colored, cprint

class Finite_Automata:
    def __init__(self, file_path):
        self.file = file_path
        self.start_state = None
        self.final_states = []
        self.alphabet = None
        self.states = None
        self.transitions = {}
        self.current_state = None
        self.dfa = True
        self.read_file()

    def read_file(self):
        file = open(self.file, 'r')
        fa = []
        for line in file:
            # we don't need the new line
            fa.append(line.replace("\n", ""))
        # get the information from the file
        self.start_state = fa[2]
        self.current_state = self.start_state
        self.final_states = fa[3].split(',')
        self.states = fa[0].split(',')
        self.alphabet = fa[1].split(',')
        for i in range(4, len(fa)):
            if (fa[i][0], fa[i][2]) in self.transitions.keys():
                self.dfa = False
            self.transitions[(fa[i][0], fa[i][2])] = fa[i][6]

    def DFA_accept(self, sequence):
        # check if sequence contains letters that are not in our alphabet
        for char in sequence:
            if char not in self.alphabet:
                return False
        for char in sequence:
            if not self.check_next_state(char):
                return False
        # we iterated all the characters from the sequence and they followed the DFA until now
        # if the last state is not a final state then it doesn't follow the DFA
        if not self.final_states.__contains__(str(self.current_state)):
            return False
        return True

    # checks if from current state we can get to the next one from the sequence
    def check_next_state(self, char):
        possible_transitions = []
        # get all possible 'next state' transitions from the current state
        for state in self.transitions.keys():
            if state[0] == self.current_state:
                possible_transitions.append(state[1])
        # switch to next state
        for trans in possible_transitions:
            if char == trans:
                old_state = self.current_state
                self.current_state = self.transitions[old_state, trans]
                return True
        return False

    def DFA_check(self):
        pass

    def get_menu(self):
        menu = ''
        menu += '0.Exit \n'
        menu += '1.Display the set of states.\n'
        menu += '2.Display the alphabet.\n'
        menu += '3.Display all the transitions.\n'
        menu += '4.Display the set of final states.\n'
        menu += '5.Check if a sequence is accepted by the FA.\n'
        menu += '6.Check if deterministic. \n'
        menu += 'Enter command:'
        return menu

    def menu(self):
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
                if self.DFA_accept(sequence):
                    print(colored(sequence + " is accepted!", 'green'))
                else:
                    print(colored(sequence + " is not accepted!", 'red'))
            elif command == 6:
                if self.dfa:
                    print(colored("Is deterministic!", 'green'))
                else:
                    print(colored("Is not deterministic!", 'red'))
            else:
                break


ok = Finite_Automata("FA.in")
ok.menu()

# 010111 - accepted for Fa2
# 010111101
# 00000001

# 01011110111
