
class Media:
    def __init__(self, edades):
        self.edades = edades

    def calcular_media(self):
        if len(self.edades) == 0:
            return 0
        return sum(self.edades) / len(self.edades)