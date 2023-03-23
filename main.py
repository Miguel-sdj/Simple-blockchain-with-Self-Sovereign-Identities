import bloco
import identidade

user01 = identidade.Identidade('Miguel', 'Cabral', '01/01/2001', 'Rua Bione 77', 'O+')
bloco01 = bloco.Bloco(user01.data_to_dict(), '0')

bloco.Bloco.imprimir_cadeia_de_blocos(bloco01)

user01.sobrenome = 'Junior'
bloco02 = bloco.Bloco(user01.data_to_dict(), bloco01.hash)

bloco.Bloco.imprimir_cadeia_de_blocos(bloco02)


user02 = identidade.Identidade('Rafael', 'Cabral', '01/01/2002', 'Rua Bione 77', 'A+')
bloco03 = bloco.Bloco(user02.data_to_dict(), bloco02.hash)

bloco.Bloco.imprimir_cadeia_de_blocos(bloco03)