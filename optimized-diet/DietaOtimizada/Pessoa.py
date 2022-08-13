from FabricaNutrientes import FabricaNutrientes


class Pessoa:
    def __init__(self, nome, idade,altura,peso,sexo, atividade):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.sexo = sexo
        self.atividade = atividade

        self.necessidadesNutricionais = FabricaNutrientes.gerar(
            calorias  =self.calculaCaloria(),
            proteinas = self.calculaCaloria() * 0.15 / 4 ,
            carboidratos= self.calculaCaloria() * 0.60 / 4,
            gorduras = self.calculaCaloria() * 0.25 / 9,
            acucar=25,
            colestorol=300,
            sodio=2000,
            potassio=3500,
            calcio=1000,
            vitC=90,
            ferro=8,
            magnesio=260)

    def calculaTMB(self):
        if(self.sexo == "Masculino"):
            if (self.idade >= 18 and self.idade <= 30):
                valor = 15.4 * self.peso - 27 * self.altura + 717
            if (self.idade >= 30 and self.idade <= 60):
                valor = 11.3 * self.peso + 16 * self.altura + 901
        else:
            if (self.idade >= 18 and self.idade <= 30):
                valor = 13.3 * self.peso + 334 * self.altura + 35
            if (self.idade >= 30 and self.idade <= 60):
                valor = 8.7 * self.peso - 25 * self.altura + 865

        return valor

    def calculaGet(self, tmb):
        if(self.sexo == "Masculino"):
            if (self.atividade == "Leve"):
                fator = 1.55
            if (self.atividade == "Moderada"):
                fator = 1.78
            if (self.atividade == "Pesada"):
                fator = 2.10
        else:
            if (self.atividade == "Leve"):
                fator = 1.56
            if (self.atividade == "Moderada"):
                fator = 1.64
            if (self.atividade == "Pesada"):
                fator = 1.82

        return fator * tmb

    def calculaCaloria(self):
        tmb = self.calculaTMB()
        caloria = self.calculaGet(tmb)

        return caloria
