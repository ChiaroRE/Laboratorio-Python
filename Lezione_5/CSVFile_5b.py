class CSVFile():

  def __init__(self, name):
    self.name = name

  def get_data(self):
    lista = []
    
    try:
      my_file = open(self.name, 'r')
      
    except FileNotFoundError:
      print('Errore : file inesistente')

    for line in my_file:
      elements = line.split(',')
      if(elements[0] != 'Date'):
        elements[1] = elements[1].replace('\n','')
        lista.append(elements)
        
      
    return lista

class NumericalCSVFile(CSVFile):

  def __init__(self,name):
    super().__init__(name)

  def get_data(self):
    lista = super().get_data()
    for item in lista:
      for i in range(1,len(item)):
          try:
            item[i] = float(item[i])
          except ValueError or IndexError:
            print('Errore')
    return lista





