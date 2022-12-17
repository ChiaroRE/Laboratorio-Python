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
      i = 0
      for i in range(len(item)):
          if(i != 0):
            try:
              item[i] = float(item[i])
              print(item[i])
            except (ValueError, TypeError):
              if(item[i] == None):
                raise ValueError('The item is empty')
              else:
                raise TypeError('The item cannot be converted into float')

    return lista





