class Identidade:
    def __init__(self, nome, sobrenome, data_nascimento, endereco, tipo_sanguinio):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.tipo_sanguinio = tipo_sanguinio
    
    def data_to_dict(self):
        return{
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'data_nascimento': self.data_nascimento,
            'endereco': self.endereco,
            'tipo_sanguinio': self.tipo_sanguinio
        }
    