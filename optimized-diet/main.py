from FabricaAlimentos import FabricaAlimentos
from FabricaNutrientes import FabricaNutrientes
from Pessoa import Pessoa
from Dieta import Dieta

if __name__ == '__main__':
    FabricaAlimentos.carregarDados()
    alimentos = FabricaAlimentos.lista

    #Exemplo 1
    guilherme = Pessoa(nome= "João", idade=23, altura=1.73, peso=60, sexo="Masculino", atividade="Moderada")
    DietaGuilherme = Dieta( pessoa = guilherme, tolerancia=0.15, alimentos = alimentos)

    DietaGuilherme.resolver()
    DietaGuilherme.mostrarResultados()

    #Exemplo 2
    nayara = Pessoa(nome="Ana Paula", idade=26, altura=1.72, peso=56, sexo="Feminino", atividade="Leve")
    alimentosNayara = FabricaAlimentos.gerar([ "Feijao carioca", "Maca", "Banana", "Pera", "Arroz branco"])

    DietaNayara = Dieta(pessoa=nayara, tolerancia=0.20, alimentos=alimentosNayara )
    DietaNayara.resolver()
    DietaNayara.mostrarResultados()

    #Exemplo 3
    #Primeiro teste
    pedro = Pessoa(nome="Pedro", idade=35, altura=1.9, peso=90, sexo="Masculino", atividade="Pesada")
    alimentosPedro = FabricaAlimentos.remover(["Goiaba","Laranja"])

    DietaPedro = Dieta(pessoa=pedro, tolerancia=0.15, alimentos=alimentos)
    DietaPedro .resolver()
    DietaPedro .mostrarResultados()

    #Retirando a quantidade de açucar do problema
    pedro = Pessoa(nome="Pedro", idade=35, altura=1.9, peso=90, sexo="Masculino", atividade="Pesada")
    alimentosPedro = FabricaAlimentos.remover(["Goiaba","Laranja"])

    pedro.necessidadesNutricionais["acucar"] = 0

    DietaPedro = Dieta(pessoa=pedro, tolerancia=0.15, alimentos=alimentos)
    DietaPedro.resolver()
    DietaPedro.mostrarResultados()

    #Diminuido a tolerância
    pedro = Pessoa(nome="Pedro", idade=35, altura=1.9, peso=90, sexo="Masculino", atividade="Pesada")
    alimentosPedro = FabricaAlimentos.remover(["Goiaba", "Laranja"])

    DietaPedro = Dieta(pessoa=pedro, tolerancia=0.25, alimentos=alimentos)
    DietaPedro.resolver()
    DietaPedro.mostrarResultados()







