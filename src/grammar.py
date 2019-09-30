class Grammar:
    def __init__(self, id):
        self.id = id
        self.productions = {}

    def __str__(self):
        grammar = f'ID: {self.id}'
        for productionHead in self.productions.keys():
            production = f'\n{productionHead} ::='
            for rule in self.productions[productionHead]:
                production += f' {rule} |'
            grammar += production[:-1]
        return grammar