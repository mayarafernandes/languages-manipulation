import traceback
from expression import *
from grammar import *
from automata import *

AUTOMATAS_DATA_FILE = '../data/automata'
GRAMMARS_DATA_FILE = '../data/grammar'
EXPRESSIONS_DATA_FILE = '../data/expression'

def load_automatas():
    try:
        automatas = []
        automata = Automata(None)
        dataFile = open(AUTOMATAS_DATA_FILE, 'r')        
        while True:
            line = dataFile.readline()
            if not line:
                if bool(automata.id) & (len(automata.transitions) > 0):
                    automatas.append(automata)
                break
            line = line.strip()
            if line.lower().startswith('id:') & bool(line[3:].strip()):
                if bool(automata.id) & (len(automata.transitions) > 0):
                    automatas.append(automata)
                automata = Automata(line[3:].strip())
                continue
            if line.lower().startswith('s'):
                symbols = line.split('|')
                if len(symbols) < 2:
                    continue
                for i in range(1, len(symbols)):
                    automata.symbols.append(symbols[i].strip())
                continue
            transitions = line.split('|')
            if len(transitions) != (len(automata.symbols) + 1):
                continue
            state = transitions[0].strip()
            automata.states.append(state)
            for i in range(1, len(transitions)):
                toStates = transitions[i].strip()
                if not bool(toStates):
                    continue
                toStates = [toState.strip() for toState in toStates.split(',')]
                automata.transitions[(state, automata.symbols[i - 1])] = toStates
        dataFile.close()
        return automatas
    except:
        traceback.print_exc()

def load_grammars():
    try:        
        grammars = []      
        grammar = Grammar(None)
        dataFile = open(GRAMMARS_DATA_FILE, 'r')
        while True:
            line = dataFile.readline()
            if not line:
                if bool(grammar.id) & (len(grammar.productions) > 0):
                    grammars.append(grammar)
                break
            line = line.strip()
            if line.lower().startswith('id:') & bool(line[3:].strip()):
                if bool(grammar.id) & (len(grammar.productions) > 0):
                    grammars.append(grammar)
                grammar = Grammar(line[3:].strip())
                continue
            productionElements = line.split('::=')
            if len(productionElements) != 2:
                continue
            rules = [rule.strip() for rule in productionElements[1].split('|')]
            grammar.productions[productionElements[0].strip()] = rules
        dataFile.close()
        return grammars
    except:
        traceback.print_exc()

def load_expressions():
    try:
        expressions = []
        expression = Expression(None)
        dataFile = open(EXPRESSIONS_DATA_FILE, 'r')
        while True:
            line = dataFile.readline()
            if not line:
                break
            line = line.strip()
            if line.lower().startswith('id:') & bool(line[3:].strip()):
                expression = Expression(line[3:].strip())
                continue
            if (not line.lower().startswith('id:')) & bool(line):
                expression.expression = line
                if bool(expression.id):
                    expressions.append(expression)
        dataFile.close()
        return expressions
    except:
        traceback.print_exc()