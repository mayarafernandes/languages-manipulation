class Automata:
    def __init__(self, id):
        self.id = id
        self.states = []
        self.symbols = []
        self.transitions = {}

    def __str__(self):
        automata = f'ID: {self.id}\nS |'
        for symbol in self.symbols:
            automata += f' {symbol} |'
        automata = automata[:-1]
        for state in self.states:
            transitions = f'\n{state} |'
            for symbol in self.symbols:
                if (state, symbol) in self.transitions:
                    toStates = ','.join(self.transitions[(state, symbol)])
                    transitions += f' {toStates} |'
                else:
                    transitions += '   |'
            automata += transitions[:-1]
        return automata
