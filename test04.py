# esse será bem simples, apenas demonstraremos o uso de decorator

class Banco:
    taxa_juros = 0.10

    def __init__(self,nome):
        self._nome = nome
        self._saldo = 0
    
    @classmethod
    def alterar_taxa(cls, nova_taxa):
        cls.taxa_juros = nova_taxa
    
    @staticmethod
    def rendimento(meses, valor):   
        print(f"SEU RENDIMENTO SERÁ: {valor * meses * Banco.taxa_juros}$")
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,novo_nome):
        self._nome = novo_nome
    

pessoa1 = Banco("jose")
pessoa1.rendimento(100,2)

# usamos o property (getter) e o setter, futuramente usaremos o deleter

    
