class Expression:
    def __init__(self, id):
        self.id = id
        self.expression = ''

    def __str__(self):
        return f"ID: {self.id}\n{self.expression}"