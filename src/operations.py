import data as data

def list_data(dataType):
    if dataType.lower() == 'e':
        [print(f'\n{e}') for e in data.load_expressions()]        
    elif dataType.lower() == 'g':
        [print(f'\n{g}') for g in data.load_grammars()]
    elif dataType.lower() == 'a':
        [print(f'\n{a}') for a in data.load_automatas()]

def convert_ndfa_to_dfa(id):
    pass

def convert_dfa_to_rg(id):
    pass

def convert_rg_to_ndfa(id):
    pass

def check_input_in_fa(id, input):
    pass

def minimize_dfa(id):
    pass

def union_dfa(id1, id2):
    pass

def intersection_dfa(id1, id2):
    pass

def convert_re_to_dfa(id):
    pass

