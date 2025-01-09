class Veiculo:

    def __new__(cls, *args, **kargs):
        print("Alocando memória para criar e retorns uma nova instanca da classe")
        instance = super(Veiculo, cls).__new__(cls)
        return instance
    
    def __init__(self,nome, cor, marca,ano):
        self.nome = nome
        self.cor = cor 
        self.marca = marca 
        self.ano = ano
        self.km = 0


    def apresentacao(self):
        print(f"Esse é o carro {self.nome} da marca {self.marca} de cor {self.cor} do ano {self.ano} de {self.km}km")
    
    def acelerar(self):
        velocidade = int(input(f"Deseja acelerar quanto no {self.nome}? "))
        print(f"acelerando {velocidade}")
        self.km = velocidade

    

# guardando a referência do objeto em uma variavel simples

carro1 = Veiculo("Corolla","Prata","Toyota",2025)
