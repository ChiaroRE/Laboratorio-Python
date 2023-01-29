class Automobile():

  def __init__(self, casa, modello, numero_posti, targa):
    self.casa = casa
    self.modello = modello
    self.numero_posti = numero_posti
    self.targa = targa

  def __str__(self):
    print("La casa automobilistica è {}".format(self.casa))
    print("Il modello dell'auto è {}".format(self.modello))
    print("L'auto è omologata per {} persone".format(self.numero_posti))
    print("La targa è {}".format(self.targa))

  def parla(self):
    print("Broom Broom")

  def confronta(self, auto2):
    if self.casa == auto2.casa and self.modello == auto2.modello and self.numero_posti == auto2.numero_posti:
      return True
    else:
      return False

Auto1 = Automobile("Mercedes", "Classe S Coupè", 5, "EC1434KR")
Auto2 = Automobile("Mercedes", "Classe A Coupè", 5, "E342FGH3")
print(Auto1.confronta(Auto2))

