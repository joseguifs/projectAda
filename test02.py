# padrão singlenton

class Banco:
    att_classe = None
    
    def __new__(cls):
        if Banco.att_classe is None:
            Banco.att_classe = super().__new__(cls)
            return Banco.att_classe
        return Banco.att_classe    
    

