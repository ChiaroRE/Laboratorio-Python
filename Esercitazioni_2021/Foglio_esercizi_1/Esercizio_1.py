def stampa(lista):
  for item in lista:
    print(item)

def statistiche(lista):
  for item in lista:
    if type(item) != int:
      raise Exception("La lista non è di numeri interi")
  somma = sum(lista)
  print("La somma è {}".format(somma))
  media = somma / len(lista)
  print("La media è {}".format(media))
  minimo = min(lista)
  print("Il minimo è {}".format(minimo))
  #minimo = lista[0]
  #for item in lista
  #  if minimo < item
  #     minimo = item
  massimo = max(lista)
  print("Il massimo è {}".format(massimo))
  #Uguale a sopra con >

def somma_vettoriale(lista1, lista2):
  int1 = True
  int2 = True
  
  for item in lista1:
    if type(item) != int:
      print("La prima lista non è di numeri interi")
      int1 = False
  for item in lista2:
    if type(item) != int:
      print("La seconda lista non è di numeri interi")
      int2 = False
  somma_v = []
  if (int1 and int2) and (len(lista1) == len(lista2)):
    for i in range((len(lista1))):
      s = lista1[i] + lista2[i]
      somma_v.append(s)
  return somma_v
      
lista = [3,5,6.2,"Viale"]
l = [23,6,7]
m = [4,5,6,8]
print(somma_vettoriale(l,m))