from Alimentos import Alimento
import csv

class FabricaAlimentos:
    lista = []
    @staticmethod
    def carregarDados():
        with open('alimentos_nutrientes - Página1.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            csv_reader.__next__()  # Tira a primeira linha (cabeçalho)

            for row in csv_reader:
                alimento = Alimento(nome = str(row[0]),
                                    preco = float(row[1]),
                                    peso = float(row[2]),
                                    calorias = float(row[3]),
                                    proteinas = float(row[4]),
                                    carboidratos = float(row[5]),
                                    acucar= float(row[6]),
                                    gorduras = float(row[7]),
                                    colestorol= float(row[8]),
                                    sodio = float(row[9]),
                                    potassio = float(row[10]),
                                    calcio = float(row[11]),
                                    vitC = float(row[12]),
                                    ferro = float(row[13]),
                                    magnesio = float(row[14]))

                FabricaAlimentos.lista.append(alimento)

    @staticmethod
    def gerar(nomes = []):
        alimentos = []

        for alimento in FabricaAlimentos.lista:
            for nome in nomes:
                if nome == alimento.nome:
                    alimentos.append(alimento)

        return alimentos

    def remover(nomes=[]):
        alimentos = FabricaAlimentos.lista

        for alimento in FabricaAlimentos.lista:
            for nome in nomes:
                if nome == alimento.nome:
                    alimentos.remove(alimento)

        return alimentos



