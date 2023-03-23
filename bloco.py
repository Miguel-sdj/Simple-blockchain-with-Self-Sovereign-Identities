import hashlib
import datetime

class Bloco:
    def __init__(self, data, bloco_anterior):
        self.timestamp = datetime.datetime.now() # salvando no bloco a data e horário atual
        self.data = data #salvando a data no bloco
        self.hash_anterior = bloco_anterior # salvando o hash do bloco anterior
        self.hash = self.calcular_hash() #calculando seu hash

    def calcular_hash(self):
        dados = str(self.timestamp) + str(self.data) + str(self.hash_anterior) # dados atual vai ser o conjunto de todas infos
        hash_calculado = hashlib.sha256(dados.encode()).hexdigest() # Encodificando para gerar o hash.

        return hash_calculado
    
    def imprimir_cadeia_de_blocos(bloco_anterior):
        bloco_atual = bloco_anterior

        while bloco_atual:
            print('Bloco #' + str(bloco_atual.hash))
            print('Dados: ' + str(bloco_atual.data))
            print('Hash anterior: ' + str(bloco_atual.hash_anterior))
            print('Hash atual: ' + str(bloco_atual.hash))
            print('Timestamp: ' + str(bloco_atual.timestamp))
            print('-------------------------')
            bloco_atual = bloco_atual.proximo_bloco if hasattr(bloco_atual, 'proximo_bloco') else None
