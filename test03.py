class Carro:
    rodas = 4

    def __new__(cls, *args, **kargs):
        print("Alocando memória para criar e retorns uma nova instanca da classe")
        instance = super(Carro, cls).__new__(cls)
        return instance
    
    def __init__(self,nome, cor, marca,ano):
        self.nome = nome
        
        self.cor = cor 
        self.marca = marca 
        self.ano = ano 

    def apresentacao(self):
        print(f"Esse é o carro {self.nome} da marca {self.marca} de cor {self.cor} de ano {self.ano}")
    

# guardando a referência do objeto em uma variavel simples

carro1 = Carro("Corolla","Prata","Toyota",2025)
carro1.apresentacao()
    