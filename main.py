# 1 - Escreva um número por extenso 1 a 99

class NomeDosNumeros():

    def __init__(self):
        # Input do valor
        self.valor = input('Digite um Valor: ')
        # Nome dos valores numericos em string dentro de um dicionario
        self.nomes_dos_valores = {
            'unidade': {
                'um': 1,
                'dois': 2,
                'tres': 3,
                'quatro': 4,
                'cinco': 5,
                'seis': 6,
                'sete': 7,
                'oito': 8,
                'nove': 9,
                'dez': 10
            },

            'dezenas_init': {
                'onze': 11,
                'doze': 12,
                'treze': 13,
                'quatorze': 14,
                'quinze': 15,
                'dezeseis': 16,
                'dezesete': 17,
                'dezoito': 18,
                'dezenove': 19,
            },

            'dezenas': {
                'vinte': 20,
                'trinta': 30,
                'quarenta': 40,
                'cinquenta': 50,
                'sessenta': 60,
                'setenta': 70,
                'oitenta': 80,
                'noventa': 90
            },

            # ver aplicabilidade de adicionar centenas
            'centenas': {
                'cento': 100,
                'dozentos': 200,
                'trezentos': 300,
                'quatrocentos': 400,
                'quinhentos': 500,
                'seiscentos': 600,
                'setecentos': 700,
                'oitocentos': 800,
                'novecentos': 900
            }
        }
        # Salva o valor e muda variavel para ver qnts numeros tem no input
        self.digito = self.valor
        if self.valor.isnumeric:
            self.valor = len(self.valor)
        self.escrever_numero()

    def escrever_numero(self):
        if self.valor == 1:
            for nome, resultado in self.nomes_dos_valores['unidade'].items():
                if int(self.digito) == resultado:
                    print(nome)

        if self.valor == 2 and self.digito[0] == '1' and self.digito[1] == '0':
            print(list(self.nomes_dos_valores['unidade'])[9])

        if self.valor == 2 and self.digito[0] == '1':
            for nome, result in self.nomes_dos_valores['dezenas_init'].items():
                aux = str(result)
                if self.digito[1] == aux[1]:
                    print(nome)

        if self.valor == 2 and self.digito[0] != '1':
            for nome, resultado in self.nomes_dos_valores['dezenas'].items():
                aux = str(resultado)
                if self.digito[0] == aux[0]:
                    dezena = nome
            for nome, resultado in self.nomes_dos_valores['unidade'].items():
                if self.digito[1] == str(resultado):
                    print(f'{dezena} e {nome}')


NomeDosNumeros()
