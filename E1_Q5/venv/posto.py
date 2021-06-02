
class Bomba:

    def __init__(self, tipo, valor, qtd):
        self.tipo_combustivel = tipo
        self.valor_litro = valor
        self.qtd_combustivel = qtd
        self.valor_pagar = 0
        self.qtd_litros = 0

    def abastecer_valor(self, valor):
        self.qtd_litros = valor / self.valor_litro
        self.qtd_combustivel -= self.qtd_litros
        return self.qtd_litros

    def abastecer_qtde(self, qtde):
        self.valor_pagar = qtde * self.valor_litro
        self.qtd_combustivel -= self.qtd_litros
        return self.valor_pagar

    def __repr__(self):
        return "Tipo de combustivel: %s, Valor por litro: R$%.3f, " \
               "Quantidade de combustivel: %.3f Litros"%(self.tipo_combustivel, self.valor_litro, self.qtd_combustivel)