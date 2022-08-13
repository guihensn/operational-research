class FabricaNutrientes:
    @staticmethod
    def gerar(calorias = 0, proteinas = 0, carboidratos = 0,acucar = 0, gorduras = 0 , colestorol= 0,
              sodio = 0, potassio = 0, calcio = 0, vitC = 0, ferro = 0, magnesio = 0):
        nutrientes = {
            "calorias": calorias,
            "proteinas": proteinas,
            "carboidratos": carboidratos,
            "acucar": acucar,
            "gorduras": gorduras,
            "calcio": calcio,
            "ferro": ferro,
            "vitamina C": vitC,
            "magnesio": magnesio,
            "colestorol": colestorol,
            "sodio": sodio,
            "potassio" : potassio
        }
        return nutrientes

