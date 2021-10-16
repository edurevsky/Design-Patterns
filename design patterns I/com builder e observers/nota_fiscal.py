from datetime import date, datetime
from observadores import imprime, envia_por_email, salva_no_banco

class Item(object):
    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor


class Nota_fiscal(object):                        # Parâmetros opcionais                         # Observadores
    def __init__(self, razao_social, cnpj, itens, data_de_emissao = date.today(), detalhes = "", observadores = []):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        self.__detalhes = detalhes
        if len(detalhes) > 20:
            raise Exception("Detalhes da nota não podem ter mais do que 20 caracteres")
        self.__itens = itens
        
        for observador in observadores:
            observador(self)

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes

    
if __name__ == "__main__":

    from criador_de_nota_fiscal import Criador_de_nota_fiscal

    itens = [
        Item(
            "ITEM A",
            100
        ),
        Item(
            "ITEM B",
            200
        )
    ]

    # Criação normal
    nota_fiscal = Nota_fiscal(
        cnpj="012345678901234",
        razao_social="FHSA Ltd.",
        itens=itens,
        observadores=[imprime, envia_por_email, salva_no_banco]
    )

    # Criação com builder
    nota_fical_com_builder = (
    Criador_de_nota_fiscal()
    .com_razao_social("FHSA Ltd.")
    .com_cnpj("012345678901234")
    .com_itens(itens)
    .constroi()
    )


