def sum_csv(file_name):

  my_file = open(file_name, "r")

  values = []
  
  for line in my_file:

    elements = line.split(',')

    if elements[0] != 'Date':

      value = float(elements[1])
      values.append(value)

  somma = sum(values)
  
  return somma

  
sum = sum_csv("shampoo_sales.csv")
print("La somma è: {}".format(sum))
