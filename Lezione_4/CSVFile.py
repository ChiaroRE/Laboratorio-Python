class CSVFile():
  
  def _init_(self, nome_file):

    self.nome_file = nome_file

  def _str_(self):

    return 'CSVfile "{}"'.format(self.nome_file)

  def get_data(self, nome_file):

    my_file = open(nome_file, "r")

    valori = []

    for line in my_file: 

      elementi = line.split(",")
      
      valori.append(elementi)

    print(valori)

file = CSVFile('shampoo_sales (copy).csv')
file.get_data()

      

  
    