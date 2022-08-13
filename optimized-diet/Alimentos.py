from FabricaNutrientes import FabricaNutrientes

class Alimento:
    def __init__(self, nome = "", preco = 0, peso = 0, calorias = 0,  proteinas = 0, carboidratos = 0, acucar = 0,
        gorduras = 0 , colestorol= 0, sodio = 0, potassio = 0, calcio = 0, vitC = 0, ferro = 0, magnesio = 0):
        self.nome = nome
        self.preco = preco
        self.peso = peso
        self.nutrientes = FabricaNutrientes.gerar(
            calorias = calorias,
            proteinas = proteinas,
            carboidratos = carboidratos,
            acucar = acucar,
            gorduras = gorduras,
            calcio = calcio,
            ferro= ferro,
            potassio = potassio,
            colestorol= colestorol,
            sodio = sodio,
            vitC = vitC,
            magnesio = magnesio)

