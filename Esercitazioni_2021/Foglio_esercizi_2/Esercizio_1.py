import random

class Automa():
    
    def __init__(self):
        self.biancheria = None
        self.calzini = None
        self.maglia = None
        self.pantaloni = None
        self.calzatura = None

    def indossa_biancheria(self):
        num = random.randint(1,100)
        if num < 80 and self.biancheria is None:
            self.biancheria = True
            return 1
        else:
            return 0

    def indossa_calzini(self):
        num = random.randint(1,100)
        if self.calzini is None and num < 80:
            self.calzini = True
            return 1
        else:
            return 0

    def indossa_maglia(self):
        num = random.randint(1,100)
        if num < 80 and self.biancheria is True and self.maglia is None:
            self.maglia= True
            return 1
        else:
            return 0

    def indossa_pantaloni(self):
        num = random.randint(1,100)
        if num < 80 and self.biancheria is True and self.calzini is True and self.pantaloni is None:
            self.pantaloni = True
            return 1
        else:
            return 0

    def indossa_calzatura(self):
        num = random.randint(1,100)
        if num < 80 and self.pantaloni is True and self.calzatura is None:
            self.calzatura = True
            return 1
        else:
            return 0

def esegui(automa, capo):
    if capo == "biancheria":
        return automa.indossa_biancheria()

    if capo == "calzini":
        return automa.indossa_calzini()

    if capo == "maglia":
        return automa.indossa_maglia()

    if capo == "pantaloni":
        return automa.indossa_pantaloni()

    if capo == "calzatura":
        return automa.indossa_pantaloni()

capi_vestiario = ["biancheria", "calzini", "maglia", "pantaloni", "calzatura"]
vestito = True

automa = Automa()

while(vestito):
    capo = random.choice(capi_vestiario)
    if capo == "maglia" and automa.biancheria is None:
        print("Non puoi indossare la maglia senza la biancheria")
    if capo == "pantaloni" and automa.biancheria is None or automa.calzini is None:
        print("Non puoi indossare i pantaloni senza biancheria o i calzini")
    if capo == "calzatura" and automa.pantaloni is None:
        print("Non puoi indossare la calzatura senza i pantaloni")
    test = esegui(automa,capo)
    if test == 0:
        raise Exception("Insuccesso")

print("automa vestito correttamente")