class Automobile():

  def __init__(self, casa, modello, posti, targa):
    self.casa = casa
    self.modello = modello
    self.posti = posti
    self.targa = targa

  def __str__(self):
    print("La casa automobilistica è {}".format(self.casa))
    print("Il modello dell'auto è {}".format(self.modello))
    print("L'auto è omologata per {} persone".format(self.posti))
    print("La targa è {}".format(self.targa))

  def parla(self):
    print("Broom Broom")

  def confronta(self, auto2):
    if self.casa == auto2.casa and self.modello == auto2.modello and self.posti == auto2.posti:
      return True
    else:
      return False

class Transformer(Automobile):
  def __init__(self, casa, modello, posti, targa, nome, generazione, grado, reparto):
    super().__init__(casa,modello, posti,targa)
    self.nome = nome
    self.generazione = generazione
    self.grado = grado
    self.reparto = reparto

  def scheda_militare(self):
    print("Il nome del Transformer è {}".format(self.nome))
    print("La sua generazione è {}".format(self.generazione))
    print("Il suo grado è {}".format(self.grado))
    print("Il suo reparto è {}".format(self.reparto))

auto_0 = Automobile("Mercedes", "Classe S Coupè", 5, "EC1434KR")
t_0 = Transformer("Mercedes", "Classe S Coupè", 5, "EC1434KR", "Edobot", 3, "sergente", "artiglieria pesante")
t_1 = Transformer("Mercedes", "Classe A Coupè", 4, "EC5424KR", "Erikabot", 3, "capitano", "artiglieria leggera")


print(type(auto_0))
print(issubclass(Transformer, Automobile))
print(type(t_0))
print(type(t_1))
print(isinstance(t_1,Automobile))
print(isinstance(auto_0,Transformer))