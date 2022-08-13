#importando o Pulp
from pulp import *

class Dieta:
    def __init__(self, pessoa , alimentos=[], tolerancia = 0):
        self.pessoa = pessoa
        self.alimentos = alimentos
        self.tolerancia = tolerancia

        self.variaveis = []
        self.prob = LpProblem("Dieta nutricional", LpMinimize)

    def __criaVariaveis(self):
        for i in range(len(self.alimentos)):
            self.variaveis.append(LpVariable(name=self.alimentos[i].nome, cat='Continuous', lowBound=0))

    def __criaRestricoes(self):
        #Quantidade máxima e mínimas de nutrientes nutrientes
        for chaveNutriente in self.pessoa.necessidadesNutricionais.keys():
            if(self.pessoa.necessidadesNutricionais[chaveNutriente] != 0 ):
                #Mínima
                self.prob += lpSum(self.alimentos[i].nutrientes[chaveNutriente] * self.variaveis[i] for i in
                                   range(len(self.alimentos))) >= self.pessoa.necessidadesNutricionais[chaveNutriente]*(1 - self.tolerancia) #Quantos por centos a mais
                # Máxima
                self.prob += lpSum(self.alimentos[i].nutrientes[chaveNutriente] * self.variaveis[i] for i in
                                   range(len(self.alimentos))) <= self.pessoa.necessidadesNutricionais[chaveNutriente] * (1 + self.tolerancia)  # Quantos por centos a mais

    def __criaFuncaoDeCusto(self):
        self.prob += lpSum(self.alimentos[i].preco * self.variaveis[i] for i in range(len(self.alimentos)))

    def resolver(self):
        self.__criaVariaveis()
        self.__criaRestricoes()
        self.__criaFuncaoDeCusto()

        self.status = self.prob.solve()

    def mostrarResultados(self):
        precoTotal = 0

        print(f'-----------Dieta para {self.pessoa.nome}---------------')
        print("Resultado:" + LpStatus[self.status] + "\n");

        if(LpStatus[self.status] != "Infeasible"):
            for i in range(len(self.alimentos)):
                if(self.variaveis[i].varValue != 0):
                    print(f'{self.alimentos[i].nome}: %.2f' % (self.variaveis[i].varValue * 100) + "g")
                    precoTotal += self.alimentos[i].preco * self.variaveis[i].varValue

        print("\nPreco total: %.2f" % precoTotal)

        print(f'--------------------------------------------------------')
