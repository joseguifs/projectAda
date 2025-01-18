from datetime import datetime, date, timedelta


def validar_nome(nome):
    nome_teste = str(nome).strip().split()
    if ''.join(nome_teste).isalpha():
        return True
    else:
        return False

class Hotel:
    Tipos_Quartos = {
        "Quarto_tipo1":10, #qtd <= 4
        "Quarto_tipo2":10, #qtd <= 5
        "Quarto_tipo3":10, #qtd <= 6
        "Quartos_disponiveis":30
    }

    def __new__(cls, *args):
        if Hotel.Tipos_Quartos["Quartos_disponiveis"] == 0:
            raise ValueError("NÃO TEMOS VAGAS EM NENHUM DOS QUARTOS NO MOMENTO, ESTÃO TODOS OCUPADOS.")
        return super(Hotel,cls).__new__(cls)

    def __init__(self, nome, qtd_pessoas, qnts_dias):
        self.__nome = nome
        self.qtd_pessoas = qtd_pessoas
        self.tipo_quarto = "Quarto_tipo1" if self.qtd_pessoas <= 4 else("Quarto_tipo2" if self.qtd_pessoas <= 5 else "Quarto_tipo3") 
        self.numero_quarto = Hotel.Tipos_Quartos[self.tipo_quarto]
        self.data_alocacao = datetime.today().date()
        self.termino_alocao = datetime.today().today() + timedelta(days=self.qnts_dias)
        Hotel.Tipos_Quartos["Quartos_disponiveis"] -= 1
        Hotel.Tipos_Quartos[self.tipo_quarto] -= 1
    

    def __str__(self):
        return f"NOME DE QUEM ALUGOU O QUARTO: {self.__nome}\nQUANTIDADE DE PESSOAS: {self.qtd_pessoas}\nNUMERO DO QUARTO: {self.numero_quarto}"

while True:
    try:
        Hospedes = list()
        nome_locador = input("Nome do locador do quarto: ")
        if validar_nome(nome_locador):
                pass
        else:
            print("nome inválido! Digite um nome válido")
            continue
        print("TEMOS QUARTO PARA 4, 5 E 6 PESSOAS!")
        quantas_pessoas = int(input("Deseja alugar um quarto para quantos pessoas? "))
        if quantas_pessoas > 6:
            print("NÃO TEMOS QUARTA PARA ESSA QUANTIDADE")
            continue
        quantos_dias = int(input("Deseja alocar o quarto por quantos dias? "))
        Hospedes.append(Hotel(nome_locador,quantas_pessoas, quantos_dias))
    except ValueError as erro:
        print(f"ERRO: {erro}")
    else:
        continuar = input("[S/N]: ").upper()
        if continuar == 'S':
            continue
        else:
            break
