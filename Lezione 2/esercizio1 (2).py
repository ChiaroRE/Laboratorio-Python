def sum_list(lista):
  risultato = 0
  if len(lista) == 0:
    return None
  else:
    for i in lista:
      risultato = risultato + i
    return risultato
  
